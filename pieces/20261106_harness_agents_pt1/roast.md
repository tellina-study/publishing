# Roast: harness-agents-pt1 (round 4 — post rewrite, Max's 9 points)

> Supersedes round 3. Round 3 flagged two Critical issues against the two-axis structural
> rewrite: (1) the axis-balance claim ("важны в равной мере") contradicted by actual word/table
> counts, (2) an orphaned, unframed quality-measurement section sitting outside both axes. This
> round checks the current text — which responds to Max's 9 explicit points (TL;DR, overview
> table+chart, 9-task table, trimmed methodology, harness-pickup clarity, H-task numbers, эталон
> callouts, closing-chart linking, "ловушки" deletion) — against both those still-open round-3
> issues and the new questions this restructuring raises on its own.

## Critical (must fix before ship)

1. **New internal numeric contradiction: "10 оценённых прогонах" vs "шести прогонах" for the
   same two tasks.** The new "Девять задач" table (line 65, T2; line 72, J) states both T2 and J
   were scored "во всех 10 оценённых прогонах." But the body text covering the exact same two
   tasks says the opposite number twice: "ни один агент, ни в одном из шести прогонов (три
   агента × два режима)" for J (line 93, repeated at line 201: "в этот разрыв не вписывается...
   шести прогонов... 0 из 4 у всех шестерых"), and "одинаковый средний балл во всех шести
   прогонах" for T2 (line 94). 3 agents × 2 harness states = 6, which is what every other mention
   in the piece uses — "10" has no basis anywhere else in the text and looks like a copy artifact
   from the new table's drafting.
   — **Fix:** change "10" to "шести" in both table cells (lines 65, 72), or if "10" means
   something else (extra calibration runs not otherwise described), say so explicitly — as written
   it just contradicts the piece's own later claims.

2. **The brief's own ship-bar item — "confound/50x/n=1 survives the edit" — is only 2/3 true.**
   `brief.md`'s ship-bar explicitly requires: "Честная методологическая часть не потеряна при
   редактуре (confound/50x/n=1)." Confound survives implicitly (line 84: cost recalculated from
   the provider invoice, not self-report, "потому что самоотчёт... нельзя брать напрямую"); n=1
   survives as one compressed sentence (line 241, as Max's point 8 asked). But **the ≈50×
   missing-price-row self-report bug — explicitly named in the brief as a must-survive number —
   is not in the piece anywhere** (checked by grep: no "50×"/"50x"/"в 50 раз" anywhere in `ru.md`).
   It lived in the deleted "ловушки" section and in the old, fuller "Как это мерили" saga; neither
   the new one-paragraph "Как мерили, вкратце" nor the self-report subsection in Ось 1 (which only
   carries the Claude Code ≈25× counter mismatch and the Hermes ≈10× cache/fresh conflation)
   picked it up. This is a direct ship-bar violation, not a style nit — the piece explicitly
   promised to keep this number and didn't.
   — **Fix:** add one sentence to "У кого самоотчёту можно верить" (or to "Как мерили, вкратце")
   naming the 50× price-row bug, the same way the 25× and ≈10× numbers are already named there.

3. **Forward-reference bug introduced by the new "Общая картина" placement.** The new overview
   section (Max's point 1) sits *before* "## Девять задач" (Max's point 2) — but its own s1-scatter
   prose already makes a specific, scored claim about a named task: "шесть точек задачи G...
   несмотря на то что именно на этой задаче качество реально менялось (0, 1 или 2 из 2)" (line
   56). Task G is not introduced, named, or described anywhere before this point — that happens
   two sections later, in the "Девять задач" table (line 70). A first-time reader hits a specific
   task letter and a specific score claim with zero context for what task G even is. Same problem,
   smaller scale, with the "из 8" denominator in the "Общая картина" table's quality column (line
   44) — it isn't explained until "Девять задач" (line 78), several hundred words later.
   — **Fix:** either move "Девять задач" before "Общая картина" (data before aggregate, which is
   also the more natural reading order), or add one clause in the s1-scatter prose flagging that G
   gets introduced properly below.

