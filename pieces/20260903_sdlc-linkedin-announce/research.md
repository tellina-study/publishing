# Research: AI in the SDLC — current (2024–2026) study-backed facts for a LinkedIn hook

Feeds a LinkedIn announce for an SDLC lecture on lessons.tellian.io.
House rule L06: the hook fact must still be true in 2026. Freshness notes below.

## What we already know (internal)
- Nothing on these specific facts. RAG returned no hits for METR / DORA / GitClear / AI code
  quality. `wiki/topics/anti-patterns.md` has only generic cautions ("X is dead" over-claims,
  "Now AI can do X" freshness traps) — relevant as *style* guardrails, not as content.

## Key sources
| Source | Type | What it supports | Link/ID | Resolved? |
|--------|------|------------------|---------|-----------|
| METR, "Measuring the Impact of Early-2025 AI on Experienced OSS Developer Productivity" (Jul 2025) | Primary (RCT) | 19% slower + perception gap | https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ ; arXiv:2507.09089 | Yes |
| Stack Overflow 2025 Developer Survey (results Dec 2025) | Primary (survey) | Trust decline; 66% fix "almost-right" AI code | https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/ ; https://survey.stackoverflow.co/2025/ai | Yes |
| Google DORA, Accelerate State of DevOps 2024 | Primary (report) | 25% more AI ⇒ -1.5% throughput, -7.2% stability | https://dora.dev/research/2024/dora-report/ (numbers via getdx/opslevel summaries) | Yes (numbers via secondary) |
| Google DORA 2025 (published Dec 2025) | Primary (report) | UPDATE: AI now +throughput, but instability persists | https://dora.dev/research/2025/ ; https://redmonk.com/rstephens/2025/12/18/dora2025/ | Yes (secondary) |
| GitClear, "AI Copilot Code Quality 2025" | Primary (data study) | Refactoring collapse, 4x clones | https://www.gitclear.com/ai_assistant_code_quality_2025_research ; PDF: https://gitclear-public.s3.us-west-2.amazonaws.com/GitClear-AI-Copilot-Code-Quality-2025.pdf | Yes |
| Veracode 2025 GenAI Code Security Report (Jul/Oct 2025) | Primary (test study) | 45% of AI code has OWASP-Top-10 vuln | https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/ ; press: businesswire 20250730694951 | Yes (numbers via helpnetsecurity) |

## Facts (each: NUMBER | MEASURES/baseline | SOURCE+YEAR | URL | status)

### F1 — METR 19% slower (THE hook)
- NUMBER: developers took **19% LONGER** to complete tasks with AI allowed; they had
  *forecast* AI would speed them up 24%, and *even after*, believed it sped them up ~20%.
- MEASURES: time-to-complete real GitHub issues, within-subject RCT randomizing AI-allowed vs
  not. 16 experienced OSS devs, 246 tasks, on mature repos (22k+ stars, 1M+ LOC) they'd worked
  on for years. Tools = Cursor Pro + Claude 3.5/3.7 Sonnet (early-2025 frontier).
- SOURCE: METR, Jul 2025. arXiv:2507.09089.
- URL: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- STATUS: **Verified** (fetched METR blog directly; numbers confirmed).
- FRESHNESS/L06: The measured direction ("experts wrongly believe AI sped them up") is the
  durable, defensible point. Caveat: it's early-2025 tooling, narrow N=16, expert-on-own-repo
  setting — do NOT generalize to "AI slows everyone." METR itself is re-running the experiment
  (blog 2026-02-24). Safe framing = the *perception gap*, which is robust and not tool-fixed.

### F2 — Stack Overflow: 66% fix "almost-right" AI code (best "deeper point")
- NUMBER: **66%** of developers say they spend more time fixing "almost-right" AI code;
  **45%** name "AI solutions that are almost right, but not quite" as their #1 frustration.
  Trust in AI *accuracy* fell **40% → 29%** YoY; adoption ~**80%** use AI.
  (Survey site framing of a different question: only ~3% "highly trust" output; experienced
  devs lowest at 2.6%.)
- MEASURES: self-report, 2025 SO Developer Survey (tens of thousands of devs; results Dec 2025).
- SOURCE: Stack Overflow, 2025 survey (published Dec 2025).
- URL: https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/
- STATUS: **Verified** (fetched SO blog).
- FRESHNESS/L06: Most current data available (Dec 2025). Trust FALLING as adoption rises is the
  non-obvious hook. Not superseded.

