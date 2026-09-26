# Control liveness: feed the gate a defect on purpose

Our evergreen take on **how you know a check still works**. Settled by
[ai-delivery-gap](../pieces/INDEX.md) (live 2026-09-25,
[blog](https://tellian.io/2026/09/25/ai-delivery-gap/)). Don't re-derive — extend.

## The frame: a silent detector is indistinguishable from a healthy one

A green CI run looks exactly the same whether everything is fine or the detector is dead. So the
question is never "is the build green" but **"is this gate still capable of saying no"** — and
there is one way to answer it: **feed it a known-bad artefact and watch**. Our published
formulation: *a control that has never been fed a deliberate defect should be treated as broken
until proven otherwise.*

## The practice has a name — use it, don't invent one

- **Bebugging / error seeding** — Harlan Mills, *On the Statistical Validation of Computer
  Programs* (IBM FSD, 1972): plant known defects, and from the share found estimate how many
  remain. **Honest boundary:** Mills measured the *artefact*; turning the same arithmetic on the
  *detector* (3 of 10 seeded found = the control's sensitivity) is **our** reading, not his.
  No settled Russian term — we write «засев заведомого дефекта».
- **Mutation testing** — the same trick narrowed to code, because code mutants can be generated
  from the language grammar, automatically, by the thousand. A surviving mutant *is* the hole in
  the test suite.
- Outside software the same norm is written down: **NFPA 720 8.4.5.1** requires real CO *in the
  sensing chamber* — «an electronic check … is not sufficient»; **EICAR** exists so you can test an
  antivirus without "setting fire to the dustbin in your office to see whether the smoke detector
  is working".

## Durable takeaways

- **Coverage is not evidence of detection.** Google (ICSE 2021, ~400k mutants, >33M test-target
  runs): a mutant would have flagged 1043 of 1502 high-priority bugs (70%) at the very change that
  introduced them — and *every* one of those changes **was already covered by existing tests**;
  the authors' own words: coverage "exhausted its usefulness". Martin & Xie (WWW 2007) show the gap
  numerically on XACML policies: **98.6% structural coverage vs 47% mutants killed**.
- **A control can be made to measure its own uselessness.** Tricorder (ICSE 2015) tracks the
  "not useful" click rate with thresholds fixed in advance: **≥10% → probation, >25% → may be
  switched off**. It caught a real nine-week outage of one analyzer (weeks 24→33, 2014).
- **The interval between detector checks is a design parameter of risk.** From functional safety
  (IEC 61508/61511): undetectable failures accumulate silently and expected miss probability scales
  with **half the proof-test interval**. Transfer the *frame*, not the arithmetic — that formula is
  derived for random hardware failures; software faults are systematic.
- **Three ways to test a detector, not one.** Seed a known defect · **independently re-do** the work
  (auditor inspections — PCAOB 2024 found deficiencies in 39% of audits inspected, risk-based
  sample) · **continuously measure a reference** (the metrology check standard — NIST IR 6969 calls
  "calibrate as needed" unacceptable). Where you can't seed, the other two are all you have.
- **A recipe exists only where the defect can be generated from a grammar** — programming language,
  manifest, a row of metrics. Of six SDLC stages, four have a ready recipe (architecture rules,
  code, CI policies, alerts/canary); prose artefacts (text requirements, ADR freshness, the agent
  instruction file, DB migrations, canary analysis) have none — we proposed ours, nobody has
  validated them.
- **Your own past incidents are the cheapest seed set** — expensive to earn, impossible to accuse of
  being invented. Run them through today's gates and see which one stays silent. (Porter, Votta &
  Basili refused to seed for exactly that reason: "No faults were intentionally seeded … All faults
  are naturally occurring.")
- **The counterweight, kept honestly:** seeding has a cost, and its benefit is measured worse than
  we'd like — cost is published for one stage only (~2.7h per 1000 mutations at 10-second tests).
  Compare blinding in clinical trials: 142 meta-analyses / 1153 RCTs found no average difference in
  effect estimates, and the authors still recommend keeping blinding.

## Sources

Curated in [`sources/INDEX.md`](../../sources/INDEX.md): `google-mutation-icse2021`,
`google-mutation-tse2021`, `tricorder`, `mills-bebugging`, `martin-xie-coverage`,
`just-mutants-faults`, `meta-ach`, `eicar-testfile`, `sre-workbook-alerting`.
Full 99-claim verification trail: `pieces/20260924_ai-delivery-gap/fact-check.md`.
