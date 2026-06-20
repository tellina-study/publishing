# Roast: prompting-recommendations

Scope: RU canonical longread, ~4040 words. Dual audience (agent-builders + ordinary chatbot users).
Checked against brief and fact-check (the ~20 must-fixes). Verdict at bottom.

## Critical (must fix before ship)

1. **Chroma link almost certainly 404 — must-fix #6 NOT applied.** — line 42 and refs (line 293).
   Fact-check #6 says cite Chroma at `trychroma.com/research/context-rot`. The body uses
   `https://research.trychroma.com/context-rot` (different host + path). This is one of the
   load-bearing "context rot / distractors" claims. Resolve the actual URL and paste the one
   that returns 200. A dead link on a flagship claim in a piece *about* sourcing rigor is the
   worst possible miss. (Verified this run: the URL in the body does not match the URL the
   fact-check verified.)

2. **"85-токенный дистиллят бил 552-токенный, 100% фактов" rests on an anonymous personal GitHub
   repo, presented as "бенчмарк".** — line 106. Must-fix #4 correctly moved the link to
   `kuba-guzik/caveman-micro`, but the *framing* is still "в бенчмарке на coding-задачах". A
   one-person repo is an anecdote, not a benchmark. Either downgrade the language ("в одном
   воспроизводимом микро-тесте автора X") or drop the exact 100%/85-vs-552 numbers. As written it
   over-claims rigor the source doesn't have.

3. **"вплоть до 99%" + "спотыкается порой уже на сотне токенов" is a single preprint stated as
   near-fact.** — line 42 (Paulsen / MECW). This is the single scariest number in the piece and it
   comes from one un-replicated 2025 paper. The hedge "порой" is doing a lot of work for a 99%
   claim. Add an explicit "одна работа, ещё не воспроизведена" tag the way you (correctly) did for
   Hakim's +26 п.п. and CaveAgent. Right now the calibration is inconsistent: some single-paper
   results are flagged as preliminary, this one (the most alarming) is not.

## Should fix

- **Thesis is split across two competing one-liners.** The H1 promises "язык, форма и место" /
  "чтобы нейросеть понимала лучше" (a *quality* claim). The TL;DR's dominant beats are about
  *cost/tokens* (2–2,5×, −75% vs −15–20%, эмодзи дороже). A 20-second reader can't tell if this is
  "write so the model understands better" or "write so you spend fewer tokens." Pick the primary
  axis in the first sentence; the cost material is the supporting act, not a co-headline.

- **TL;DR is six bullets + two extra paragraphs (lines 5–16). That is not a TL;DR, it's a
  pre-summary.** For the mass reader the brief wants to onboard, this is already a wall. Cut the
  "честная рамка" paragraph (line 14) and the "дальше — приём за приёмом" paragraph (line 16) out
  of the TL;DR block — they are meta-navigation, not the takeaway.

- **The "English-harness + Russian I/O" section (lines 67–84) is the densest in the piece and lands
  well structurally, but it buries its own load-bearing caveat.** The "7–9B post-trained models
  flip the result" hedge (line 71, must-fix #14) is parenthetical inside a "почему английский
  выгоден" paragraph. Good that it's there; bad that the section's bolded conclusion (line 84)
  doesn't carry it. A sharp reader will quote line 84 back at you as over-claim.

- **"Mind Your Tone" rudeness result (line 88) — keep the steelman but the number invites misuse
  even with the hedge.** "84,8% против 80,8%" on "небольшой выборке" with one cross-lingual
  counterweight is exactly the kind of viral-thread stat the brief's DO-NOT list warns against
  ("не превращать в вирусный листикл"). It's well-hedged, but ask: does it earn its place, or is it
  a spicy aside that dilutes the spine? Consider compressing to one sentence.

- **"Markdown — самый родной регистр" is now hedged as "рабочая гипотеза" (line 125) — good — but
  the TL;DR (line 8) states "Markdown модели понимают лучше всего" flatly, no hedge.** Must-fix #13
  said this is an authorial frame, not a sourced fact. The hedge exists in the body but not in the
  summary the mass reader actually reads. Align them.

- **Two contested-number bases are clean in body but the closing "Что отбросили" list re-states them
  bare.** Line 264 "Русский… в 2–2,5 раза дороже" (fine, matches must-fix #7) and line 267 caveman
  "реально ~15–20%". These are consistent — good — but line 10 TL;DR says "~15–20%" while body line
  106 says "~14–21%". Pick one range and use it everywhere; the drift looks careless in a
  precision piece.

- **Length: ~4040 words against a blog shape of 800–2500 (CLAUDE.md).** This is ~1.6× the top of
  the stated range. It's a canonical reference and the master table justifies some of it, but the
  "Как работают разные модели" section (lines 200–213) substantially overlaps the master table's
  "Поправка по модели" column and the decision rules. One of the two model-specific treatments is
  redundant. Cutting ~400–600 words there costs nothing.

## Minor / polish

- "Четыре класса задач" (line 48) says "три класса плюс один сквозной слой" — the heading says
  "четыре", the text says "три плюс один". Pick one framing; the off-by-one reads as an error.
- Line 42: "на 32K половина моделей уже валится" — attribute which benchmark (NoLiMa or RULER) gives
  the 32K/half figure; right now it's appended after both and reads as either.
- Line 133: "YAML обходит XML, который раздувает токены на +80% к Markdown (на большинстве моделей;
  на Llama картина инвертировалась)" — single-model-ish source (improvingagents, GPT-4.1-nano); the
  "+80%" needs the "single-vendor bench" tag the fact-check (line 80) asked for. It's in the body
  prose but easy to read as general.
- Line 162: SEAL described as "обучаемый метод усиления внимания, не просто трюк в промпте" — good,
  must-fix #20 applied. But it sits in a how-to section about prompting; a *trainable* method is
  out of reach for the mass reader and most prod-prompt authors. Consider footnoting rather than
  inlining.
- Line 211: DeepSeek MoE-routing speculation is correctly tagged "догадка одного блога" (must-fix
  #16 applied) — good. But it's still ~3 lines on a thing you tell the reader not to rely on. Trim.
- Sources block: "Found in the Middle" (line 293) is cited in refs but never referenced in the body.
  Either use it or drop it from refs.
- ты/вы consistency: brief flagged this as an open item (brief line 54). Body is mostly "вы" but
  spot-check the imperatives — do a final pass.

## What works (briefly)
- The "Flaw or Artifact?" steelman section (lines 192–196) lands. It's the right move for a piece
  full of scary percentages and it's placed well (near the end, before the synthesis). Keep it.
- The self-referential "this article is built by its own rules" callbacks (lines 44, 283) are
  earned, not cute — they demonstrate the thesis.
- Must-fixes #1, #2 (ID split), #3, #16, #19, #20, #9 (25 langs), #7 (2–2,5×) appear applied in the
  body. The fact-check largely landed.
- Pattern/Antipattern tables + master table + decision rules + checklist genuinely serve the
  agent-builder half of the dual audience. The "для тех, кто просто пользуется" box (lines 217–224)
  is the right onboarding ramp for the other half.

## Verdict: REVISE

Not SHIP: at least 3 real Critical issues are open — a likely-dead flagship link (must-fix #6 not
applied), an anecdote dressed as a "benchmark", and an un-flagged single-paper 99% claim that
breaks the piece's own calibration discipline. None are fatal to the argument; all are quick fixes.
Not HOLD: the spine is sound, sourcing core holds, structure works.

substance_fraction: ~0.85 (most findings are sourcing/calibration/thesis, not style nits)

one-line: Fix the Chroma link, downgrade the "benchmark" anecdote and the 99% claim to single-source
hedges, and reconcile the quality-vs-cost thesis so the first screen says one thing — then ship.
