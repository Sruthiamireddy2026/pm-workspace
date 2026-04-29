# PRD: AI Weekly Cross-Project Summary

**Status:** Draft
**Date:** 2026-04-23
**Hypothesis:** An AI-generated weekly cross-project summary for TaskFlow team leads.

---

## 1. Problem Statement

Team leads managing 15–20 concurrent projects spend 30+ minutes every Monday manually
aggregating cross-project status — a workflow TaskFlow does not support natively, forcing
users to build and maintain parallel tracking systems outside the product. The behavior is
both daily friction and a concrete churn signal: named users have set explicit windows
before evaluating competitors, and the synthesis confirms that retention is currently driven
by migration cost, not product satisfaction. TaskFlow's existing AI summary feature is
already used and praised, making AI-generated weekly cross-project synthesis the most
tractable extension of a foundation that already works.

---

## 2. Research Summary

- Team leads spend ~30 min/Monday clicking through individual projects to build a status
  picture that TaskFlow provides no native view for; parallel Google Sheets are the
  standard workaround. *"It's dumb but it's the only way I can see across everything."*
  — source: multi-source-triangulation-2026-04-22.md (Rachel Torres, GreenPath Studios)
- Retention is currently driven by lock-in (migration cost, Slack integration), not
  product satisfaction. *"If a competitor reduces migration friction, the retention floor
  drops."* — source: multi-source-triangulation-2026-04-22.md
- The existing AI task summary feature is valued by daily users but produces generic output
  because the model has no team context. *"If the AI knew that 'GTM launch' means a
  specific process at our company… the output would be much more useful."*
  — source: multi-source-triangulation-2026-04-22.md (Rachel Torres); corroborated by
  survey respondent 17 (PM, 120-person SaaS co): *"AI doesn't know anything about our
  product context."*
- Only 4 of 12 licensed seats on Rachel's team are actively used after 8 months. The
  cross-project gap is part of why she alone owns the aggregation workflow — her team
  has no incentive to engage at the summary level.
  — source: multi-source-triangulation-2026-04-22.md
- Second independent respondent confirms the gap: *"No cross-project view — I can't see
  everything due this week in one place."* NPS 6. Would improve: portfolio or multi-project
  dashboard view. — source: 2026-04-13-feedback-synthesis.md (survey respondent 2,
  Marketing Manager, 45-person company)
- Cross-project portfolio views are table stakes in adjacent analytics and HR tech products.
  In people analytics platforms, the executive dashboard is typically the product entry
  point, not a later roadmap item. TaskFlow's gap is 2–3 cycles behind industry norm.
  — source: roadmap-cross-reference-2026-04-22.md
- RICE analysis scores this at 4.1 (Q3), with Medium evidence confidence — rated below
  notification overhaul (18.0) and onboarding redesign (7.2). Context for sequencing, not
  a reason to deprioritize feature definition.
  — source: roadmap-cross-reference-2026-04-22.md

---

## 3. Users and Use Cases

**Primary user:** Team leads managing 10–20+ people across 10–20+ concurrent projects at
mid-market companies (40–300 employees). Specifically: marketing ops managers, program
managers, and operations leads who are the single point of status aggregation for their
team. These users are also the economic buyers or primary renewal influencers — their
satisfaction directly shapes contract outcomes.

**Use cases:**
- Monday morning review: generate this week's cross-project status before standup,
  replacing the manual 30-minute aggregation ritual
- Mid-week check-in: targeted scan for what has slipped or gone newly blocked since Monday
- Standup facilitation: run the team meeting directly from the summary instead of clicking
  through projects live

**Explicit exclusions:**
- Individual contributors: no cross-project scope, no aggregation need
- Enterprise accounts blocked on SSO and audit logs (TK-1202, TK-1213, survey R9, R16):
  security compliance is the primary blocker; a summary feature does not unblock renewal
- PMO directors at 500+ person firms needing resource management and capacity planning
  (survey R25): different problem scope, different data model, different roadmap position

---

## 4. User Journey with Ins and Outs

The AI summary is not on screen 1 (the existing dashboard). It lives one level deeper,
accessed from the left navigation or the project list.

