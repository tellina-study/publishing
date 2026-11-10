# Mirror review: harness-agents-pt1

> Supersedes the prior round (REVISE, on the pre-rewrite draft with the axis split, Definition,
> and six data charts). The orchestrator has since rewritten the piece directly against nine
> pieces of Max's own feedback — none of it reviewed yet. This pass confirms what that rewrite
> fixed from the prior round (not re-flagged below) and focuses on the specific thing it was asked
> to check: does trimming methodology to near-nothing, while simultaneously adding an aggregate
> overview, a fuller task table, and a TL;DR, leave the piece internally consistent about how much
> depth it shows inline vs. defers to the open dataset — and does the result still read as one
> article, not an assembly of nine separately-satisfied checklist items.

## Confirmed fixed from the prior round (not re-flagged)
- The three "инсайт графика" label-announcements — gone, checked by grep, none remain.
- The three "не декоративно / не декларация / не ради иллюстрации" self-justifying asides — gone.
- The d1/d2 diagram-vs-prose duplication — both diagrams now stand on their own; nothing narrates
  them box-by-box in the sentence right after.
- The "почему не верить одной цифре" section — deleted, confirmed by grep, no remnant.
- Claude Code vs. dsh reading too similar on a chart that shows a real gap — fixed with real
  numbers now (3.31× vs 1.34× on task H, "разница примерно в 2,5 раза", плюс the "узор по всей
  батарее" table giving each agent a genuinely distinct profile sentence).

## Where this misses Max's bar (must fix)

1. **The one methodological fact that matters for reading every single number in the piece — n=1,
   no statistical test — is disclosed only in the next-to-last paragraph, line 241, after ~5300
   words of presenting those same numbers as findings.** This is the direct cost of cutting
   methodology down to one paragraph: that paragraph kept the *why* (holding the model constant,
   repricing off the provider invoice) but lost the one caveat that should gate how the reader
   holds every table before it — the aggregate overview's table, the whole of axis 1, the whole of
   axis 2. It isn't that the methodology cut was wrong in principle (see "where it nails" below) —
   it's that this specific sentence got stranded by the cut instead of migrating with the rest of
   "как мерили" to sit right after it, early. Move it (or a one-line echo of it) into or
   immediately after "## Как мерили, вкратце," not just at the finish line.
2. **"## Коротко" is, almost verbatim, the exact banned label.** The standing rule names
   "«Коротко:»" by name as a машинная этикетка to cut, and in the same breath prescribes the
   correct word for exactly this block: "Сводку — явным ярлыком **TL;DR**." This section does
   precisely what Max asked for in substance (both repo links, the right findings, properly
   hedged) and then headlines it with the one word his own profile singles out as the violation.
   Rename to `## TL;DR`.
3. **The aggregate-overview table's quality column — "(из 8, одинаково с харнесом и без)" — is
   ungrounded at the point it appears.** This is the concrete collision the review was asked to
   check for: Max wants the aggregate up top (item 1) *and* wants every quality table to state its
   reference score before the table (item 6) *and* the "из 8" in this, the very first table in the
   piece, only resolves 38 lines later in the task table ("из 2" T2/G + "из 4" J = 8), which hasn't
   been shown yet. A skimming reader hits "из 8" with no way to check it means anything. Every
   other quality table in the piece states its reference right before it (task G: "эталон — 2 из
   2," stated in prose, immediately preceding the table) — this is the one place that doesn't,
   precisely because it's the one table asked to come before the detail that would ground it. Fix
   in place, don't reorder: add the breakdown inline in the header or the sentence right above it
   ("из 8 = 2 по T2 + 2 по G + 4 по J, по задачам — ниже").
4. **The candlestick recap's own caption admits, in its own words, that half of what it shows is
   not a new insight.** "Это тот же вывод, что в разделе про жанровый эффект, только теперь видно
   глазами" — for the "построить" half of the chart, this is the chart explicitly narrating itself
   as illustration of an already-stated finding, which is exactly what the newest, explicit rule
   (2026-11-08, written in direct response to this piece) forbids: "минимум один чётко
   сформулированный инсайт, а не иллюстрация к уже сказанному словами." The "разобраться" half of
   the same caption *does* carry a genuinely new point (that the per-task token direction is mixed
   even though per-task step counts almost always drop — a finer grain than the aggregate ratio in
   Effect 1) — keep that, lead with it, and cut or rewrite the self-admitted recap clause for the
   "построить" half.

None of these four are structural, and none ask for more agent work beyond sentence-level moves
and one header rename — but all four are squarely inside what this review was dispatched to
check, so they're must-fix, not nudges.

## Would nudge
- **"честно" — still present, third round of recidivism now unaddressed.** Line 95 ("Это честно
  помечено как «не измерено»") and line 241 ("Мерить всё это честно трудоёмко") are pure author
  voice and exactly the banned tic ("ты откуда такой стиль взял?!"); line 71 ("честно сказать" in
  the task-H description) is more defensible as paraphrase of the actual task wording, lower
  priority. Given this was already flagged once and survived a full rewrite untouched, worth
  fixing on sight rather than flagging a fourth time.
- **Front matter runs long relative to the payload: 2,248 of 5,573 words (~40%) land before "Ось
  1" even opens** — TL;DR, three agent descriptions, the Definition, the harness-pickup paragraph,
  the architecture diagram, the two-axis framing, the aggregate overview (table + chart), the task
  table, the trimmed methodology, and the quality-summary, each independently justified and each
  individually requested, stacked in sequence. No single piece of it is wrong — each earns its
  place reread in isolation — but the cumulative weight before the actual per-axis analysis is
  worth a conscious check on the next pass: is there a pair of these that can share a paragraph
  rather than each getting its own?
- **"Если такой ответ вообще можно дать одной таблицей"** (aggregate-overview framing) is a hedge
  that does get paid off two sentences later (the "two tasks dominate the sum" point) — so it's not
  an empty tease. But the phrasing itself leans rhetorical-cute rather than plainly stating the
  limit, which is close enough to the newest "ноль заигрывания" line to be worth a plainer rewrite
  on the next pass: state the limit, don't stage a question about whether it's answerable.

## Where it nails his taste
- **The methodology cut is the right split, not an overcorrection.** What stayed inline is *why*
  two real engineering decisions were made (holding the model constant was work; self-reports
  couldn't be trusted so price was recomputed off the provider invoice) — that's substance a
  reader needs to trust every number downstream. What got pushed to the external link is *how*,
  in engineering-ticket detail (the earlier draft's checksum workaround, proxy specifics) — that's
  internal kitchen, exactly what the anti-проговор rule says doesn't belong on the page. WHAT
  stays, HOW goes external: this is a coherent principle, not the piece swinging from one failure
  mode to the other. Fix #1 above is the one place that split lost something that should have
  stayed, not evidence the split itself is wrong.
- **The aggregate-overview section genuinely answers to item 1** (it precedes all per-task detail,
  as asked) **without duplicating the TL;DR that precedes it** — the TL;DR states "ни один агент
  не выигрывает сразу по цене и качеству" as a compressed finding; the aggregate table two screens
  later is what actually proves it with real numbers. That's the вывод→тело→вывод schema working
  as designed across sections, not a redundant recap.
- **The normalized scatter (s1) earns a genuinely non-obvious insight**: task G's six points
  scattered across the whole field despite genuinely different quality scores shows, visually,
  that effort (steps/price) and outcome (rubric score) are different axes — a point the rest of the
  piece spends the next four sections proving in detail. The chart gets there first, by eye.
- **The piece does not read as nine bolted-on checklist answers.** Read end to end, the connective
  prose between tables and charts is doing real analytical work, not captioning ("дальше становится
  сложнее"; "значит, «как агент реагирует на харнес» — свойство не харнеса, а пары агент плюс
  задача") — the throughline survives the density of structure the genre rule actually demands.
- **No hype, no mentor tone, no evaluative language on the agents, title matches the body.**
  Re-checked directly, not just carried over from the prior pass.

## Calibration gaps (instinct vs. profile)
- Whether "Ось 1" / "Ось 2" as literal section labels still reads right to him — flagged last
  round, unresolved either way this round (left as-is), still worth a one-line confirmation rather
  than a second unilateral call from me.
- Whether a single consolidated "limits" heading is what the genre rule's "явная секция честных
  пределов" actually wants, versus caveats distributed at the point they're relevant (n=1 aside,
  "верхняя граница не закрыта" for dsh, "честно помечено как не измерено"). I lean toward
  distributed-but-early (hence must-fix #1 moving the n=1 line, not consolidating everything into
  one block) — but this is a reading of intent, not something Max has said directly about this
  piece.

## Verdict: REVISE

The structural asks all landed and don't collide with each other in principle: the methodology
trim is a coherent WHAT-stays/HOW-goes-external split, not a swing from over-detailed to
under-detailed, and the new front-matter sections (TL;DR, aggregate overview, task table) are each
individually earned and don't duplicate one another. What blocks SHIP is four concrete, narrow
items — the stranded n=1 caveat, the "Коротко" header reusing the exact word the profile bans by
name while prescribing "TL;DR" for this exact slot, one ungrounded denominator in the first table
the reader meets, and one chart caption that admits to being illustration rather than insight for
half its content — plus one recidivist word and one pacing note worth a conscious look, not a
rewrite.

one-line: move the n=1 caveat up into the methodology section, rename "## Коротко" to "## TL;DR,"
ground the "из 8" in the first table inline, and fix the candlestick caption's self-admitted recap
clause — everything else holds together as one piece, not nine checklist items bolted on.
