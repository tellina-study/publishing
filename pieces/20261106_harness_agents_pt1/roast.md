# Roast: harness-agents-pt1

## Critical (must fix before ship)

1. **Thesis is not clear in paragraph 1 — fails the piece's own ship-bar item.**
   Para 1 (line 5) is 100% external hype-stats (SWE-bench 168–317, 29.8pp vs 8.8pp). A reader
   after 20 seconds learns "industry says harness matters, here are big benchmark numbers" —
   indistinguishable from the hype pieces this draft is positioning itself against. The signal
   that this is *our own* experiment appears only at the tail of para 2 ("Мне захотелось
   проверить... взять несколько агентов и прогнать каждого... дважды"), and the actual finding
   ("получили не подтверждение, а более интересный результат: быстрой победы харнеса не видно")
   doesn't land until para 5 (line 13, "Ответов эксперимент дал два..."). That's ~300 words and
   two full external citations before the reader knows what this piece actually claims. Ship-bar
   item 1 ("Тезис ясен в первом абзаце") is unchecked and should stay unchecked as written.
   — **Fix:** pull the one-line "мы проверили сами и лёгкой победы не нашло" claim into paragraph
   1, even briefly, before or interleaved with the SWE-bench numbers — the external stats can stay
   as colour, but shouldn't be the *entire* first paragraph.

2. **Hermes cumulative framing edges into the DO-NOT'd value judgment, despite each sentence
   being individually hedged.** The fact-check already flagged this and explicitly deferred it to
   roast (claim #4, "cumulative framing... worth one more look at roast stage against the brief's
   DO-NOT"). Tally what lands on Hermes specifically: highest repeat-run noise (up to 9.3x, line
   37), explicitly labeled "самый непредсказуемый из троих" (line 69), 0/2 on the rubric with
   0 files changed in *both* runs at the equal-price table (line 81), and then the line-53 payoff:
   "та же чувствительность к дешёвой модели, на которой Hermes теряет в качестве, похоже, той же
   природы, что и его самый крупный выигрыш в цене: там, где качество на задаче не критично, он
   экономит больше всех." That sentence directly follows the piece's own disclaimer ("не приговор
   продукту") and then undercuts it — it reframes Hermes's biggest win (cheapest) as evidence of
   corner-cutting/low effort, which *is* an evaluative judgment about the product, not just "behavior
   on this battery." The hedge word "похоже" doesn't fully neutralize a causal story that isn't
   measured anywhere (the fact-check calls this exact sentence "a causal unification... not
   directly measured or stated anywhere else"). Combined with the self-report-error finding being
   correctly pinned on Claude Code (good — that one is genuinely distributed), the net reader
   takeaway for Hermes specifically is "flaky and skimps when it can get away with it" — close
   enough to a product verdict that it should be rewritten, not just footnoted.
   — **Fix:** cut the "похоже, той же природы" causal sentence entirely, or replace it with a
   purely descriptive restatement with no shared-mechanism claim (e.g., state the two facts
   side by side, explicitly flag that the piece does NOT claim they share a cause).

## Should fix

- **"Почти наверняка" in the practical block is more confident than the methodology section
  earns.** Lines 109: "На навигации и разборе он почти наверняка окупается... На «построить с
  нуля» почти наверняка обойдётся дороже." The *direction* is well-supported (consistent across
  all 3 agents), but "почти наверняка" reads as a magnitude/certainty claim sitting right next to
  a methodology section that just told the reader every number above is n=1 per cell with up to
  9.3x run-to-run noise. Either hedge this phrase or explicitly tie it back to "direction held for
  all three agents, not magnitude" so it doesn't read as a stronger claim than the data supports.

- **Section header "Чем агенты отличаются друг от друга — ещё до всякого харнеса" is undercut by
  its own last example.** The "Хватает ли агенту дешёвой модели" subsection (line 51) ends with
  "Харнес был включён у всех троих одинаково" — harness was ON, just held constant. That's a valid
  design (isolate the agent variable), but the section's framing promises "before any harness" and
  this example isn't that; it's "harness constant, not absent." A careful reader notices the
  whiplash. One clarifying clause earlier in the section (e.g., "харнес то отсутствует, то держится
  одинаковым для всех троих — важно, что он не варьируется") would close the gap.

- **SWE-bench is used unexplained in the opening hook** (line 5), for an audience the brief
  explicitly says doesn't have to know agent jargon. The brief calls out "харнес"/MCP as terms to
  soften on first use but SWE-bench — doing real evidentiary work in the very first paragraph — gets
  no gloss at all. A half-clause ("стандартный тест, где агенту дают реальные баг-репорты и считают,
  сколько он закрыл") would cost six words and remove a stumble right at the hook.

- **Only one table in the whole piece**, despite this being the piece explicitly pitched as
  "simplified but genuinely scientific, not a listicle." The genre-effect numbers (steps: 0.84x /
  1.16x; per-step cost: 1.14x / 1.17x) are dense and load-bearing but delivered only in prose
  (lines 59–61) — a reader has to re-parse four decimals embedded in two paragraphs. A compact
  table there (genre × step-ratio × per-step-cost-ratio) would do more for the "scientific, not
  anecdotal" bar than the prose currently does, and it's exactly the kind of table a rigorous
  write-up would reach for.

- **Noise ceiling discrepancy vs. brief.** Brief/outline flagged "9–16x" as the repeat-run
  variance to report; current draft caps at "до 9,3" (line 37) and "почти до девяти раз" (line 95).
  Fact-check already flagged this as open/non-blocking and assumed it's an intentional correction —
  but that assumption isn't confirmed anywhere in this draft's trail. Get an explicit one-line
  confirmation from whoever ran the numbers that 16x was a withdrawn/corrected figure, not a quietly
  dropped one, before shipping.

- **Length ~2440 words vs. the outline's own 1700–1900 target** — about 30% over. Not fatal (the
  extra length mostly buys the thorough 4-part "agent character" section, which earns its place),
  but worth one trim pass. Candidates: the repeated "не приговор продукту" / "харнес не вытащит
  задачу, которую агент... в принципе сделать не может" caveat appears in slightly different words
  twice (lines 53 and 118) — fine as an intentional callback, but check it isn't just restating
  itself for safety's sake.

## Minor / polish

- "Суб-агенты" (line 41) and "кэш" (line 47) get light-to-no definition; probably fine given
  surrounding context, but on the edge of the audience's stated floor ("не знает жаргон").
- Title in the file ("Харнес по частям. Часть 1: три агента, девять задач — и никакой лёгкой
  победы") differs slightly in punctuation/wording from the brief's registered title ("Харнес по
  частям, часть 1... и нет лёгкой победы") — harmless, but worth a sanity check that this was a
  deliberate edit and not drift.

## What works (briefly)

- **Zero internal-process leakage.** Grepped for ROAST, alm#, issue #, `agent-lab-manager`,
  `agent-harness-registry`, `harness-control`, `tellina-study` — nothing. Clean.
- **No literal "харнес нужен/не нужен" verdict, no hype language** ("game changer" etc.) — grep
  confirms neither appears; the closing section genuinely stays open ("харнес — это обмен, и знак у
  обмена меняется от задачи к задаче и от агента к агенту") and the part-2 teaser lists categories
  without spoiling results, as required.
- **The two parallel threads (genre effect vs. agent-vs-agent character) stay in clearly separate,
  well-labeled sections** and the one place they're explicitly recombined ("«как агент реагирует на
  харнес» — свойство не харнеса, а пары агент плюс задача", line 71) is the intended synthesis, not
  an accidental blur.
- **The methodology section (lines 87–99) genuinely delivers the confound/50x/n=1 ship-bar item** —
  concrete, with the price-version confound, the 50x self-report error pinned on Claude Code (not
  Hermes — good for balance), and an explicit n=1-per-cell caveat tied to the hedging words used
  earlier in the piece.
- **The antiexample table (lines 77–81) is concrete and memorable** — a real worst case, not an
  abstraction, exactly per ship-bar.

## Verdict: REVISE

substance_fraction: 7/10
one-line: Move the piece's own thesis (our experiment, no easy harness win) into paragraph 1, and cut or de-causalize the "Hermes's savings = corner-cutting" sentence (line 53) before it reads as the product verdict the brief forbids.
