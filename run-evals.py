#!/usr/bin/env python3
"""
run-evals.py — Reference eval harness for Week 2 of "Claude Code for PMs".

What this does
--------------
Runs LLM-as-judge evals on your prototype's AI feature output by shelling out
to headless Claude Code (`claude -p --bare "..."`). No Anthropic API key
required: Claude Code handles auth, we just pipe prompts through it and
collect scores. The --bare flag keeps each call lean (no CLAUDE.md, hooks, or
memory loaded), and judge calls default to Haiku to conserve tokens.

The pattern is simple enough to teach and powerful enough to be real:

    for each test case:
        1. call `claude -p --bare <product_prompt + input_data>` -> feature output
        2. call `claude -p --bare --model haiku <judge + rubric>` -> JSON scores
    aggregate -> write results.json and results.md -> print summary

Inputs (sibling files you create; see --init to scaffold them):
    test-cases.json     list of {id, description, input_data, difficulty}
    rubric.json         list of {criterion, weight, five_out_of_five, one_out_of_five}
    product-prompt.md   the actual prompt your feature uses (this is what's tested)
    thresholds.json     {ship_if, iterate_if, pivot_if} strings

Usage:
    python3 run-evals.py --init              # scaffold starter files here
    python3 run-evals.py                     # run with defaults (haiku judge)
    python3 run-evals.py --judge-model default  # use same model for judge too
    python3 run-evals.py --parallel 6 \
        --out results/run-01.json            # results.json + results.md next to it

Default file paths resolve relative to --test-cases' directory, so you can run
this from anywhere in your project once the eval files exist.
"""

from __future__ import annotations

import argparse
import tempfile
import concurrent.futures as cf
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path


DEFAULT_TIMEOUT = 120
DEFAULT_PARALLEL = 4
DEFAULT_JUDGE_MODEL = "haiku"
MAX_CASES_WARNING = 5


# ---------------------------------------------------------------------------
# I/O
# ---------------------------------------------------------------------------

def load_inputs(test_cases_path: Path, rubric_path: Path,
                product_prompt_path: Path, thresholds_path: Path):
    """Load and lightly validate the four input files."""
    def _read_json(p: Path):
        if not p.exists():
            sys.exit(f"Missing input file: {p}\n"
                     f"Run `python3 {sys.argv[0]} --init` to scaffold starter files.")
        try:
            return json.loads(p.read_text())
        except json.JSONDecodeError as e:
            sys.exit(f"Invalid JSON in {p}: {e}")

    cases = _read_json(test_cases_path)
    rubric = _read_json(rubric_path)
    thresholds = _read_json(thresholds_path)

    if not product_prompt_path.exists():
        sys.exit(f"Missing product prompt file: {product_prompt_path}")
    product_prompt = product_prompt_path.read_text()

    for c in cases:
        for k in ("id", "description", "input_data"):
            if k not in c:
                sys.exit(f"Test case missing '{k}': {c}")
    for r in rubric:
        for k in ("criterion", "weight", "five_out_of_five", "one_out_of_five"):
            if k not in r:
                sys.exit(f"Rubric entry missing '{k}': {r}")
    for k in ("ship_if", "iterate_if", "pivot_if"):
        if k not in thresholds:
            sys.exit(f"Thresholds missing '{k}'")

    return cases, rubric, product_prompt, thresholds


# ---------------------------------------------------------------------------
# Prompt construction
# ---------------------------------------------------------------------------

def build_product_call(case: dict, product_prompt: str) -> str:
    """Compose the prompt that generates the feature output for a test case."""
    input_blob = json.dumps(case["input_data"], indent=2)
    return (
        f"{product_prompt.strip()}\n\n"
        f"---\nTEST CASE: {case['id']} ({case.get('difficulty', 'n/a')})\n"
        f"DESCRIPTION: {case['description']}\n\n"
        f"INPUT DATA (JSON):\n{input_blob}\n"
    )


