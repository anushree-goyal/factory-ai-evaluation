# Issue #4 — Filter todos by done status

**Original task:** [Khiem's benchmark issue #4](https://github.com/HawKhiem/warp-factory-sandbox/issues/4)  
**Factory submission:** [PR #10](https://github.com/anushree-goyal/factory-sandbox-factory/pull/10) (private repository access may be required)  
**Model/workflow:** Factory AI Droid, NVIDIA Nemotron 3 Ultra free OpenRouter route

| Field | Observed result |
|---|---|
| First handling aligned to benchmark rubric | **Yes** |
| Eventual rubric-aligned outcome | **Yes (provisional)** |
| Corrective human feedback rounds | **0** |
| Recorded selected-run tokens | **510,269** |
| API calls | **29** (from request-level rows) |
| Active session time (not PR elapsed time) | **148.2 seconds**; not comparable to Warp `minutes_to_pr` |
| API charges recorded | **$0.00** (free-route OpenRouter requests only) |

## What Factory did

Implemented `done=true/false` filtering before pagination, invalid-parameter 400 behavior and README updates.

## Evidence and limitations

Tests do not directly prove cross-page filtered totals and exhibit fixture/test-order coupling.

**Code evidence:** [PR #10 sanitized diff](../../evidence/patches/factory-pr-10.patch)

## Contrast with Warp's published benchmark

Warp reportedly exercised page-two totals and multiple invalid parameter cases against the baseline and patch. See [Warp's original scorecard](https://github.com/HawKhiem/warp-factory-sandbox/blob/main/eval/scorecard.csv); the Warp run was not independently repeated for this report.

## Lesson for CSEE

Tests must establish filtered totals and independence from prior test execution order.
