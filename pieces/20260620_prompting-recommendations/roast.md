# Roast: prompting-recommendations

Scope: RU canonical longread, ~4188 words. Dual audience (agent-builders + ordinary chatbot users).
Checked against brief and fact-check. v1 roast (REVISE) is preserved below the v10 section.

---

## Roast v10

Reviewing the owner's scannability pass: blockquote cards (💡/📌/🛠️/🎯), emoji budget
subheadings, TL;DR label, softened opener, the "Пример бьёт запрет" card moved 3→4, finale
reordered (Общие решения before Стек под каждый тип), RU→«язык пользователя».

The big v1 criticals are GONE: the 99% MECW figure is now "эффективный контекст в разы ниже"
(line 160), the caveman "бенчмарк" is now "воспроизводимом микро-тесте автора" (line 103),
the Chroma claim is hedged. Good. New issues are mostly the seams left by the v10 reshuffle.

### Critical (must fix before ship)

1. **The moved card orphaned its antipattern row in Приём 3.** — line 151 vs lines 169–182.
   The "Пример бьёт запрет" explanation now lives in Приём 4 (line 171), but Приём 3's
   antipattern table still carries `Голый запрет «не делай так» без «делай вот так»` (line 151)
   and `Один образец ответа для структурированного вывода`. A reader scanning Приём 3's table
   hits the JSON-output / образец advice with zero supporting text — the support was carried two
   приёма away. The split also means the *same* idea (образец > запрет; JSON only on output)
   is now spread across Приём 3 (table) and Приём 4 (card + code block), so neither place owns
   it. Direction: either pull the example-vs-prohibition card back to Приём 3 where structured
   output is discussed, or move that table row out of Приём 3 into Приём 4's table (line 190)
   so the rule and its evidence sit together. Right now the move created a dangling reference.