def build_judge_prompt(case: dict, product_output: str, rubric: list) -> str:
    """Compose the judge prompt. Asks for JSON-only output with fixed shape."""
    criteria_lines = []
    score_shape = []
    reasoning_shape = []
    for r in rubric:
        anchors = f"5/5 = {r['five_out_of_five']} | 1/5 = {r['one_out_of_five']}"
        if "three_out_of_five" in r:
            anchors = (f"5/5 = {r['five_out_of_five']} | "
                       f"3/5 = {r['three_out_of_five']} | "
                       f"1/5 = {r['one_out_of_five']}")
        criteria_lines.append(
            f"- {r['criterion']} (weight: {r['weight']}): {anchors}"
        )
        score_shape.append(f'"{r["criterion"]}": <1-5 integer>')
        reasoning_shape.append(f'"{r["criterion"]}": "<one sentence>"')

    shape = (
        "{\n"
        '  "scores": {' + ", ".join(score_shape) + "},\n"
        '  "reasoning": {' + ", ".join(reasoning_shape) + "}\n"
        "}"
    )

    input_blob = json.dumps(case["input_data"], indent=2)

    return (
        "You are an eval judge. Score the PRODUCT OUTPUT below against the RUBRIC.\n"
        "You have the original INPUT DATA — use it to verify every fact in the output.\n"
        "Return ONLY valid JSON, no preamble, no code fences, no commentary.\n\n"
        f"TEST CASE: {case['id']} — {case['description']}\n\n"
        "INPUT DATA (this is what the product was given):\n"
        "<<<INPUT>>>\n"
        f"{input_blob}\n"
        "<<<END INPUT>>>\n\n"
        "PRODUCT OUTPUT (this is what the product generated — judge this):\n"
        "<<<OUTPUT>>>\n"
        f"{product_output}\n"
        "<<<END OUTPUT>>>\n\n"
        "RUBRIC:\n" + "\n".join(criteria_lines) + "\n\n"
        "Return JSON with this EXACT shape (keys must match criterion names exactly):\n"
        f"{shape}\n"
    )


# ---------------------------------------------------------------------------
# Subprocess layer
# ---------------------------------------------------------------------------

def run_claude(prompt: str, timeout: int = DEFAULT_TIMEOUT,
               model: str | None = None) -> str:
    """Invoke `claude -p <prompt>` and return stdout. Raises on failure."""
    if shutil.which("claude") is None:
        sys.exit(
            "`claude` is not on PATH. Install/verify Claude Code first.\n"
            "See course/week-2-prototyping/local-project-setup.md."
        )
    cmd = ["claude", "-p", prompt]
    if model:
        cmd.extend(["--model", model])
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout,
                cwd=tmpdir,
            )
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"claude -p timed out after {timeout}s")
    if result.returncode != 0:
        raise RuntimeError(
            f"claude -p exited {result.returncode}: {result.stderr.strip()[:400]}"
        )
    return result.stdout.strip()


def parse_judge_output(text: str, rubric: list) -> dict:
    """Parse the judge's JSON reply. Tolerates preamble/code fences."""
    # Models occasionally add preamble or ```json fences; strip them.
    candidates = []
    candidates.append(text.strip())
    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if fenced:
        candidates.append(fenced.group(1))
    braced = re.search(r"\{.*\}", text, re.DOTALL)
    if braced:
        candidates.append(braced.group(0))

    last_err = None
    for blob in candidates:
        try:
            data = json.loads(blob)
            break
        except json.JSONDecodeError as e:
            last_err = e
            data = None
    if data is None:
        raise ValueError(f"Could not parse judge output as JSON: {last_err}")

    scores = data.get("scores", {})
    reasoning = data.get("reasoning", {})
    parsed = {}
    for r in rubric:
        name = r["criterion"]
        if name not in scores:
            raise ValueError(f"Judge missing criterion '{name}' in scores")
        try:
            val = int(scores[name])
        except (TypeError, ValueError):
            raise ValueError(f"Non-integer score for '{name}': {scores[name]!r}")
        if not 1 <= val <= 5:
            raise ValueError(f"Score out of range 1-5 for '{name}': {val}")
        parsed[name] = {"score": val, "reason": reasoning.get(name, "")}
    return parsed