| Step | Screen/State | Way In | User Action | Way Out |
|---|---|---|---|---|
| 1 | Existing Dashboard | App open, email link, Slack | Scans recent activity; no cross-project aggregation available here | Clicks "Weekly Summary" in left nav |
| 2 | Weekly Summary home | Left nav click | Sees last generated summary (if any) + "Generate this week's summary" button; date range defaults to current Mon–Sun | Clicks Generate |
| 3 | Generating state | Clicked Generate | Sees progress indicator; AI scanning all active projects (~5–15 sec) | Auto-advances when complete |
| 4 | Summary results | Auto-advance | Reads grouped-by-project output; blocked and overdue items lead within each group | Clicks a task to update, or shares/exports |
| 5 | Inline task update | Clicked a task row | Updates status, assignee, or adds a comment without navigating away from the summary | Saves and returns to summary view |
| 6 | Share / export | Clicked Share | Copies a read-only link or pushes to a connected Slack channel | Returns to summary or navigates away |

---

## 5. Goals and Non-Goals

**Goals (measurable):**
- Reduce Monday cross-project review time from ~30 min to <5 min for team leads managing
  10+ active projects. Measured via session event data (time from app open to first standup
  action or task update). Target: 30-day post-launch.
- 60%+ of generated summaries rated accurate by the generating team lead (inline thumbs
  prompt). Target: 60-day post-launch.
- 40% reduction in connected parallel tracking among team-lead accounts. Proxy: decrease in
  Google Sheets integrations, supplemented by direct survey. Target: 90-day post-launch.

**Non-Goals (specific):**
- Real-time live dashboard: this is a generated point-in-time summary, not a streaming
  view. Live status requires different infrastructure and is a distinct roadmap item.
- Notification system overhaul: rated higher priority (RICE 18.0) and should ship before
  or in parallel — not folded into this scope.
- Onboarding redesign: higher RICE score (7.2), already on Q2 roadmap. Not in scope here.
- Gantt / timeline / dependency views: separately requested Q3 item; requires dependency
  data modeling beyond this feature.
- Team context customization (teaching the AI company terminology and process norms): Phase
  2. Phase 1 ships factual accuracy; Phase 2 ships contextual relevance.
- Resource management and capacity planning: different buyer, different data model,
  different Q3+ scope. Not this feature.

---

## 6. Functional Requirements

1. The system generates a cross-project summary covering all active projects the requesting
   user owns or is team lead on, scoped to the current calendar week.
2. The summary groups output by project. Within each project it surfaces: tasks due within
   7 days, overdue tasks (due date past and status is not "done"), and blocked tasks or
   projects (status = blocked or a blocker field is populated).
3. Projects with no due-this-week, overdue, or blocked items are excluded from the summary.
4. If a project is marked "on_track" but contains overdue tasks, the system surfaces the
   overdue tasks and flags the status discrepancy explicitly.
5. Each summary item displays: task name, assignee (or "Unassigned" if null), status,
   due date (or "No due date" if null), and blocker reason if present.
6. Each item links directly to its source task. Clicking opens an inline edit panel without
   navigating away from the summary.
7. The system uses only data present in TaskFlow. It does not infer, fabricate, or fill in
   missing values. If a field is null or absent, it states that explicitly.
8. Team leads can generate a new summary at any time. Auto-generation defaults to Monday
   at 8am local time (configurable per user).
9. Summaries can be shared via read-only link or pushed to a connected Slack channel.

---

## 7. Riskiest Assumption

My product only works if the AI can consistently surface the correct due, overdue, and
blocked tasks from a team lead's project data without hallucinating status, assignees, or
due dates that are not in the source data.

---

## 8. Eval Plan

**What we're testing:** Given a JSON payload of projects and tasks, does the AI produce
a summary that is factually accurate, complete, actionable, and scannable — without
fabricating any values not present in the input?

**Rubric:**

| Criterion | Weight | 5/5 looks like | 1/5 looks like |
|---|---|---|---|
| factual_accuracy | Critical | Every task name, assignee, due date, and status matches the input exactly. Null fields stated as "Unassigned" or "No due date" — never guessed. | Multiple fabricated assignees, dates, or statuses that contradict the input. |
| completeness | High | All overdue, due-this-week, and blocked items from the input appear in the summary. Nothing significant omitted. | More than half of actionable items are missing. |
| actionability | High | Each item gives the team lead enough to act: task name, project, assignee, status, due date, blocker reason where present. No vague placeholders. | Vague summary with no task-level detail. Team lead must click into projects to understand what to do. |
| scannability | Medium | Readable in under 60 seconds. Grouped by project. Blocked and overdue items lead. No redundancy. | Wall of text. No grouping. Critical items buried or repeated. |

**Test cases:**

