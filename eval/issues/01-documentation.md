# Issue #1 — Local development documentation

**Original task:** [Khiem's benchmark issue #1](https://github.com/HawKhiem/warp-factory-sandbox/issues/1)  
**Factory submission:** [PR #7](https://github.com/anushree-goyal/factory-sandbox-factory/pull/7) (private repository access may be required)  
**Model/workflow:** Factory AI Droid, NVIDIA Nemotron 3 Ultra free OpenRouter route

| Field | Observed result |
|---|---|
| First handling aligned to benchmark rubric | **Yes (provisional)** |
| Eventual rubric-aligned outcome | **Yes (provisional)** |
| Corrective human feedback rounds | **0** |
| Recorded selected-run tokens | **280,995** |
| API calls | **20** (from request-level rows) |
| Active session time (not PR elapsed time) | **50.6 seconds**; not comparable to Warp `minutes_to_pr` |
| API charges recorded | **$0.00** (free-route OpenRouter requests only) |

## What Factory did

The agent reportedly updated local setup documentation, stayed in scope, passed 9/9 tests after a retry and passed lint.

## Evidence and limitations

No PR #7 patch supplied. Test/merge outcomes are experimenter-reported, not independently re-run.

**Code evidence:** No Factory diff for PR #7 was included in the evidence package.

## Contrast with Warp's published benchmark

Warp made a README-only fix, noted the unrelated flaky test, and avoided expanding scope. See [Warp's original scorecard](https://github.com/HawKhiem/warp-factory-sandbox/blob/main/eval/scorecard.csv); the Warp run was not independently repeated for this report.

## Lesson for CSEE

No code patch is included for #1; the PR is linked but may require access to the private Factory experiment repository.
