# Issue #5 — Monotonic creation timestamps

**Original task:** [Khiem's benchmark issue #5](https://github.com/HawKhiem/warp-factory-sandbox/issues/5)  
**Factory submission:** [PR #11](https://github.com/anushree-goyal/factory-sandbox-factory/pull/11) (private repository access may be required)  
**Model/workflow:** Factory AI Droid, NVIDIA Nemotron 3 Ultra free OpenRouter route

| Field | Observed result |
|---|---|
| First handling aligned to benchmark rubric | **No** |
| Eventual rubric-aligned outcome | **Yes (provisional)** |
| Corrective human feedback rounds | **1** |
| Recorded selected-run tokens | **744,956** |
| API calls | **35** (from request-level rows) |
| Active session time (not PR elapsed time) | **243.7 seconds**; not comparable to Warp `minutes_to_pr` |
| API charges recorded | **$0.00** (free-route OpenRouter requests only) |

## What Factory did

First PR #11 was incorrect on repeated same-millisecond creation and rollover; after one explicit human review intervention, PR #11-v2 used monotonic epoch-millisecond logic and added tests.

## Evidence and limitations

First attempt is a failure. Patch inspection supports the revised algorithm but supplied tests do not freeze time. Full 40-run CI evidence was not supplied.

**Code evidence:** [PR #11 sanitized diff](../../evidence/patches/factory-pr-11.patch), [initial failing patch](../../evidence/patches/factory-pr-11.patch), [revised patch](../../evidence/patches/factory-pr-11-v2.patch)

## Contrast with Warp's published benchmark

Warp used a deterministic mocked-clock test strategy and reported 40/40 runs, with no corrective human intervention. See [Warp's original scorecard](https://github.com/HawKhiem/warp-factory-sandbox/blob/main/eval/scorecard.csv); the Warp run was not independently repeated for this report.

## Generalizable lesson

A retry only improves eventual success; it must never retroactively count as first-attempt success.
