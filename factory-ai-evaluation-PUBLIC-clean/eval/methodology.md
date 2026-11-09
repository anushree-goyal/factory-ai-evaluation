# Methodology: what was compared

## Scope and design

- Six issues from Khiem's Node.js Todo API benchmark, replayed on a separate Factory experiment repository.
- Factory evaluation: 8–9 November 2026, Europe/Berlin. **Factory Droid** (not a documented Factory Missions multi-agent run). Evaluated model reported by experimenter: `nvidia/nemotron-3-ultra-550b-a55b:free` through OpenRouter; logs show `nvidia/nemotron-3-ultra-550b-a55b-20260604` with `variant=free`.
- General task prompt: `Fix GitHub issue #N in this repo. Open a pull request that resolves it.` Specific session prompts and continuations sometimes varied or were paraphrased.
- Warp reference: Khiem's **default managed Warp Factory** with model `auto`, reviewed on 26 October 2026. #3 and #4 shared one Warp chat and PR; this weakens per-issue independence.
- Original [runbook](https://github.com/HawKhiem/warp-factory-sandbox/blob/main/eval/RUNBOOK.md), [answer key](https://github.com/HawKhiem/warp-factory-sandbox/blob/main/eval/answer-key.md), [scorecard](https://github.com/HawKhiem/warp-factory-sandbox/blob/main/eval/scorecard.csv).

## Definitions of measured outcomes

- **Rubric-aligned initial handling:** the first substantive agent response respects task-specific acceptance criteria and appropriate stop/clarification behavior. A question on underspecified issue #6 counts as aligned initial judgment, even though the answer requires a person.
- **Eventual rubric-aligned outcome:** the final code or non-code resolution satisfies the intended benchmark, counting a revised solution after corrective feedback but marking that feedback separately.
- **Corrective feedback:** human input pointing out a flaw and requesting a changed implementation; *distinct* from answering a task-clarification question.
- **Accepted/merged:** experimenter-reported for Factory where unavailable independently; not equivalent to having CI logs or proof of correctness.
- **Provisional:** a satisfactory reported outcome based on provided patches/notes but missing full independent CI or original diff.

## Usage measurement and exclusions

- #1–#4: 96 of 104 shared-key OpenRouter request rows attributed using fixed UTC windows checked against Factory session-history timestamps. **8 shared-key requests (66,822 tokens) are left unassigned.** Some may relate to #5, so complete all-attempt costs may be higher.
- #5: **35** dedicated-key rows, **744,956** total tokens. Request bursts of **367,351** and **377,605** tokens are time separated but *not provably* pre/post human-feedback cost segments.
- #6: only a separate **842,382-token aggregate** attributed by the experimenter to the successful 08:45–08:49 CET run. Its screenshot reports **39** API requests and **$0.00**. The separate earlier aborted run (**318,507** tokens, 19 requests) is excluded and documented, not silently added to the selected-run total.
- OpenRouter token counts **include cached input inside input**. Do not add cached tokens a second time. Some failures/cancelled requests with nonzero recorded usage are included if inside the selected window.
- Total selected Factory tokens: **3,017,684**. The figure is provider-recorded request usage, **not** distinct codebase tokens or all possible exploration attempts.

## Timing and cost caveats

Factory duration values are sums of **logged agent session active seconds**, not end-to-end user prompt-to-merged-PR times. In particular, #3 was resumed, and #5's later requests fall outside the nominal session metadata. Warp's published `minutes_to_pr` has a different definition and is partially missing/shared across tasks. There is no valid cross-provider throughput ratio.

Factory dollar figures reflect **$0.00 captured OpenRouter API charges** using the free-model route; they exclude subscriptions, runner compute, human review and any other costs. Warp reported **$11.26** across its benchmark under its own metering. Equal cost scope/model price was **not** established.

## Experimental weaknesses

Single run per issue/provider; small Node.js project; non-identical models, workflows, tool budgets and prompts; Factory private PRs not independently fetched in this review; Factory #1 diff missing; full Factory tests not replayed; #6's successful token aggregate lacks per-request timestamps; no Warp token ledger. Treat these observations as a case study, not a statistical product ranking.
