# Code evidence index

These are the **sanitized patches supplied with the Factory evaluation package**, not freshly downloaded or independently verified GitHub changes. Authorship email addresses have been redacted for the shareable repository. They are retained for technical inspection, not as a guarantee the full PR/CI history was replayed.

| Benchmark issue | Evidence | Note |
|---|---|---|
| #1 | [Factory PR #7](https://github.com/anushree-goyal/factory-sandbox-factory/pull/7) | No patch was supplied; private PR may require access |
| #2 | [PR #8 patch](patches/factory-pr-8.patch) | Pagination fix and unit regression tests |
| #3 | [PR #9 patch](patches/factory-pr-9.patch) | Slug normalization and whitespace tests |
| #4 | [PR #10 patch](patches/factory-pr-10.patch) | Done filter and HTTP tests |
| #5 | [PR #11 initial patch](patches/factory-pr-11.patch), [PR #11 revised patch](patches/factory-pr-11-v2.patch) | First version fails a timestamp invariant; second follows corrective user feedback |
| #6 | [PR #12 patch](patches/factory-pr-12.patch) | Implementation candidate, not verified speedup |

**Review warning:** Patches for #5 represent sequential states. The revised file is a multi-commit patch; it must not be treated as a standalone independent baseline replay without respecting its commit order.

For rigorous red/green test demonstrations, use a clean checkout at the benchmark `baseline` commit and replay each patch/PR with an audited command transcript. These artifacts do not substitute for that execution.
