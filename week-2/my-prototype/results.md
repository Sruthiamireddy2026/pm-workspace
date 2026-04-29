# Eval Run — 2026-04-23 20:44:31

- Test cases: **4**  
- Errors: **0**  
- Overall weighted score: **4.88**

## Per-criterion averages

| Criterion | Avg | N | Weight |
|---|---|---|---|
| factual_accuracy | 5.0 | 4 | Critical |
| completeness | 4.75 | 4 | High |
| actionability | 5.0 | 4 | High |
| scannability | 4.5 | 4 | Medium |

## Per-case results

| ID | Difficulty | Status | factual_accuracy | completeness | actionability | scannability |
|---|---|---|---|---|---|---|
| adversarial-01 | adversarial | ok | 5 | 5 | 5 | 5 |
| easy-01 | easy | ok | 5 | 5 | 5 | 5 |
| hard-01 | hard | ok | 5 | 4 | 5 | 4 |
| realistic-01 | realistic | ok | 5 | 5 | 5 | 4 |

## Thresholds

- **ship_if**: factual_accuracy avg >= 4.5 across all cases, zero adversarial cases score below 4 on factual_accuracy, completeness avg >= 4.0, actionability avg >= 4.0
- **iterate_if**: any criterion avg below 3.5, or adversarial-01 scores below 3 on factual_accuracy, or more than one case omits a blocked or overdue item
- **pivot_if**: factual_accuracy avg below 3.5 after two prompt iterations, or adversarial-01 consistently fabricates assignees or due dates after targeted prompt fixes