| ID | Description | Difficulty | Input |
|---|---|---|---|
| easy-01 | 3 projects, 1 blocked task, 1 overdue task. All fields populated. | easy | 3 projects, 5 tasks |
| realistic-01 | 6 projects, mixed statuses, cascading blocker, 1 null assignee. | realistic | 6 projects, 9 tasks |
| hard-01 | 12 projects, multiple simultaneous blockers, overlapping deadlines. | hard | 12 projects, 20 tasks |
| adversarial-01 | "on_track" project with 2 overdue tasks. Null assignees. Null due dates. Status mismatch. | adversarial | 3 projects, 7 tasks, null fields |

**Grading:**
- Ship if: factual_accuracy avg ≥ 4.5 across all cases; zero adversarial cases score below
  4 on factual_accuracy; completeness avg ≥ 4.0; actionability avg ≥ 4.0
- Iterate if: any criterion avg below 3.5; adversarial case scores below 3 on
  factual_accuracy; more than one case omits a blocked or overdue item
- Pivot if: factual_accuracy avg below 3.5 after two prompt iterations; adversarial-01
  consistently fabricates values after targeted prompt fixes

---

## 9. Success Metrics and Open Questions

**30-day:** % of eligible team leads (10+ active projects) who generate at least one
summary. Target: 30%.

**60-day:** Average Monday cross-project review session time drops below 10 minutes for
weekly summary users. Baseline: ~30 min from Rachel Torres interview. Proxy: Monday morning
time-in-app event data.

**90-day:** % of active team-lead accounts that have removed their connected Google Sheets
integrations (parallel-spreadsheet abandonment proxy). Target: 20% reduction from baseline.
Supplement with direct survey: "Do you maintain a tracking system outside TaskFlow?"

**Open Questions:**

| Question | Owner | Priority |
|---|---|---|
| Synthesis recommends follow-up interviews with survey R21 (Engineering Manager, 200-person co) and R25 (PMO Director, 500-person consulting firm) before scoping. Should this ship before those interviews, or after? | PM | High |
| Do we have session-level timing data to measure Monday review time today? Can we instrument it before launch? | Analytics / Engineering | High |
| How does the summary handle projects where the team lead has view-only access but is not the formal owner? Include or exclude? | Engineering / PM | High |
| RICE scores this Q3. What needs to be true to pull it into Q2 alongside notifications and onboarding — resourcing conversation or sequencing conversation? | PM / Leadership | High |
| Phase 2: what is the data model for team context (terminology, approval chains, process norms)? What does the AI actually need to produce less generic output? | PM | Medium |
| Should "blocked" detection rely only on explicit status fields, or infer from comment gaps and task inactivity? Inference raises completeness but raises hallucination risk. | PM / Engineering | Medium |
| Should timezone configurability ship day one, or is a single default (Monday 8am local) sufficient for the first cohort? | Engineering | Low |

---

## 10. Design Reference and Prototype Fidelity

**Reference products:** Linear, Slack, Notion, Workday

---

### Linear — clean status lists and information density

**Borrow:** The issue list row pattern — status badge left-anchored (color-coded: red for
blocked, orange for overdue, blue for in-progress), task title center-weighted, metadata
(assignee, due date) right-aligned. One row per item, no decorative chrome. Linear proves
you can surface 20+ items at high density without the view feeling overwhelming.

**Specific interaction to lift:** The flat list structure that makes item count visible
immediately — a team lead should be able to scan "there are 6 items needing attention
across 4 projects" within 2 seconds of the summary loading. Use Linear's status pill
treatment for the [BLOCKED], [OVERDUE], [DUE THIS WEEK] labels in each row.

**What not to copy:** Linear's left-sidebar project tree — that's navigation scaffolding
we don't need inside a digest view.

---

### Slack — digest format and weekly summary style