# ---------------------------------------------------------------------------
# Per-case execution
# ---------------------------------------------------------------------------

def score_case(case: dict, product_prompt: str, rubric: list,
               timeout: int, judge_model: str | None = None) -> dict:
    """Run one test case end to end. Returns a result dict with status info."""
    started = time.time()
    result = {
        "id": case["id"],
        "description": case["description"],
        "difficulty": case.get("difficulty", "n/a"),
        "status": "ok",
        "error": None,
        "product_output": None,
        "judge_raw": None,
        "scores": None,
        "elapsed_s": None,
    }
    try:
        product_call = build_product_call(case, product_prompt)
        product_output = run_claude(product_call, timeout=timeout)
        result["product_output"] = product_output

        judge_prompt = build_judge_prompt(case, product_output, rubric)
        judge_raw = run_claude(judge_prompt, timeout=timeout,
                               model=judge_model)
        result["judge_raw"] = judge_raw

        result["scores"] = parse_judge_output(judge_raw, rubric)
    except Exception as e:
        result["status"] = "error"
        result["error"] = f"{type(e).__name__}: {e}"
    finally:
        result["elapsed_s"] = round(time.time() - started, 2)
    return result


# ---------------------------------------------------------------------------
# Aggregation + reporting
# ---------------------------------------------------------------------------

def summarize(results: list, rubric: list, thresholds: dict) -> dict:
    """Compute per-criterion averages and a weighted overall score."""
    totals = {r["criterion"]: [] for r in rubric}
    for res in results:
        if res["status"] != "ok" or not res["scores"]:
            continue
        for name, entry in res["scores"].items():
            totals[name].append(entry["score"])

    per_criterion = {}
    for r in rubric:
        vals = totals[r["criterion"]]
        avg = round(sum(vals) / len(vals), 2) if vals else None
        per_criterion[r["criterion"]] = {
            "avg": avg,
            "n": len(vals),
            "weight": r["weight"],
        }

    weighted_num = 0.0
    weighted_den = 0.0
    for r in rubric:
        avg = per_criterion[r["criterion"]]["avg"]
        if avg is None:
            continue
        # Weight may be numeric or a label like "Critical"/"High"/"Medium".
        w = r["weight"]
        if isinstance(w, str):
            w = {"critical": 3, "high": 2, "medium": 1, "low": 0.5}.get(
                w.strip().lower(), 1
            )
        weighted_num += avg * w
        weighted_den += w
    overall = round(weighted_num / weighted_den, 2) if weighted_den else None

    errors = [r for r in results if r["status"] != "ok"]

    return {
        "per_criterion": per_criterion,
        "overall_weighted": overall,
        "total_cases": len(results),
        "error_cases": len(errors),
        "thresholds": thresholds,
    }


