# Factory AI Droid vs. Warp Factories
## Evidence-based comparison on CSEE's six-issue software-factory benchmark

**CSEE Code Factory — technical evaluation**  
**Prepared:** 9 November 2026  
**Experiment windows:** Warp, 26 October 2026; Factory AI, 8–9 November 2026 (Europe/Berlin)  
**Scope:** Six issues in Khiem Nguyen's Node.js Todo API sandbox, evaluated from the supplied Factory data package and the original public Warp benchmark.  
**Status:** Comparative case study, **not** a controlled provider-level performance ranking.

> **Executive conclusion.** Both systems demonstrated useful issue-to-PR automation. The meaningful difference in this small sample is *judgment and validation*, not the ability to generate patches. Factory AI Droid produced six PRs, but its first Issue #5 patch was incorrect and needed human correction; on deliberately vague Issue #6 it made an unbenchmarked optimization instead of first establishing a measurable performance problem. Warp's published six-issue assessment records acceptable outcomes for all tasks, notably asking for clarification and measuring before changing code on #6. This favors the *observed Warp workflow* under this rubric, but does **not** establish that the Warp product or its underlying models are inherently more capable than Factory AI: configurations, models, orchestration, task grouping, and cost bases differed.

## 1. Key results

| Metric | Factory AI **Droid** | Warp **Factories** | Interpretation |
|---|---|---|---|
| Benchmark issues | 6 | 6 | Same task definitions and starting sandbox concept; different runs and workflows |
| Rubric-aligned initial handling | **4/6** (#1–4) | **6/6** (#1–5 implemented; #6 appropriately paused) | On #5 Factory's first PR was defective; on #6 its response was contrary to the benchmark's expected clarification-first behavior |
| Final rubric-aligned issue outcomes | **5/6, provisional** (#1–5 after #5 revision) | **6/6, author-verified** | Factory #6 is not a rubric pass merely because a PR was produced; Factory test/merge verification is less complete |
| Corrective human feedback | **1 round** (#5) | **0 recorded** | Separate from answering a clarification question |
| Clarification to complete #6 | **0 questions observed** | **1 user answer required** | Warp's question was appropriate task refinement, not failure to operate autonomously |
| PRs created | **6** | **4** for #1–5; none for #6 | Warp grouped #3 and #4 into one PR. PR count is not a success metric |
| Tests / validation | Variable; tests added for #2–6, but gaps remain | Reported red/green regression verification; 40 repeated suite runs for #5 | Warp's evaluation had stronger published *independent validation evidence* |
| Factory token use | **3,017,684** recorded tokens in selected runs | **Not disclosed per issue** | No valid cross-provider token-efficiency ratio |
| Recorded API/platform cost | **$0.00 OpenRouter API spend** for selected free-model calls | **$11.26 charged** in Khiem's experiment | Different charging boundaries and model choices; no end-to-end cost winner |
| Duration evidence | Logged *active sessions*; not prompt-to-PR elapsed time | Partial prompt-to-PR figures; some tasks grouped/untimed | Timing columns must not be compared as equivalent measures |

**Scoring definitions matter.** “Rubric-aligned initial handling” assesses the first substantive response to the issue, including the decision to *stop and ask* on an underspecified request. It does **not** mean every task was fully completed without a human: Warp #6 needed one answer before the benchmark and recommendation. “Final rubric-aligned issue outcomes” includes Factory's corrected #5, but excludes its speculative #6 patch. The Factory figures are based on provided patches, experimenter confirmations, and code inspection—not independent re-execution of every full PR and CI pipeline. Warp results use Khiem's published review and scorecard, not a fresh independent replay. [W1–W4]

## 2. Experimental design and comparability

### Benchmark

The reference is Khiem Nguyen's public [`warp-factory-sandbox`](https://github.com/HawKhiem/warp-factory-sandbox), whose `baseline` tag is intended to seed a clean private copy for each provider. Its six issues cover documentation scope, an off-by-one bug, Unicode/whitespace handling, a filtering feature, a flaky timestamp test, and a deliberately underspecified performance request. The common task prompt is:

> Fix GitHub issue #N in this repo. Open a pull request that resolves it.

The [runbook](https://github.com/HawKhiem/warp-factory-sandbox/blob/main/eval/RUNBOOK.md) calls for independent issue runs, review before merge, tests that **pass with the patch and fail on old source**, and 40 full-suite repetitions on the flaky-test task. It also prescribes a clarification response for #6 if the system asks. [W2–W4]

### What was actually tested

- **Warp:** Khiem's **default managed Warp Factory**, with a foreman and specialist triage/spec/implementation/review workflow, model recorded as **`auto`**. The published scorecard dates the evaluation **26 October 2026**. Issues **#3 and #4 were submitted within one chat and combined into one PR**, which weakens per-issue independence and makes their time/cost inseparable. [W1–W3]
- **Factory AI:** A **Factory Droid** handling issue prompts and GitHub PRs, using an experimenter-reported **NVIDIA Nemotron 3 Ultra 550B A55B** through OpenRouter's free variant (`nvidia/nemotron-3-ultra-550b-a55b:free`). Sessions are dated **8–9 November 2026**. This was **not a demonstrated Factory Missions** multi-Droid orchestration run. Some sessions were resumed; failed/no-op or abandoned sessions were excluded under documented rules. [F1–F3]
- **Control quality:** The six *tasks* are comparable; the **model, orchestration topology, experimental date, intervention timing, number of chats, measurement instrumentation and pricing** are not held constant. Warp's author manually checked its PRs; Factory's supplied archive contains diffs for PRs #8–12 and experimenter-reported review/test outcomes, but **no supplied patch for #7**, and no complete CI transcripts or independently accessible private Factory GitHub history. Therefore this is an observational *workflow-and-task-outcome comparison*, not a clean A/B experiment.

Factory's product also offers a separate multi-agent **Missions** capability; its presence in the product is not evidence it operated in these six runs. [V1]

## 3. Reproducibility and data audit

The attached ZIP was extracted and checked before interpreting outcomes. The supplied standard-library script, `rebuild_factory_usage.py`, successfully regenerated the issue-level usage summaries. Independently checking the package's **13 source-manifest entries** found **no SHA-256 or byte-size mismatches**. The rebuilt issue totals summed to **3,017,684 request tokens**. [F1–F3]

| Evidence | Verification performed | Confidence / remaining limitation |
|---|---|---|
| Factory usage #1–4 | Rebuilt request counts and token totals from timestamped shared-key OpenRouter records | **High confidence in recorded counts within selected windows**; session association is inferred from UTC clustering, because provider requests have no Factory session ID |
| Factory usage #5 | Matched **35 dedicated-key requests** to **744,956 tokens**; identified two temporal bursts | **High for dedicated-key total**, not for complete all-key activity or the precise first-attempt/revision split |
| Factory usage #6 | Verified separate **842,382-token aggregate**; screenshot shows **39 requests** and **$0.00** | **Aggregate verified; run attribution experimenter-confirmed**, not independently timestamp-linked; no input/output/cache detail |
| Excluded activity | Audited **8 unassigned shared-key requests / 66,822 tokens** and **19 aborted #6 requests / 318,507 tokens** | Excluded from the selected six-run numerator; cannot silently reassign to issues |
| Factory code correctness | Inspected patches #8–12 including both #5 revisions; reproduced #5's faulty timestamp logic in an isolated Node.js check | Strong evidence for the specific initial #5 defect; **not equivalent to rerunning the complete Factory repository or its CI** |
| Warp results | Cross-checked public README, `eval/scorecard.csv`, `eval/RUNBOOK.md`, answer key, and public #6 benchmark comment | Publicly traceable **author-reported** review and measurements; not independently replayed for this report |

**Issue #5 reproducible failure.** In the first Factory patch, when a new ISO timestamp was not later than the previous one, the code incremented the fractional-millisecond substring of the *current* timestamp. Under multiple creations in the same millisecond, successive calls could repeat the same adjusted string (e.g. `.123`, `.124`, `.124`). At `.999`, textual increment could yield `.1000Z`, which is not the canonical three-digit millisecond representation returned by `Date#toISOString`. An isolated execution of the patch's algorithm reproduced both observations. The revised patch instead stores epoch milliseconds and uses `max(nowMs, lastTimestampMs + 1)`, which resolves the demonstrated repeated-time and millisecond-boundary cases. The added tests, however, do not use a deterministic frozen clock. [F4]

### Attribution rules that change the answer

1. For #1–4, **96 of 104** shared-key requests were assigned by documented time windows; the other **8 / 66,822 tokens** were not allocated. A request overlapping the early #5 window may belong to #5, so its full experiment cost could be undercounted.
2. #5's dedicated key separates into **burst A: 367,351 tokens / 21 requests** and **burst B: 377,605 / 14**. These plausibly correspond to first attempt and later revision, but the exact feedback boundary was not logged: **do not label these as confirmed phase costs**.
3. The earlier #6 attempt (**318,507 tokens / 19 requests**) was aborted and explicitly excluded. The evaluated #6 row is **only the later successful run's 842,382-token export**; adding both would conflate distinct attempt scopes. The later aggregate is linked to the 08:45–08:49 CET run by experimenter confirmation rather than per-request timestamps.
4. #3's two Nemotron sessions are counted; two abandoned Qwen sessions are excluded. The main total is therefore a **selected-run model-usage total**, not every failed setup or exploratory action in the study.

## 4. Issue-by-issue technical assessment

| Issue / expected behavior | Factory AI Droid | Warp Factories | Comparative verdict |
|---|---|---|---|
| **#1 Documentation:** README accurately mirrors local setup; stay in scope | PR #7 reportedly updated instructions; 9/9 tests passed after rerun; lint reported passing; no extra feedback. **Patch not provided.** | PR #7 changed README only; correctly noted pre-existing flaky CI but left it out of scope. | **Both provisionally pass.** Warp's evidence is publicly inspectable; Factory patch cannot be independently checked here. |
| **#2 Pagination:** fix page-one offset, add bug-catching tests | PR #8 changed `page * size` to `(page - 1) * size`; added unit regressions for pages 1 and 2. | PR #8 fixed same root cause and added HTTP-level regressions, including defaults and later pages; 6 new test cases reportedly failed against old code. | **Both pass.** Warp demonstrated broader contract-level test coverage. |
| **#3 Slugify:** normalize accents and repeated whitespace, avoid hard-coded examples | PR #9 used `NFD`, stripped combining accents and collapsed `\s+`; added accented and whitespace examples. Does **not** collapse existing repeated hyphens or trim newly exposed edge hyphens. | Combined PR #9 used broader normalization and test cases, including decomposed accents / additional whitespace. It still dropped some non-decomposing characters (`ø`, `ß`, `æ`), a gap its reviewer missed. | **Both pass core request, with edge-case gaps.** Warp's published tests are broader; neither demonstrates comprehensive internationalization. |
| **#4 Status filter:** apply before pagination; accurate filtered `total`; reject invalid values; docs and tests | PR #10 correctly filters before `paginate`, returns 400 on invalid `done`, updates README. Tests check basic true/false and one invalid value, but **not filtered pagination / filtered totals across pages**. Two tests share state established by a preceding test. | Combined PR #9 tested interleaved completed/incomplete todos and page-two filtered totals; tested several invalid values. Published red/green validation. | **Both implementations match the main specification**, but Factory's tests are notably weaker and order-dependent. |
| **#5 Flaky timestamps:** find cause; avoid retries/deleting test | **First PR #11 fails** under same-millisecond repeats and rollover. **After 1 human feedback round**, PR #11-v2 uses monotonic epoch-ms, adds three tests, and was reported merged. Tests do not freeze time and no 40-run evidence was supplied. | PR #10 found millisecond ties, removed randomness, used deterministic clock mocking and monotonic timestamps. Khiem reported 40/40 full suite runs and red/green regression checks. Changes timestamp behavior by allowing future drift, without asking. | **Warp first-pass pass; Factory eventual pass after intervention.** Both make a defensible but nontrivial product-behavior choice. |
| **#6 Vague “make API faster”:** ask for measurable goal; don't speculate | PR #12 added store pagination and an ID map, with functional tests, **0 clarification questions**, **no before/after performance numbers**. May reduce avoidable copying and lookups, but no demonstrated user problem or measured gain. | Foreman asked for scope. After the requested user answer, ran an HTTP benchmark, commented results on the issue, and recommended closing without a code PR. | **Warp passes the intended ambiguity/judgment test; Factory fails that rubric.** This is a failure of problem framing/measurement, **not proof the Factory patch is functionally incorrect**. |

The answer key explicitly treats a speculative optimization PR for #6 as a red flag. It similarly values regression tests that fail on the baseline rather than merely pass after a patch. [W3–W4]

### The most discriminating issue: #6

The public original issue says only: “Users say the API feels slow. Please make it faster.” Warp requested an endpoint, workload or latency goal, then measured instead of inventing an objective. Its public follow-up records **108 benchmark runs, 1,519,104 measured HTTP requests, 54.017 seconds of measured traffic**, across dataset sizes **100 / 1,000 / 10,000**, client concurrency **1 / 4**, and list, filtered list, ID lookup and CRUD workloads. In the reported 10,000-todo / four-client condition, the table's largest median-of-run p95 is **1.193 ms** for the entire CRUD cycle. It reported no demonstrated bottleneck **under those local loopback test conditions**, not a universal production guarantee. [W5]

Factory #12's implementation has a *plausible mechanism*: `listPaginated()` slices only the requested page rather than copying the whole array, and a `Map` can improve average-case ID retrieval from linear search to constant-time lookup at the expense of extra memory and maintenance. However, `done` filtering still scans an array; deletion still requires an array search/splice; and the test named “does not copy full array” only validates returned items—it **does not instrument copying, memory, latency or throughput**. The patch therefore supports **a proposed optimization**, not a demonstrated speedup. The correct outcome under this benchmark was to clarify or measure first.

## 5. Autonomy, intervention and quality gates

A useful comparison requires separating **task completion**, **repair after feedback**, and **appropriate deferral**:

| Dimension | Factory observed | Warp observed |
|---|---|---|
| First substantive response satisfying the benchmark rubric | #1–4 = **4/6** | #1–5 solutions + #6 clarification-first response = **6/6** |
| Completion with **no additional user input** and rubric-aligned outcome | #1–4 = **4/6** | #1–5 = **5/6**; #6 asked a question |
| Completion following **corrective feedback** | #5 revised successfully after **one** explicit intervention | **No corrective user intervention** recorded; internal reviewer requested changes on some Warp PRs |
| Appropriate clarification / justified no-op | Not observed on #6 | Observed on #6; user answered once, then no PR |
| Final accepted issue outcomes under benchmark's rubric | **5/6 provisional** | **6/6 author-reported / reviewed** |

This avoids calling Warp's #6 “fully autonomous”: it correctly involved the person in deciding the goal. Conversely, counting Factory's #5 as a first-pass win because its *revised* PR was eventually accepted would overstate first-attempt reliability.

**Independent test quality differs.** Warp's benchmark documentation says its new regressions were executed with and without the fix, with 40 repeated complete suite runs for #5. The Factory archive includes new tests and reported pass messages but not equivalently comprehensive red/green or 40-run evidence. Factory #2's unit tests and #3's normalization cases are meaningful; #4 lacks a critical filter-before-pagination regression, #5 lacks deterministic time control, and #6 lacks a performance measurement. These are observed *evidence gaps*, not a claim that every Factory test is useless. [W1–W3, F4]

## 6. Time, token usage and costs

### Factory AI: audited selected-run consumption

| Issue | Total tokens (input + output) | Requests | Logged Factory active time* | Recorded OpenRouter API spend |
|---|---:|---:|---:|---:|
| #1 Docs | 280,995 | 20 | 50.6 s | $0.00 |
| #2 Pagination | 284,886 | 20 | 62.2 s | $0.00 |
| #3 Slugify | 354,196 | 27 | 163.1 s in two sessions | $0.00 |
| #4 Filter | 510,269 | 29 | 148.2 s | $0.00 |
| #5 Timestamps, initial + revision | 744,956 | 35 | 243.7 s, **incomplete** for full revision | $0.00 |
| #6 Optimization, **successful run only** | 842,382 | 39† | 213.0 s | $0.00† |
| **Selected-run total** | **3,017,684** | **170‡** | **880.8 s summed** | **$0.00 recorded** |

\* These are *Factory session-duration fields*, **not** prompt-to-PR or human elapsed time. They exclude gaps, and #5's revision timing is incomplete. The 880.8 s figure is only the arithmetic sum of logged fields, **not a valid six-task wall-clock completion time**.  
† #6 request count and dollar amount are visible on a key-filtered dashboard; aggregate tokens come from its separate CSV. Its per-request token split is unavailable.  
‡ Of 170, **131 requests** (#1–5) have counted individual request records; #6 contributes **39 screenshot-reported requests**. [F1–F3]

For #1–5 only: **2,153,030 input tokens** (including **1,753,600 cached prompt tokens**, 81.4% of input), **22,272 output tokens**, and **2,175,302 total tokens**. Cached input is a **subset**, not a further addition. No input/output/cache breakdown is available for #6. These are the sum of token accounting across API requests, not unique source-code tokens or a measure of reasoning quality.

### Warp: published time and charge evidence

| Issue(s) | Published elapsed-time evidence | Published charge |
|---|---|---:|
| #1 | 1.2 min to PR | ≈ $1.67* |
| #2 | ≈ 3 min to PR | ≈ $1.67* |
| #3 + #4 | ≈ 9 min **shared** across one chat / PR | **$1.87 combined** |
| #5 | Exact minutes to PR **not recorded** in scorecard | $3.66 |
| #6 | **No PR**; duration to final issue comment not reported as `minutes_to_pr` | $2.39 |
| **Total** | **No comparable six-task elapsed-time total** | **$11.26** |

\* #1 and #2 totalled **$3.34**; the ≈$1.67 figures are **averaged estimates**, not separately metered costs. Similarly, splitting the $1.87 for #3/#4 to about $0.94 per issue would be an **allocation**, not two measured issue costs. [W1–W2]

### What these numbers do—and do not—show

- **Exact comparison permitted:** Warp's trial had **$11.26 in reported charges**, while the selected Factory **OpenRouter free-model API requests recorded $0.00**. This is a description of two billing records.
- **Not established:** Factory's full economic cost is lower, or Warp's token efficiency is worse. The Factory accounting excludes subscription/plan, local or cloud compute, user review time, and any costs outside the captured OpenRouter calls; free requests have underlying compute costs and rate limits. Warp's charge includes its own platform/inference accounting and a different auto-routed configuration.
- **Not established:** Factory is faster. Factory's seconds are reported **active session durations**, whereas Warp's available minutes refer to **prompt-to-PR time**, and #3/#4 share an elapsed-time figure. In Factory #3, a significant gap separates initial work and continuation.
- **Not established:** A token ratio between providers. Warp did **not** publish task-specific token counts in the original scorecard.
- **Sensitivity / selection:** The stated 3,017,684 tokens **exclude** 318,507 tokens from aborted #6 and 66,822 unassigned shared-key tokens. They are retained as a separate audit trail, not silently attributed to selected successes. An end-to-end *all-attempts* assessment would need a broader, consistently logged denominator across both providers.

## 7. Implications for CSEE's Code Factory architecture

The benchmark suggests prioritizing **workflow control and evidence of correctness** over producing more code or PRs. A viable design is:

```text
Issue / request
      ↓
TRIAGE + REFINE  ─── underspecified? ──→ ask a focused question / define a benchmark
      ↓                                     └─→ evidence supports no change → close/recommend
Acceptance criteria + constraints
      ↓
IMPLEMENT in isolated workspace
      ↓
VALIDATE: unit/integration + baseline-red / patched-green + targeted stress tests
      ↓
INDEPENDENT REVIEW: spec compliance, diff scope, edge cases, test quality
      ↓
Gate result ── fail → bounded retry with specific feedback → revalidate
      ↓
Human PR approval / merge
      ↓
Record outcome, duration, tokens, cost, interventions, and later regressions
```

**Priority 1 — A genuine Refine gate.** Before implementation, classify whether the request supplies (a) a verifiable defect or feature, (b) acceptance criteria, and (c) sufficient context. For optimization or reliability claims, require a workload, baseline and measurable target—or explicitly choose a bounded diagnostic run. A *correct no-op* must count as success when justified. The contrast on #6 is the clearest argument for this gate.

**Priority 2 — Test the tests.** Require regression checks against the prior source state for bug fixes, not just “tests green” on the new branch. For #4, generate cross-page filtered-total cases; for #5, freeze the clock and test repeated timestamps and boundaries; for #6, require a before/after benchmark on representative workloads. Save CI outputs and randomized/repeated runs when nondeterminism is the issue.

**Priority 3 — Independent review with a bounded repair loop.** Issue #5 illustrates why review is not cosmetic: the first patch looked plausible but violated the required invariant. A reviewer should identify counterexamples, reject inadequate tests, and return *actionable* feedback. Cap repair attempts and escalate to a human when confidence remains low. Warp also missed #3 Unicode edge cases: reviewer agents themselves need evaluations.

**Priority 4 — Explicit stop / no-op / PR decisions.** Do not force the pipeline to open a PR for every prompt. Supported end states should include `clarification_needed`, `benchmark_reported`, `no_change_recommended`, `pr_ready`, `retry_required`, and `human_review_required`. Measure **accepted task resolution**, not raw PR throughput.

**Priority 5 — Cost, latency and provenance observability.** Capture a per-task trace across agent and provider boundaries: versioned prompt, baseline commit, model/harness version, time to final outcome, active agent time, input/output/cached tokens, actual billed model/runner cost, attempts, feedback rounds, test results and PR decision. Set maximum request/token budgets and termination conditions for open-ended investigations. This closes the attribution issues seen in #3, #5 and #6.

**Priority 6 — Modular agents rather than premature orchestration complexity.** A minimal prototype can implement Triage/Refine → Implement → Validate/Review as **separable stages** with clear artifacts and gates. Parallel specialist agents may be worthwhile later, but this benchmark does not isolate the marginal benefit of multi-agent orchestration from model choice or run configuration. Warp provides one evaluated managed orchestration example; Factory's separate Missions architecture still needs a like-for-like trial. [V1–V3]

## 8. Recommended next evaluation

To turn this indicative case study into a stronger Code Factory architecture decision:

1. **Freeze a versioned task set and rubric.** Start every trial at the same `baseline` commit. Publish unambiguous expected behavior, including what counts as justified refusal/no-op; score task outcomes independently of whether a PR was opened.
2. **Repeat each task** (preferably at least three times per configuration) and report each trial, not just a best or selected successful one. Capture failures from provider errors, rate limits, abandoned runs and repair retries using both *attempt-level* and *task-level* denominators.
3. **Test comparable configurations.** Run Factory Droid, Factory Missions, and Warp using as similar a model/model budget and prompt as available. Treat native/default configurations as a **separate product-experience track**, not as a controlled architecture comparison.
4. **Enforce identical validation.** Review every diff blind; run standard tests, baseline red/green checks, 40-run flaky tests where appropriate, and a documented performance protocol for #6. Label correctness, design judgment, scope discipline, test adequacy and intervention separately.
5. **Instrument real costs and elapsed time.** Record task wall time, active agent time, model and cache token types, compute/platform charges, subscription allocations (where relevant), and human review minutes. Normalize neither money nor time when source boundaries differ.
6. **Expand beyond the toy repo.** Add ambiguous feature requests, security-sensitive changes, multi-file refactors, dependency updates, and a larger unfamiliar repository. Review defects *after merge* as well as PR acceptance.

A small recommended reporting schema per `(provider, config, issue, trial)` is: `initial_rubric_pass`, `final_rubric_pass`, `needs_clarification`, `corrective_feedback_rounds`, `pr_created`, `tests_pass_on_patch`, `regression_tests_fail_on_baseline`, `review_scope_pass`, `elapsed_seconds`, `agent_active_seconds`, `input_tokens`, `output_tokens`, `cached_input_tokens`, `recorded_cost_usd`, `cost_scope`, and `evidence_link`.

## 9. Limitations and defensible conclusion

**Limitations.** Six deliberately small tasks in one Node.js sandbox; one principal run per issue/provider; different dates, models and agent topologies; Warp #3/#4 combined; Factory #3 continued after a gap; incomplete or differently defined timing; Factory's private PRs not independently fetched; no Factory #1 patch; no full Factory CI replay; token attribution by time windows; user-confirmed rather than timestamp-verified #6 export; no Warp token ledger; free-model rate limits; pricing boundaries not equal; no direct proof of large-codebase reliability, long-term maintenance quality, general statistical advantage, or return on investment.

**Conclusion.** On this specific rubric, **Warp showed stronger observed specification handling and documented validation**, especially on the ambiguous performance request and the flaky test. **Factory AI Droid showed meaningful autonomous implementation ability**, including acceptable patches for ordinary tasks and a successful human-guided repair on the hardest correctness issue, at **zero recorded OpenRouter API charge** using the free model. Yet #5 shows the cost of an undetected first-attempt defect, and #6 shows why a plausible optimization is not equivalent to resolving a user problem. For CSEE, the key architectural lesson is to build a factory that can **refine, measure, validate, review, retry within limits, and decline unnecessary changes**—then evaluate it on reproducible task outcomes rather than PR counts or incomparable billing figures.

---

## References and evidence provenance

### Public Warp and vendor sources

- **[W1]** Khiem Nguyen, [Warp Factories evaluation: README and original report](https://github.com/HawKhiem/warp-factory-sandbox), 26 October 2026.
- **[W2]** Khiem Nguyen, [original six-issue scorecard (`eval/scorecard.csv`)](https://github.com/HawKhiem/warp-factory-sandbox/blob/main/eval/scorecard.csv).
- **[W3]** Khiem Nguyen, [benchmark runbook (`eval/RUNBOOK.md`)](https://github.com/HawKhiem/warp-factory-sandbox/blob/main/eval/RUNBOOK.md).
- **[W4]** Khiem Nguyen, [benchmark answer key (`eval/answer-key.md`)](https://github.com/HawKhiem/warp-factory-sandbox/blob/main/eval/answer-key.md).
- **[W5]** [Original issue #6 and Warp's detailed measurement comment](https://github.com/HawKhiem/warp-factory-sandbox/issues/6), 26 October 2026.
- **[V1]** Factory AI, [Missions: multi-agent orchestration](https://factory.ai/product/missions).
- **[V2]** Warp, [Introducing Warp Factories](https://www.warp.dev/blog/open-infrastructure-for-building-a-software-factory), 18 August 2026.
- **[V3]** Warp, [Factory benchmarks documentation](https://docs.warp.dev/factories/benchmarks/).

### Internal Factory evidence (retained separately; do **not** publish raw exports)

- **[F1]** Supplied Factory evidence ZIP: `README.md`, `comparison-prompt.md`, `factory-evaluation-context.md`, `data-quality-notes.md`, `source-manifest.csv`.
- **[F2]** `derived-data/factory-usage-by-issue.csv`, `factory-session-attribution.csv`, `issue5-usage-by-burst.csv`, `excluded-and-unassigned-requests.csv`, with reproducibility script `rebuild_factory_usage.py`.
- **[F3]** Source OpenRouter request/aggregate exports, Factory session-history CSV, experiment log and key-filtered #6 dashboard screenshot. **Not reproduced here** because they include private experiment metadata.
- **[F4]** Supplied Factory patches: `factory-pr-8.patch`, `factory-pr-9.patch`, `factory-pr-10.patch`, `factory-pr-11.patch`, `factory-pr-11-v2.patch`, `factory-pr-12.patch`. PR #7 patch absent.

**Evidence classification:** Counts explicitly sourced to CSVs or screenshot are *recorded measurements*; assignment of shared-key usage to sessions and the successful #6 export to its time window are *attributions*; PR merge/CI claims unavailable for independent replay are *experimenter reports*; code properties derived from patch inspection or isolated reproductions are *analyst findings*; the proposed pipeline is an *architectural recommendation*.
