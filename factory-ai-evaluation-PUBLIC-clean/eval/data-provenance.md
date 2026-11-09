# Data provenance and evidence boundaries

## Supplied materials audited

The private source package contained OpenRouter request-level CSV exports, issue/session logs, a source manifest with SHA-256 checksums, an attribution script, derived ledgers, one #6 screenshot, and PR diffs for #2–#6 (including both versions of #5).

The comparison audit reported matching checksums and file sizes for **13 source-manifest entries** and rebuilt the issue-usage totals using a standard-library Python attribution script. This publication-oriented repository includes only the *aggregate results*, sanitized code diffs and technical write-up, not the raw provider exports or personally identifying session metadata. Therefore public `validate_results.py` verifies **consistency of published results**, not reconstruction from unpublished inputs.

## Source confidence

| Source category | Available public evidence | Confidence boundary |
|---|---|---|
| Factory issues #1–4 token usage | [Published per-issue aggregates](../data/factory-usage-by-issue.csv) | Totals obtained from timestamp-window-attributed provider requests; no direct provider-to-session ID link |
| Factory #5 tokens | Per-issue aggregate; two request bursts reported in methodology | Dedicated-key ledger exact for that key, but another overlapping shared-key call may relate to #5 |
| Factory #6 tokens | 842,382 selected-run aggregate; 39 screenshot-counted requests | User-confirmed association of a key-specific export with the final run, not individual timestamped requests |
| Factory code outcomes | [Sanitized PR patches](../evidence/README.md) and reviewed descriptions | Not an independent replay of all Node.js tests/CI; PR #7 missing |
| Warp benchmark | [Khiem's public repository](https://github.com/HawKhiem/warp-factory-sandbox), [scorecard](https://github.com/HawKhiem/warp-factory-sandbox/blob/main/eval/scorecard.csv) | Author-reviewed evidence, not independently rerun here |

## What is *not* published here

- Request-level `generation_id`, user/session IDs, key labels, timestamps, internal conversations and dashboard screenshots.
- Raw source CSVs and the internal rebuild script. Keep these in a **private evidence archive** with restricted reviewer access if audits require rebuilding the numbers.
- Unavailable Factory #1 patch or complete CI logs. Do not imply they exist in this repo.

## Quality of the test evidence

Code diffs, user-provided test confirmations and informal patch review support a provisional judgment. Formal reproducibility would require the full pinned baseline/PR commit hashes, test transcripts, random seeds or fixed clocks where relevant, and measured performance benchmarks on issue #6. Those are not claimed here.