def write_markdown_report(out_path: Path, results: list, summary: dict,
                          rubric: list) -> None:
    """Write a human-readable summary table next to the JSON results."""
    lines = []
    lines.append(f"# Eval Run — {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    lines.append(f"- Test cases: **{summary['total_cases']}**  ")
    lines.append(f"- Errors: **{summary['error_cases']}**  ")
    lines.append(f"- Overall weighted score: **{summary['overall_weighted']}**\n")

    lines.append("## Per-criterion averages\n")
    lines.append("| Criterion | Avg | N | Weight |")
    lines.append("|---|---|---|---|")
    for r in rubric:
        c = summary["per_criterion"][r["criterion"]]
        lines.append(
            f"| {r['criterion']} | {c['avg']} | {c['n']} | {c['weight']} |"
        )
    lines.append("")

    lines.append("## Per-case results\n")
    header_cols = ["ID", "Difficulty", "Status"] + [r["criterion"] for r in rubric]
    lines.append("| " + " | ".join(header_cols) + " |")
    lines.append("|" + "|".join(["---"] * len(header_cols)) + "|")
    for res in results:
        row = [res["id"], res["difficulty"], res["status"]]
        if res["status"] == "ok" and res["scores"]:
            for r in rubric:
                row.append(str(res["scores"][r["criterion"]]["score"]))
        else:
            row.extend(["-"] * len(rubric))
        lines.append("| " + " | ".join(row) + " |")
    lines.append("")

    lines.append("## Thresholds\n")
    for k in ("ship_if", "iterate_if", "pivot_if"):
        lines.append(f"- **{k}**: {summary['thresholds'][k]}")
    lines.append("")

    errors = [r for r in results if r["status"] != "ok"]
    if errors:
        lines.append("## Errors\n")
        for e in errors:
            lines.append(f"- `{e['id']}`: {e['error']}")
        lines.append("")

    out_path.write_text("\n".join(lines))


def print_terminal_summary(summary: dict, rubric: list) -> None:
    print()
    print("=" * 60)
    print(f"Eval run complete: {summary['total_cases']} cases, "
          f"{summary['error_cases']} errors")
    print("-" * 60)
    for r in rubric:
        c = summary["per_criterion"][r["criterion"]]
        avg = c["avg"] if c["avg"] is not None else "n/a"
        print(f"  {r['criterion']:<24} avg={avg}  n={c['n']}  weight={c['weight']}")
    print("-" * 60)
    print(f"  Overall weighted score: {summary['overall_weighted']}")
    print("=" * 60)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Run LLM-as-judge evals via headless Claude Code."
    )
    parser.add_argument("--test-cases", default="test-cases.json")
    parser.add_argument("--rubric", default="rubric.json")
    parser.add_argument("--product-prompt", default="product-prompt.md")
    parser.add_argument("--thresholds", default="thresholds.json")
    parser.add_argument("--out", default="results.json",
                        help="Results JSON path (a .md summary is written alongside).")
    parser.add_argument("--parallel", type=int, default=DEFAULT_PARALLEL,
                        help=f"Max concurrent test cases (default {DEFAULT_PARALLEL}).")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT,
                        help=f"Per-call timeout in seconds (default {DEFAULT_TIMEOUT}).")
    parser.add_argument("--judge-model", default=DEFAULT_JUDGE_MODEL,
                        help=f"Model for judge calls (default '{DEFAULT_JUDGE_MODEL}'). "
                             "Use 'default' to use the same model as product calls.")
    parser.add_argument("--init", action="store_true",
                        help="Write starter eval files into the current directory and exit.")
    args = parser.parse_args()

    if args.init:
        _scaffold_example_files(Path.cwd())
        return

    # Resolve paths relative to the test-cases file's directory.
    cases_path = Path(args.test_cases).expanduser().resolve()
    base = cases_path.parent
    rubric_path = _resolve_rel(args.rubric, base)
    prompt_path = _resolve_rel(args.product_prompt, base)
    thresh_path = _resolve_rel(args.thresholds, base)
    out_path = _resolve_rel(args.out, base)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    cases, rubric, product_prompt, thresholds = load_inputs(
        cases_path, rubric_path, prompt_path, thresh_path
    )

    if len(cases) > MAX_CASES_WARNING:
        print(f"⚠  You have {len(cases)} test cases. To conserve tokens on a Pro "
              f"plan, consider trimming to {MAX_CASES_WARNING} or fewer.")
        print(f"   (Each case = 2 Claude calls. With iterations you could hit "
              f"{len(cases) * 2 * 3} calls total.)\n")

    judge_model = None if args.judge_model == "default" else args.judge_model

    print(f"Running {len(cases)} test case(s) with parallelism={args.parallel}"
          f", judge-model={args.judge_model}...")
    results = []
    # ThreadPool is correct here: we're waiting on subprocess I/O, not CPU.
    with cf.ThreadPoolExecutor(max_workers=max(1, args.parallel)) as pool:
        futures = {
            pool.submit(score_case, c, product_prompt, rubric, args.timeout,
                        judge_model): c
            for c in cases
        }
        for fut in cf.as_completed(futures):
            res = fut.result()
            marker = "ok " if res["status"] == "ok" else "ERR"
            print(f"  [{marker}] {res['id']} ({res['elapsed_s']}s)")
            results.append(res)

    results.sort(key=lambda r: r["id"])
    summary = summarize(results, rubric, thresholds)

    out_path.write_text(json.dumps(
        {"summary": summary, "results": results}, indent=2
    ))
    md_path = out_path.with_suffix(".md")
    write_markdown_report(md_path, results, summary, rubric)

    print_terminal_summary(summary, rubric)
    print(f"\nJSON:     {out_path}")
    print(f"Markdown: {md_path}")


