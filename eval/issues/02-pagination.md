# Issue #2 — Pagination off-by-one

**Original task:** [Khiem's benchmark issue #2](https://github.com/HawKhiem/warp-factory-sandbox/issues/2)  
**Factory submission:** [PR #8](https://github.com/anushree-goyal/factory-sandbox-factory/pull/8) (private repository access may be required)  
**Model/workflow:** Factory AI Droid, NVIDIA Nemotron 3 Ultra free OpenRouter route

| Field | Observed result |
|---|---|
| First handling aligned to benchmark rubric | **Yes** |
| Eventual rubric-aligned outcome | **Yes (provisional)** |
| Corrective human feedback rounds | **0** |
| Recorded selected-run tokens | **284,886** |
| API calls | **20** (from request-level rows) |
| Active session time (not PR elapsed time) | **62.2 seconds**; not comparable to Warp `minutes_to_pr` |
| API charges recorded | **$0.00** (free-route OpenRouter requests only) |

## What Factory did

Corrected the 1-based page offset from `page * size` to `(page - 1) * size` and added first- and second-page regression checks.

## Evidence and limitations

Patch reviewed, but suite execution not independently reproduced from the supplied archive.

**Code evidence:** [PR #8 sanitized diff](../../evidence/patches/factory-pr-8.patch)

## Contrast with Warp's published benchmark

Warp also corrected the root cause and reportedly added broader HTTP-level red/green tests for defaults and later pages. See [Warp's original scorecard](https://github.com/HawKhiem/warp-factory-sandbox/blob/main/eval/scorecard.csv); the Warp run was not independently repeated for this report.

## Lesson for CSEE

Regression tests should exercise the API contract as well as a helper function.