2. **TL;DR order contradicts the body order, and the card promise mis-sets expectations.**
   — lines 9–14 vs Приём headings. TL;DR lists Язык → Место → Форма → Краткость → Значки →
   Порядок. The body runs Язык(1) → Caveman(2) → Форматы(3) → Место(4) → Значки(5). So the
   reader who internalises the TL;DR sequence meets the приёмы in a different order, and
   "Краткость" (TL;DR #4) is actually Приём 2. For a piece whose own thesis is "order and
   placement matter," a summary that re-orders its own body is a self-inflicted wound. Either
   renumber the приёмы to match the TL;DR's logical grouping (язык/место/форма/краткость), or
   reorder the TL;DR bullets to body order. The "Порядок" bullet (line 14) already states the
   *recommended* sequence (place+format → language → length last) — which is a THIRD ordering.
   Three orderings of the same five levers in the first screen is genuinely confusing; pick the
   priority ordering (the one in "Порядок" / the finale) and make TL;DR + приёмы echo it.

### Should fix

- **Orphan reference: MCP tool descriptions (2602.14878).** — refs line 287. Listed in
  Источники but never cited in the body. The "описания инструментов заслуживают столько же
  внимания" line (225) attributes to Anthropic "Building Effective Agents," not to the MCP
  paper. Either cite it where harness tool-descriptions are discussed (lines 38, 225, 260) or
  drop it from refs. A ref that appears nowhere in the body is exactly the "source that probably
  exists" smell this piece is otherwise careful to avoid.

- **The two 🛠️ practice cards (lines 126, 128) sit back-to-back and partly overlap.** Both are
  "из практики," both argue human-readable structure pays off, both land in Приём 3 before the
  "Как применять" list. Two adjacent first-person blockquotes of the same flavour read as
  padding and dilute the "structure pays twice" punch of the first. Direction: merge into one
  card, or move the second (read-it-with-your-eyes) point down into the YAML/Markdown-KV bullet
  where it's directly actionable. The v10 card pass added scannability but here it doubled a beat.

- **Card density is high enough to fragment, not aid.** 8 emoji blockquote cards
  (lines 57, 78, 126, 128, 158, 171, 202) plus 5 pattern/antipattern tables plus the TL;DR
  bullets. In Приём 4 the section opens with a 💡 card (158) that restates what the budget
  subheading "🎯 Бюджет внимания" (28) already said and what the TL;DR "Место" bullet (10) said —
  the same "edges good, middle drops" claim now appears ~4 times before the evidence. Cards work
  when they're the one thing to remember per section; when every section both opens with a card
  AND closes with a table, the prose between them reads as connective tissue nobody anchors on.
  Direction: cap it at one card per приём (the payoff), and let the opening 💡 in Приём 4 be the
  *only* statement of the placement rule rather than the fourth.

- **Length: ~4188 words vs blog shape 800–2500 (CLAUDE.md).** Still ~1.7× the top of range, and
  v10 added words (cards, TL;DR expansion). "Как работают разные модели" (lines 218–229) still
  substantially overlaps the per-type finale and the in-приём model notes (e.g. Claude-in-tail
  appears at 186, 225, and 229). The DeepSeek MoE-routing aside (227) is still ~3 lines on a
  thing the text tells you not to rely on. Cutting 300–500 words from the model section costs
  nothing — the finale's "GPT вперёд / Claude+DeepSeek в хвост" (229) is the only load-bearing
  model fact and it's already stated.

### Minor / polish

- Line 32–34: "держим в уме четыре типа задач" then a "### Четыре типа задач" subheading
  immediately under "🎯 Бюджет внимания." The four-types block is structurally a *third* thing
  under the "два бюджета" H2 — so the section titled "два бюджета" actually delivers two budgets
  AND four task-types. Reads slightly mislabeled; consider promoting "Четыре типа задач" to its
  own H2 or folding the budgets+types under a "Прежде чем начать" umbrella that names both.

- Line 160: "на 32K половина моделей валится" — appended after both NoLiMa and RULER; still
  reads as "either/both." Attribute the 32K/half figure to the specific benchmark.

- Line 158 (💡 card in Приём 4) has no bold lead-in label while the other cards do
  (💡 **Что это значит**, 📌 **Короткий рецепт**). Inconsistent card formatting after the pass.

- Line 134: improvingagents "+80%" and Markdown-KV "~60,7%" are single-vendor bench
  (GPT-4.1-nano) — the body says "на большинстве моделей" but the single-bench caveat the
  fact-check asked for (line 80) is softer here than for other single-source numbers. Tag it.

- Line 202 (📌 card in Приём 5) and line 206 ("Структуру стройте заголовками и тегами, а не
  значками") say the same thing 4 lines apart — close the section on one or the other.

- ты/вы: brief flagged this (brief line 54). Cards lean "вы," some practice cards lean "ты"
  (126: "ты сам её проясняешь"). Intentional voice shift for first-person cards is fine, but
  spot-check it's consistent within each register.

### What works (briefly)

- Reordered finale (Общие решения → Стек под каждый тип, lines 235–267) is the right call:
  cross-cutting questions first, then per-class stacks. Reads logically; the general/specific
  gradient is correct.
- The moved card's *bridge* is clean — line 169 "И раз уж речь о примерах" hands off from the
  few-shot positional-bias point (167) into the example-vs-prohibition card naturally. The
  transition works; it's only the left-behind table row (Critical #1) that's the problem.
- "Flaw or Artifact?" steelman in the finale (line 271) still lands — right hedge for a piece
  full of percentages, well placed before sign-off.
- Generalising RU→«язык пользователя» (lines 65, 70, 78) widened the audience without losing the
  concrete RU ×2 example where it earns specificity (57). Good balance.
- Calibration is now consistent: single-paper results (Hakim, CaveAgent, Mythbuster "предв.",
  Mind Your Tone "небольшой выборке") are flagged as such. The v1 inconsistency is fixed.
- The 🌐/💰/🎯 emoji subheadings genuinely help the dual audience navigate to their half.

### Verdict: REVISE

Not SHIP: Critical #1 (the moved card left a dangling antipattern row in Приём 3) and #2 (three
different orderings of the five levers in the first screen) are real reader-facing defects
introduced or exposed by the v10 reshuffle — both quick fixes, neither fatal. Not HOLD: spine is
sound, sourcing core holds, finale reorder is an improvement, calibration is clean.

substance_fraction: ~0.8 (findings are structure/orphan-source/calibration, not style nits)

one-line: Reunite the example-vs-prohibition rule with its Приём-3 table row, and collapse the
three competing orderings of the five levers into one — then ship.

---

## Roast v1 (archived)

(Superseded by v10 above; kept for trace. The three v1 Criticals — Chroma link, "benchmark"
anecdote, un-flagged 99% claim — are addressed in v10.)