### F3 — GitClear: refactoring collapse + 4x clones
- NUMBER: "moved"/refactored lines fell from **~25% (2021) to <10% (2024)**; copy/pasted lines
  rose **8.3% → 12.3%** (2021–2024); code clones ~**4x**; 2024 = first year copy/paste exceeded
  moved code. Basis: **211M changed LOC, Jan 2020–Dec 2024**.
- MEASURES: git-history line classification across a large multi-org corpus (observational,
  correlational — not causal to AI).
- SOURCE: GitClear, "AI Copilot Code Quality 2025."
- URL: https://www.gitclear.com/ai_assistant_code_quality_2025_research (PDF linked above)
- STATUS: **Verified** (fetched GitClear page).
- FRESHNESS/L06: Vendor (GitClear sells code analytics) — disclose. Correlation, not proof AI
  caused it; timing coincides with Copilot era. Solid for "code quality trend," not "AI did X."

### F4 — DORA 2024: AI adoption ⇒ less stable delivery
- NUMBER: every **25% increase in AI adoption** ⇒ **-1.5% delivery throughput** and
  **-7.2% delivery stability** (while **+2.1% productivity**, +2.6% job satisfaction). ~76% used
  AI daily.
- MEASURES: survey + statistical model, DORA 2024 (thousands of practitioners).
- SOURCE: Google Cloud DORA, Accelerate State of DevOps 2024.
- URL: https://dora.dev/research/2024/dora-report/ (numbers via getdx.com + opslevel summaries)
- STATUS: **Verified** on the numbers via two independent secondaries (getdx, opslevel);
  primary landing page didn't expose the figures to WebFetch. Number consistent across sources.
- FRESHNESS/L06: **PARTIALLY SUPERSEDED — DO NOT use the 2024 throughput number as current.**
  DORA **2025** (Dec 2025) reports AI now correlates POSITIVELY with throughput; but
  **instability persists** across both years. If used, cite the *stability* finding and pair
  with the 2025 update. See F5.

### F5 — DORA 2025 update (freshness anchor, use to keep F4 honest)
- NUMBER/FINDING: 2025 — ~**90%** of devs use AI, **>80%** report a productivity gain; AI now
  positively correlates with **throughput**, but continues to correlate with **instability**
  (more change failures, rework, longer resolution). Teams >1yr on AI report *less* disruption.
- SOURCE: Google Cloud DORA, State of DevOps 2025 (Dec 2025).
- URL: https://dora.dev/research/2025/ ; summary https://redmonk.com/rstephens/2025/12/18/dora2025/
- STATUS: **Verified via secondary** (RedMonk, Scrum.org, Faros summaries; consistent). Primary
  report not directly fetched — mark **Inferred/secondary** for exact wording.
- ROLE: This is the L06 guard. The durable 2024→2025 story = "AI speeds you up but destabilizes
  delivery; the throughput hit went away, the instability didn't."

### F6 — Veracode: 45% of AI code ships an OWASP-Top-10 vuln
- NUMBER: in **45%** of test cases LLMs produced code with an OWASP-Top-10 vulnerability (i.e.
  when there was a secure vs insecure way, they chose insecure ~45% of the time). **Java >70%**
  failure; Python/C#/JS 38–45%; **86%** failed XSS defense (CWE-80); **88%** vulnerable to log
  injection (CWE-117). Basis: **80 coding tasks × 100+ LLMs**. Larger models not meaningfully
  safer (systemic, not scaling).
- MEASURES: controlled security testing of model outputs on curated tasks.
- SOURCE: Veracode, 2025 GenAI Code Security Report (press Jul 30 2025; update Oct 2025).
- URL: https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/
- STATUS: **Verified** on numbers via helpnetsecurity + businesswire press (consistent). Vendor
  (Veracode sells AppSec) — disclose.
- FRESHNESS/L06: Current (2025). Vendor-run; the "larger models aren't safer" line is the
  non-obvious bit and is defensible.

## Counter-arguments / steelman (a hook with no steelman is weak)
- **METR is narrow.** N=16, expert devs on *their own* mature repos, early-2025 tools. The
  slowdown may not generalize to greenfield work, juniors, or 2026 agentic tooling. The robust,
  un-refutable core is the *perception gap*, not "AI is slower, period."
