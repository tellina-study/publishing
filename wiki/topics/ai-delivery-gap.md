# The AI delivery gap: every part faster, the whole not

Our evergreen take on **what measurably happens to software delivery when AI writes the code**.
Settled by [ai-delivery-gap](../pieces/INDEX.md) (live 2026-09-25,
[blog](https://tellian.io/2026/09/25/ai-delivery-gap/)). Don't re-derive — extend.

## The frame: the bottleneck moved into the control

Local development metrics go up; what reaches the user does not move with them. The constraint
travelled downstream — into review and the quality gates. The industry's answer is to take the
human out of that loop, which has **measured wins and measured losses**, and turns everything on
one question almost nobody answers: **is the remaining detector alive?**
(→ [defect-seeding](defect-seeding.md)).

## The numbers that carry it

- **Chen & Stratton (Harvard, Aug 2026)** — staggered DiD on telemetry, 718 firms, 725,938 workers,
  300M events, Jan 2021 – Mar 2026: after moving to AI agents **+30% lines of code, +20% commits,
  +23% PRs**, while shipped output is "small positive, but statistically insignificant" (estimates
  rule out an increase above ~12%). Review time **+49%**, share of PRs with changes requested nearly
  doubled — and the bottleneck **persists after AI review tools are adopted**.
  **Honest boundary:** three separate coefficients, not a mediation — the data do not assemble them
  into one causal chain.
- **NBER WP 35275** (Demirer, Musolff, Yang) — 500k+ GitHub developers, matched event study:
  **+240% commits, +80% projects, +30% releases** — cumulative across three tool generations, not
  one switch-on — and "task-level AI productivity gains have translated only partially into shipped
  and used software".
- **DORA 2024** (pp. 37, 39–40) — per +25% AI adoption: **+7.5%** documentation quality, **+3.4%**
  code quality, **+3.1%** review speed, but **−1.5%** delivery throughput and **−7.2%** stability.
  **Boundary:** "AI adoption" is a latent self-report scale of seven items, not a measured input.
- **DORA 2025** reverses the throughput sign ("from negative to positive"); the −7.2% stability
  finding is neither confirmed nor refuted — the 2025 instrument is three items (incl. *trust*),
  so it is not the same measurement.

## Taking the human out of the loop — both sides at the same weight

- **Wins.** Meta's **RADAR** (arXiv:2605.30208): 535k+ diffs reviewed, 331k+ landed; relaxing the
  risk threshold p25→p50 auto-approves **60.31%**; revert rate **1/3** and production incident rate
  **1/50** of non-RADAR diffs. **Boundary:** diffs are selected by risk through an eligibility
  funnel and evaluated by observational before/after — not randomisation.
  DORA 2019 (p. 50, ~1000 respondents) separately found external change approval correlates with
  **2.6× more low performers** and "no evidence to support" it.
- **Price.** Anthropic's classifier replacing manual confirmations misses **17% of dangerous
  actions** (FNR on n=52 real overeager actions; 0.4% FPR on n=10,000 real traffic) — counted by the
  system's own authors. And **93% of permission prompts are approved** anyway: approval fatigue is
  what the automation is escaping from.
- **The asymmetry to state out loud:** the removal of control has mostly been measured by the people
  doing the removing, and the "AI code is worse" arguments largely measure AI code **with a human
  still in the loop** — a different question.

## Durable takeaways

- **Never present a local metric as delivery.** Lines, commits, PRs, task-level speed-ups are inputs;
  throughput and stability are the outcome, and in this data they do not move together.
- **Name the denominator and the instrument.** Self-reported adoption scales, risk-selected samples
  and before/after comparisons are all legitimate — and all fragile; say which one a number came
  from, and never treat the DORA calculator's demo inputs as a measured effect.
- **If a piece is about AI, AI must be visible in every section** — what it breaks, what it fixes,
  what practice follows (owner's rule, `notes/owner-taste.md`).

## Sources

Curated in [`sources/INDEX.md`](../../sources/INDEX.md): `chen-stratton-bottlenecks`,
`nber-writing-vs-shipping`, `dora-2024`, `dora-2025`, `meta-radar`, `anthropic-auto-mode`,
`dora-2019`. Full 99-claim verification trail:
`pieces/20260924_ai-delivery-gap/fact-check.md`.
