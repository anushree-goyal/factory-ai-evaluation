# Issue #3 — Slugify: accents and whitespace

**Original task:** [Khiem's benchmark issue #3](https://github.com/HawKhiem/warp-factory-sandbox/issues/3)  
**Factory submission:** [PR #9](https://github.com/anushree-goyal/factory-sandbox-factory/pull/9) (private repository access may be required)  
**Model/workflow:** Factory AI Droid, NVIDIA Nemotron 3 Ultra free OpenRouter route

| Field | Observed result |
|---|---|
| First handling aligned to benchmark rubric | **Yes** |
| Eventual rubric-aligned outcome | **Yes (provisional)** |
| Corrective human feedback rounds | **0** |
| Recorded selected-run tokens | **354,196** |
| API calls | **27** (from request-level rows) |
| Active session time (not PR elapsed time) | **163.1 seconds**; not comparable to Warp `minutes_to_pr` |
| API charges recorded | **$0.00** (free-route OpenRouter requests only) |

## What Factory did

Applied Unicode NFD normalization, stripped combining marks and collapsed whitespace; added accented-string and whitespace cases.

## Evidence and limitations

Factory patch does not cover all existing-hyphen or trimming cases. The initial session was resumed; abandoned Qwen attempts are excluded.

**Code evidence:** [PR #9 sanitized diff](../../evidence/patches/factory-pr-9.patch)

## Contrast with Warp's published benchmark

Warp wrote broader edge-case tests but its published review still disclosed Unicode corner cases it missed. See [Warp's original scorecard](https://github.com/HawKhiem/warp-factory-sandbox/blob/main/eval/scorecard.csv); the Warp run was not independently repeated for this report.

## Generalizable lesson

A broad text-processing fix needs adversarial Unicode cases and a documented character-set contract.