4. **Both of round 3's Critical findings are still live — Max's 9 points never touched them.**
   - *Axis-balance claim vs. actual text*: line 33 still says, verbatim, "обе этой статье важны в
     равной мере." Measured: Ось 1 (lines 99–165) = 1,123 words / 2 tables / 3 charts; Ось 2
     (lines 166–232) = 1,494 words / 3 tables / 3 charts — Ось 2 is 33% longer with 50% more
     tables for the same chart count. The gap narrowed since round 3 (was 59%/3×) but the literal
     sentence claiming parity is unchanged and the underlying asymmetry is still real and still
     measurable by anyone who counts.
   - *Orphaned quality section*: "## Там, где качество можно было измерить, оно не двинулось"
     (lines 88–97) still sits between "Как мерили, вкратце" and "## Ось 1," outside both axes,
     still forward-pointing generically into Ось 2 ("таблица и график — ниже, в разделе про ось
     2," line 92) rather than being folded into it. Its content (G/J/T2 scores) is then **retold a
     third time**, with a full table, inside Ось 2's "Эффект третий" (lines 217–224) — meaning the
     orphan section isn't even saving space by existing separately; it's adding a redundant fourth
     stop for the same three numbers (TL;DR → "Девять задач" table → orphan section → "Эффект
     третий" table).
   — **Fix (either):** fold the orphan section into Ось 2 as an explicit "нулевой, общий для обеих
   осей" result, cutting its now-redundant retelling in "Эффект третий"; or trim Ось 2's "Эффект
   первый" (still the most over-instrumented subsection — 2 tables + a named-task callout + a
   worked multiplication back to back) to bring the axes closer to the parity the text claims.

## Should fix

- **The same two scores (task G, task J) are stated in full four separate times** across the
  piece: the "Коротко" TL;DR (line 12, in general terms), the "Девять задач" table (lines 70, 72,
  with the actual numbers), the orphan quality section (lines 92–93), and the "Эффект третий" full
  table (lines 217–224) plus "Эффект второй" (line 201 for J). Each repetition is individually
  justified by its local argument, but stacked up this reads as the same fact dressed four
  different ways rather than four facts — exactly the kind of redundancy that inflates length
  without adding information. Cut at least one occurrence (the orphan section is the best
  candidate, per Critical #4).

- **Length: 5,573 words against the brief's own channel shape.** `brief.md`'s frontmatter targets
  `channels: [blog, telegram, linkedin]`, and `CLAUDE.md`'s channel table caps blog pieces at
  800–2,500 words. This draft is more than double that ceiling. Given the redundancy just listed
  and the forward-reference/orphan-section issues above, at least some of that length is
  structural debt from four rounds of additive feedback rather than irreducible content — this is
  worth a real trim pass, not just a note.

- **The closing synthesis chart (s2, candlestick) concedes it adds no new finding.** Its own prose
  says so directly: "Это тот же вывод, что в разделе про жанровый эффект, только теперь видно
  глазами" (line 239). That's a legitimate role for a recap visualization, but Max's point 9 asked
  for a "generalizing" visualization — as delivered, it's a restatement-with-picture of "Эффект
  первый," not a new generalization the reader couldn't already state from the text above.

- **"Общая картина" oversells itself in its own framing, then immediately walks it back.** Line 42
  calls the table "прямой ответ на вопрос «какой агент в среднем...»" — then line 52, two sentences
  later, says this is "агрегат по всем девяти задачам сразу, а не по типичной задаче," and that 2
  of 9 tasks dominate the token sums. The self-correction is honest and good calibration, but the
  initial framing ("прямой ответ") is exactly the kind of claim a reader who stops at the table
  (or screenshots it) will carry away unqualified. Soften "прямой ответ" up front rather than
  earning it back a paragraph later.

- **Both repo links appear three times, not the "TL;DR + end" the request asked for** — once in
  "Коротко" (line 16), once in "Всё вместе" (line 241), once in "Источники" (line 273–274). Max's
  point 7 asked for TL;DR-plus-end; the mid-article repeat in "Всё вместе" is the dispensable one.

## Minor / polish

- The "Девять задач" table's "Оценена?" column already states the actual scores for G/J/T2
  (lines 70, 72) — two sections before the dedicated "Там, где качество..." section explains the
  "почему only 3 of 9" context those scores need. Consider trimming that column to "да/нет" and
  moving the numbers to where they're explained.
- "эталон" callouts (Max's point 6) are consistently and correctly applied everywhere a quality
  score appears, including the explicit "нет эталона" note for files-changed (line 225) — no issue
  found here, flagging only to confirm this specific ask is fully delivered.

## What works (briefly)

- **Point 4 (does Hermes/dsh "pick up" the harness the same way)** is cleanly delivered in one
  paragraph right after the agent list (lines 27), with the key distinction stated plainly: same
  content, different physical format per agent. No ambiguity left for a careful reader.
- **Point 5 fix (Claude Code vs dsh on task H)** — the 3.31× vs 1.34× numbers are now explicit and
  load-bearing (line 211), with the ratio-of-ratios spelled out ("разница примерно в 2,5 раза").
  This directly closes the gap the owner flagged between the chart and the prose.
- **s1 overview scatter's prose delivers three genuinely chart-specific, falsifiable
  observations** (dsh's wide X-spread, Hermes's lower-left cluster, task G's scattered-but-
  undifferentiated-by-quality position) rather than just restating the overview table — this one
  clears the "real insight, not just repetition" bar even though its placement causes the
  forward-reference problem in Critical #3.
- **DO-NOT list: clean.** No harness verdict, no hype language, no leaked private-repo names,
  script names, or issue numbers, no evaluative "bad product" framing of Hermes/dsh (differences
  stay tied to measured numbers throughout), and no sentence conflates a process effect
  (tokens/steps/$) with a quality effect — "Эффект третий" and "Эффект второй" both explicitly
  separate "усилие" from "результат" as two different things in two different clauses.

## Verdict: REVISE

substance_fraction: 9/11
one-line: Fix the T2/J "10 оценённых прогонах" vs "шести прогонах" contradiction and restore the missing 50× self-report number the brief explicitly required to survive editing — both are concrete, fixable facts, not style opinions, and both are currently wrong or missing in a piece that stakes its whole identity on measured precision.
