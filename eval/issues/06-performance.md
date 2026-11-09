# Issue #6 — Ambiguous API performance request

**Original task:** [Khiem's benchmark issue #6](https://github.com/HawKhiem/warp-factory-sandbox/issues/6)  
**Factory submission:** [PR #12](https://github.com/anushree-goyal/factory-sandbox-factory/pull/12) (private repository access may be required)  
**Model/workflow:** Factory AI Droid, NVIDIA Nemotron 3 Ultra free OpenRouter route

| Field | Observed result |
|---|---|
| First handling aligned to benchmark rubric | **No** |
| Eventual rubric-aligned outcome | **No — optimization without clarification/measurement** |
| Corrective human feedback rounds | **0** |
| Recorded selected-run tokens | **842,382** |
| API calls | **39** (from screenshot) |
| Active session time (not PR elapsed time) | **213.0 seconds**; not comparable to Warp `minutes_to_pr` |
| API charges recorded | **$0.00** (free-route OpenRouter requests only) |

## What Factory did

Agent produced PR #12 adding store-level pagination and map-backed ID lookup without asking clarifying questions.

## Evidence and limitations

No measured baseline or before/after latency/memory evidence. A functional test bearing an optimization name does not prove speedup. Earlier aborted run excluded.

**Code evidence:** [PR #12 sanitized diff](../../evidence/patches/factory-pr-12.patch)

## Contrast with Warp's published benchmark

Warp explicitly requested scope, then ran a load experiment and recommended no code change under the observed conditions. See [Warp's original scorecard](https://github.com/HawKhiem/warp-factory-sandbox/blob/main/eval/scorecard.csv); the Warp run was not independently repeated for this report.

## Generalizable lesson

The ability to pause, clarify and recommend no-op is part of correctness for ambiguous issues.