**Borrow:** The section-per-source structure: bold header anchors each group ("GTM Launch
— Product A"), followed by bullet items with just enough context to act without clicking.
The mental model Slack's weekly digest establishes — "read this once, know what needs you,
done" — is exactly the experience this summary should deliver.

**Specific interaction to lift:** The one-line item format: [label] task name — assignee —
due date — blocker reason if present. No multi-line expansions by default; details appear
on hover or click. Also borrow Slack's "muted" section header style for projects with only
due-this-week items (lower urgency than blocked/overdue).

**What not to copy:** Slack's threaded reply model or inbox-queue UX. The summary is a
snapshot, not a persistent to-do list. Don't make it feel like a queue the user has to
clear.

---

### Notion — dashboard card layout

**Borrow:** The card container that makes a weekly summary feel like a self-contained unit
with a defined boundary — not an infinite scroll or an open-ended feed. Notion's home page
card treatment, where generated/structured content sits inside a muted-background block
visually separated from editable fields, helps users immediately distinguish AI-generated
output from the inline task edit panel.

**Specific interaction to lift:** The week-as-a-card framing: each generated summary is
its own card with a header showing the date range and a "generated on [date]" timestamp.
Past summaries are accessible as previous cards. This gives team leads a lightweight
weekly history without building a separate archive feature.

**What not to copy:** Notion's freeform block editing canvas. The summary is structured
output — users update tasks via the inline panel, not by editing summary text directly.

---

### Workday — HR data display patterns

**Borrow:** Workday's "Awaiting Your Action" home panel — the closest existing product
pattern to what this summary should feel like for the target persona. It groups items by
category, shows owner and due date inline, and lets users click into the detail without
losing their place. Most mid-market ops managers and HR-adjacent team leads already use
Workday, making this a familiar mental model.

**Specific interaction to lift:** The priority grouping — items requiring immediate action
appear first with a distinct visual treatment (red/orange urgency signal), followed by
items due this week (neutral), followed by items coming up (muted). Apply this hierarchy
to the summary: blocked → overdue → due this week, within each project group.

**What not to copy:** Workday's dense form-based data entry UI. The reference is the
viewing and action-routing experience, not the editing flows. Workday's input forms are
notoriously slow and high-friction — the summary's inline edit panel should be the
opposite.

---

### Avoid list

- **Jira's dense metadata rows** — story points, sprint labels, fix versions, components
  per item. Wrong cognitive model for a weekly digest. Users stall at the table instead of
  acting.
- **Monday.com's color grid** — feels like a spreadsheet, requires horizontal scrolling,
  implies ongoing configuration. A summary should have zero setup cost.
- **Full Asana portfolio configuration UI** — requires "add projects to this portfolio"
  setup before delivering value. Our summary generates automatically with no configuration.
- **BI dashboard widget grid** — implies "watch this continuously." The summary is a
  periodic digest, not a live monitoring view.
- **Notification inbox / queue model** — don't make the summary feel like a list of items
  the user must triage and clear. Each summary is a snapshot; once read, it's done.

---

### Seeded data spec

The prototype must load with this sample data so the feature is testable and demo-ready
without placeholder text.

| Field | Sample value | Notes |
|---|---|---|
| Team lead | Rachel Torres | Matches the primary research persona |
| Active projects | 8 projects | Enough to show grouping value; not so many the view feels unmanageable |
| Project statuses | 3 on_track, 3 at_risk, 2 blocked | Mix that generates a non-trivial summary with all label types visible |
| Project names | Q2 Email Campaign, Brand Refresh, GTM Launch — Product A, Event Series Planning, Paid Ads Q2, Customer Newsletter, Sales Enablement Deck, Social Media Audit | Marketing ops naming from Rachel Torres interview — avoids "Project 1" feel |
| Tasks due this week | 6 tasks across 4 projects | Shows the filtering is doing real work |
| Overdue tasks | 2 tasks in 2 separate projects | Surfaces the overdue state distributed across projects, not stacked in one |
| Blocked tasks | 3 tasks across 2 projects | One with a written blocker reason; one without (to test the null-blocker display) |
| Assignee names | Marcus Lee, Dana Kim, Priya Nair, Rachel Torres, TBD | Real names for most; TBD on one to show the Unassigned state |
| Due dates | Mix of past (overdue), current week, and 2+ weeks out | Makes the date-filter logic visually demonstrable in the prototype |

---

### Prototype fidelity

Clickable mockup, not a working prototype. Must show four states:

1. **Summary home** — last generated summary visible, "Generate this week's summary"
   button prominent, date range selector defaulted to current week
2. **Generating state** — progress indicator, AI scanning projects, ~5–10 second
   animation
3. **Summary results** — full grouped-by-project output with all label types visible
   (BLOCKED, OVERDUE, DUE THIS WEEK); blocked and overdue items lead within each group
4. **Inline task update panel** — triggered by clicking a task row; shows editable status,
   assignee, and comment fields without navigating away from the summary

Engineers and design need enough fidelity to align on the results view layout before the
product prompt is written — the row structure and label hierarchy in state 3 directly
determines whether the AI output scans well when rendered.