def _resolve_rel(p: str, base: Path) -> Path:
    pp = Path(p).expanduser()
    return pp if pp.is_absolute() else (base / pp).resolve()


# ---------------------------------------------------------------------------
# --init scaffolding
# ---------------------------------------------------------------------------

EXAMPLE_FILES = {
    "test-cases.json": """\
[
  {
    "id": "easy-01",
    "description": "Small clean project set with one obvious blocker.",
    "difficulty": "easy",
    "input_data": {
      "projects": [
        {"id": "PRJ-A", "name": "Sample project", "status": "blocked",
         "tasks": [{"title": "Legal review", "status": "blocked", "due": "2026-04-10"}]}
      ]
    }
  },
  {
    "id": "realistic-01",
    "description": "Mid-sized project set with mixed signals.",
    "difficulty": "realistic",
    "input_data": {
      "projects": [
        {"id": "PRJ-B", "name": "Website rebrand", "status": "at_risk",
         "tasks": [{"title": "Copy rewrites", "status": "in_progress", "due": "2026-04-10"}]},
        {"id": "PRJ-C", "name": "Paid ads", "status": "blocked",
         "tasks": [{"title": "Audience research", "status": "not_started", "due": "2026-04-03"}]}
      ]
    }
  }
]
""",
    "rubric.json": """\
[
  {
    "criterion": "completeness",
    "weight": "High",
    "five_out_of_five": "Every real blocker and due-this-week item surfaced.",
    "one_out_of_five": "Misses more than half of real blockers."
  },
  {
    "criterion": "hallucination",
    "weight": "Critical",
    "five_out_of_five": "Zero fabricated owners, dates, or status claims.",
    "one_out_of_five": "Multiple invented facts."
  },
  {
    "criterion": "actionability",
    "weight": "High",
    "five_out_of_five": "Each item is specific, linked, and has a clear next step.",
    "one_out_of_five": "Vague statements with no linkage."
  },
  {
    "criterion": "readability",
    "weight": "Medium",
    "five_out_of_five": "Scannable in under 60 seconds, grouped coherently.",
    "one_out_of_five": "Wall of text, inconsistent structure."
  }
]
""",
    "product-prompt.md": """\
You are generating a weekly cross-project summary for a team lead at a
mid-market company. Use ONLY the data provided. Do not invent owners, dates,
or status. Group the summary by project. For each project, surface:

- What is due this week
- What is overdue
- Any blockers or risks

For every flagged item, cite the project by name and the specific task.
If data is missing, say so explicitly rather than guessing.

Output in plain markdown. Keep it scannable. Aim for under 300 words.
""",
    "thresholds.json": """\
{
  "ship_if": "completeness avg >= 4.0, hallucination 5/5 on 95%+ of cases, actionability avg >= 4.0, zero critical failures",
  "iterate_if": "any criterion below 3.5 avg, or hallucination scores below 5 on more than 5% of cases",
  "pivot_if": "hallucination averages below 4.0 even after two prompt iterations"
}
""",
}


def _scaffold_example_files(target_dir: Path) -> None:
    wrote = []
    skipped = []
    for name, body in EXAMPLE_FILES.items():
        p = target_dir / name
        if p.exists():
            skipped.append(name)
            continue
        p.write_text(body)
        wrote.append(name)
    print("Scaffolded starter eval files in:", target_dir)
    for n in wrote:
        print(f"  wrote    {n}")
    for n in skipped:
        print(f"  skipped  {n} (already exists)")
    if wrote:
        print("\nNext: edit these to match your feature, then run:")
        print(f"  python3 {os.path.basename(sys.argv[0])}")


if __name__ == "__main__":
    main()