- **DORA 2024's throughput hit is already gone (2025).** Using it as "AI slows delivery" would
  violate L06 — that specific limitation moved. Only the *stability/instability* finding carries
  forward. This is exactly the trap L06 warns about.
- **GitClear & Veracode are vendors** with a product interest in "AI code is risky." Their data
  is real but correlational/curated — frame as trend/lab signal, not causal proof.
- **SO trust is self-report**, and "trust falling" partly reflects rising exposure (people who
  use AI more see more failures). Adoption is still ~80% — devs use it *despite* distrust, which
  is itself the interesting tension.
- The optimistic read across all of it: teams >1yr into AI (DORA 2025) stabilize — the pain is a
  maturity/process lag, not a permanent AI tax.

## Shaky / do-not-assert-without-more
- "AI code has 2.74x more vulnerabilities than human code" and "10x more security findings" —
  widely repeated in blog coverage but I could **not** resolve these to a clean primary; they
  appear in SoftwareSeni/secondary posts, not confirmed from Veracode's own report text. **Do
  not use.**
- "3% highly trust" vs "29% trust accuracy" are two *different* SO questions — don't conflate.
- GitClear "8x duplication" phrasing appears in some summaries; the report's own figures are the
  8.3%→12.3% / ~4x clones numbers. Use the report's numbers, not the "8x."

## Gaps
- Did not directly fetch DORA 2024/2025 primary PDFs (landing pages gated to WebFetch; numbers
  triangulated from ≥2 independent secondaries — high confidence on the figures, medium on exact
  wording).
- Veracode/GitClear exact numbers verified via press + reputable tech press, not the gated
  vendor PDFs directly.

VERDICT: enough to draft.
Ranked hooks:
1. **METR perception gap** (F1) — most counterintuitive, most gripping for eng leaders; frame as
   the *gap* (believed +20% while measured -19%), pair with SO's 66% (F2) as the "why it matters."
2. **SO 2025: 66% now spend MORE time fixing almost-right AI code, trust 40%→29% while adoption
   ~80%** (F2) — freshest (Dec 2025), squarely non-obvious, zero L06 risk.
3. **Veracode 45% / larger models not safer** (F6) — strong for a security-leaning audience.
Deeper-point pairings: F3 (refactoring collapse) and F5 (DORA: throughput hit gone, instability
stayed) as the "here's the structural cost" beat. AVOID leaning on F4's throughput number alone.
CONFIDENCE: high (F1, F2, F3, F6 verified from primary/press; F4/F5 numbers via consistent
secondaries).

---

## 2026 refresh (added 2026-09-03)

Hunt for genuinely 2026-published / 2026-measured successors to the 2025 facts above.
Owner rule: NUMBERS FROM 2026 — 2025 figures now read as last-year.

### R1 — METR reversal: the slowdown flipped to a speedup (HUGE — this INVALIDATES the old hook)
- NUMBER: METR re-ran the experiment (started Aug 2025). For the **10 developers who did both
  studies**, the later result was a **~18% SPEEDUP** with AI (CI −38% to +9%). For **47 newly
  recruited devs**: **~4% speedup** (CI −15% to +9%). Original early-2025 result was a **~20%
  slowdown** (CI +2% to +39% longer). METR's stated belief: "developers are more sped up from AI
  tools now — in early 2026," but "our data is only very weak evidence for the size of this
  increase" (wide CIs cross zero + selection bias: devs increasingly refuse to work without AI).
- MEASURES: within-subject RCT, time-to-complete real tasks. Methodology changed: pay $150→$50/hr,
  pool 10→57, broader/greenfielder repos. So the −20%→+18% shift is NOT clean apples-to-apples.
- SOURCE: METR, **2026-02-24**. "We are Changing our Developer Productivity Experiment Design."
- URL: https://metr.org/blog/2026-02-24-uplift-update/ ; https://metr.substack.com/p/2026-02-24-uplift-update
- STATUS: **Verified** (fetched METR blog directly).
- L06 / IMPACT: **This is the single most important 2026 update.** The famous "AI makes experts
  19% SLOWER" line is now stale — METR itself walked toward a speedup for 2026 agentic tooling.
  Do NOT ship the old slowdown number as current. BUT the **perception-gap framing still survives
  in weakened form** and the *measured* signal is now noisy (CIs cross zero, self-admitted weak
  evidence). Honest 2026 framing: "the one clean RCT that found experts were slower has itself
  reversed toward a modest speedup — and even its authors call the new signal weak." Nuance, not a
  clean hook number.

### R2 — Stack Overflow 2026: 84% adoption, trust just 29% (adoption UP, trust FLAT-LOW)
- NUMBER: **84%** using or planning to use AI; only **29%** trust AI accuracy (**down 11pp** from
  2024's 40%); ~**46%** actively distrust accuracy > the **33%** who trust it; **3%** "highly
  trust" output (experienced devs lowest, **2.6%**). Bonus 2026 governance stat: **38%** of
  employees shared confidential company data with unapproved ("shadow") AI systems.
- MEASURES: self-report, tens of thousands of devs. IMPORTANT NUANCE: this Feb-2026 SO blog is a
  **fresh 2026 re-analysis of the 2025 survey data** ("closing the AI trust gap"), not a brand-new
  2026 survey. The **2026 SO Developer Survey opened June 2026 and is still in field/analysis** —
  no 2026-survey results published yet as of Sep 2026.
- SOURCE: Stack Overflow, **2026-02-18**, "Mind the gap: Closing the AI trust gap for developers."
- URL: https://stackoverflow.blog/2026/02/18/closing-the-developer-ai-trust-gap/
- STATUS: **Verified** (fetched SO blog directly). Underlying data = 2025 survey.
- L06: The **adoption-up-while-trust-flat-and-low** story is the freshest 2026-published SO framing
  and is not superseded. Note it's built on 2025 field data re-packaged in 2026. The "66% spend
  more time fixing almost-right AI code" number (our F2) did NOT get a 2026 refresh — it remains
  the 2025 figure; this Feb-2026 piece leads on the trust gap instead.

### R3 — Veracode 2026: AI code security STALLED at 56% pass rate (direct 2025→2026 successor)
- NUMBER: across **100+ models**, average **security pass rate = 56%** — "barely changed from 55%"
  in the 2025 report. Put differently: **~44%** of AI code-gen tasks introduced a risky
  (OWASP-class) vulnerability when given no security-specific guidance (vs ~45% in 2025). Syntax
  pass ~100% (code compiles) but security stalls. **Best model GPT-5.5 = 68%** (still fails ~1 in
  3 security tasks); code-purpose-built models avg ~51%. XSS pass only ~15%, log injection ~12%;
  Java worst at ~30% (but most-improved). Headline: "LLMs are getting smarter, but not safer."
- MEASURES: controlled security testing of model outputs on standardized tasks.
- SOURCE: Veracode, **2026 GenAI Code Security Report**, blog + press **2026-07-28**.
- URL: https://www.veracode.com/blog/2026-genai-code-security-report-ai-risk/ ;
  press https://www.businesswire.com/news/home/20260728207685/en/ ;
  report https://www.veracode.com/resources/analyst-reports/2026-genai-code-security-report/
- STATUS: **Verified** (fetched Veracode 2026 blog; confirmed via SD Times + TNW + businesswire).
  Vendor (Veracode sells AppSec) — disclose.
- L06: **Clean 2026 successor to our F6.** The story got STRONGER: a full model generation later,
  security did NOT improve (55%→56%). "Models got smarter, not safer" is a genuinely 2026,
  denominator-anchored, non-obvious hook. Directly supersedes the 2025 45% number — use 56%
  pass / 44% vuln.

### R4 — Faros "Acceleration Whiplash": largest 2026 telemetry study (THE new structural-cost hook)
- NUMBER: telemetry from **22,000 developers / 4,000+ teams, two years of before-and-after data**.
  Under **high AI adoption**: individual throughput **+34%**, epics/dev **+66%** — BUT bugs/dev
  **+54%**, incidents per PR **+242.7%** (incidents-to-PR ratio "more than tripled"), median PR
  review time **+441%**, code churn (lines deleted soon after written) **+861%**, and **31.3%**
  more PRs merged with **zero review** (reviewers can't keep pace with volume).
- MEASURES: objective git/delivery telemetry (not self-report), high-AI-adoption cohorts vs
  their own before-AI baseline / lower-adoption teams.
- SOURCE: Faros AI, "AI Engineering Report 2026: The Acceleration Whiplash," **published Apr 2026**.
- URL: https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways ;
  PDF https://pages.faros.ai/hubfs/AI_Engineering_Report_2026_The_Acceleration_Whiplash_Faros.pdf ;
  coverage https://adtmag.com/articles/2026/04/22/more-code-more-bugs.aspx
- STATUS: **Verified** on numbers via Faros blog + ADT Mag + multiple 2026 secondaries
  (consistent). Primary PDF resolvable (not fetched directly — WebFetch 403/404 on some Faros
  URLs). Vendor (Faros sells eng-analytics) — disclose.
- L06: **This is the freshest, largest, telemetry-based (not survey) 2026 fact.** It replaces the
  DORA-2025 "throughput up, instability persists" story with harder, bigger, objective numbers and
  a memorable name. Best 2026 candidate for the "AI speeds output but breaks delivery" beat.

### R5 — JetBrains Aug-2026: 90% weekly / 68% daily agent adoption; Copilot dethroned
- NUMBER: **90%** of professional devs use AI coding agents at least weekly, **68%** daily
  (May–Jul 2026 field). Tool churn: GitHub Copilot **29%→21%** YoY; Claude Code ~**39%** global
  (47% US); Codex **3%→16%** (Jan→mid-2026); Cursor ~12%.
- MEASURES: self-report, >15,000 professional devs, globally representative.
- SOURCE: JetBrains, **2026-08**, "AI Coding Agents: Adoption Trends."
- URL: https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/
- STATUS: **Verified** (fetched JetBrains blog). No trust/quality figures — adoption only.
- L06: Freshest adoption number (Aug 2026). Good for "agentic coding is now the default" framing;
  supersedes DORA-2025's ~90% and SO's 84% as the most-current adoption figure.

### Which of our 2025 facts got a 2026 update — and which did NOT
- **F1 METR (19% slower):** UPDATED, and REVERSED → see R1. The old slowdown is stale; a modest
  (noisy) speedup is now METR's stance. Biggest change. Do not reuse the slowdown as current.
- **F2 Stack Overflow (66% fix almost-right code / trust 40%→29%):** PARTIAL. A 2026 SO blog (R2)
  re-frames the 2025 data around the trust gap (84% adoption, 29% trust). The specific "66%"
  number did NOT get a 2026 refresh; 2026 SO *survey* results not out yet.
- **F4/F5 DORA:** NO 2026 DORA report yet (latest = 2025 "State of AI-assisted Software Dev").
  Faros 2026 (R4) is the de-facto 2026 successor for the same throughput-vs-stability story.
- **F6 Veracode (45% OWASP vuln):** UPDATED → R3. 2026 report: 56% pass / ~44% vuln, "smarter not
  safer." Clean successor; use the 2026 numbers.
- **F3 GitClear (refactoring collapse):** NO confirmed 2026 refresh found. Faros' 861% churn (R4)
  is the nearest 2026 analogue for the "code-churn/rework rising" story — use Faros for 2026.

VERDICT (2026 hooks, ranked):
1. **Faros "Acceleration Whiplash" (R4)** — freshest + largest + objective telemetry. Pair the
   upbeat side (+34% throughput, +66% epics) against the cost (+441% PR review, +861% churn,
   incidents/PR +242.7%, 31% PRs merged unreviewed). Memorable name, hard numbers, 2026-dated.
2. **Veracode 2026 (R3)** — "models got smarter, not safer": 56% pass / ~44% vuln, unchanged a
   full generation later. Best security hook; clean 2026 successor. Pair with R4's incident spike.
3. **METR reversal (R1)** — most *interesting* 2026 story precisely because it undercuts the
   viral 2025 slowdown; frame as "the one clean RCT that found experts slower has reversed — and
   even its authors call the new signal weak." Nuance hook, not a clean stat.
Adoption anchor: R5 (90% weekly / 68% daily, Aug 2026) — the current "AI is the default" number.
CONFIDENCE: high on R1/R2/R3/R5 (fetched primaries); high on R4 numbers via Faros blog + ADT Mag +
multiple consistent 2026 secondaries (primary PDF resolvable, not directly fetched).
GAPS: no 2026 DORA report yet; no 2026 SO *survey* results yet (Feb-2026 blog re-uses 2025 data);
no confirmed 2026 GitClear refresh; Faros primary PDF resolvable but not directly fetched (WebFetch
blocked) — numbers triangulated across ≥3 sources.
