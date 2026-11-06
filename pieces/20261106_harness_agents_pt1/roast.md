# Roast: harness-agents-pt1

> Supersedes the prior roast pass. That pass's two Critical findings (thesis buried past
> paragraph 1; the causal "Hermes's savings = corner-cutting" sentence) are both fixed in this
> draft — confirmed below under "What works." This pass evaluates the piece as expanded ~1.9x
> since then (full methodology exposition, named-task taxonomy, granular quality breakdown, a
> third pricing trap, the infra-noise anecdote, worked arithmetic).

## Critical (must fix before ship)

1. **dsh silently disappears from the piece's own flagship "agent-specific effect" finding.**
   — `## Тот же тумблер, но в руках разных агентов` (the section built entirely around "второй
   эффект... зависит... от того, кому харнес достался, — и иногда разворачивается в обратную
   сторону"), lines 155–172. The section's own framing promises per-agent coverage ("на всей
   картине у **каждого** агента читается свой узор," line 161) and then the comparison table two
   lines later has exactly two rows: Claude Code and Hermes. dsh is never mentioned once in this
   entire section — not on task J (where CC goes to 4.3x and Hermes drops to 0.25x), not in the
   "узор" table, not in the closing synthesis ("значит, «как агент реагирует на харнес» — свойство
   не харнеса, а пары агент плюс задача," line 172). Since dsh ran task J too (9×3×2=54 confirms
   all three agents hit all nine tasks), this is a real reporting gap, not a missing data point —
   and the piece elsewhere is careful to flag exactly this kind of gap for dsh explicitly ("dsh —
   тестировался только на дешёвой, сравнить не с чем," line 127). Leaving dsh out here — without
   even dsh's one-line verdict ("held near 1x, unlike the other two") — creates an unearned halo:
   a reader comes away thinking dsh is the "stable" one of the three specifically *because* it was
   never in the drama, when in fact we just don't know, because the piece didn't say.
   — **Fix:** add one clause giving dsh's actual number/pattern on task J (or, if the result
   genuinely isn't noteworthy, say so explicitly — "у dsh на этой же задаче разброс остался
   близко к исходному" — so the omission reads as a reported null, not a silent gap).

2. **The piece's single most important claim — "quality never moved" — is stated as an absolute
   header, but the body it introduces concedes 6 of 9 tasks were never scored for quality at all.**
   — `## Качество не двинулось — ни у одного агента`, line 71. This is not a minor finding
   among many; it is the core result the brief's own angle is built on ("Качество результата не
   изменилось ни разу"). The very next sentence hedges hard ("рубрика вообще смогла измерить, — а
   смогла она не везде одинаково"), and the bulleted breakdown that follows shows the "no movement"
   claim rests on exactly 3 of 9 tasks (one where only agent-vs-agent varied, not harness-state;
   one at a measurement floor — 0 everywhere; one at a ceiling — flat everywhere) — with the
   "оставшиеся шесть задач" explicitly unmeasured. The claim is true for what was measured, but a
   header this blunt, attached to the piece's central thesis, invites a reader (or a quote-puller,
   or a skimmer who reads only headers) to believe quality was checked across the board and never
   budged — a stronger claim than 3/9-task coverage supports. This is exactly the "unearned
   certainty on a load-bearing number" the brief's own calibration bar warns against.
   — **Fix:** fold the coverage caveat into the header itself, e.g. "Качество не двинулось — там,
   где его вообще можно было измерить," rather than relying on the reader to reach the hedge one
   sentence later.

## Should fix

- **The model-price-confound story is told in full twice, 140 lines apart, with the second telling
  adding almost nothing new.** Methodology (lines 56–58) narrates the flag-defaults-to-the-
  expensive-model bug in full, with mechanism and stakes ("Назвать модель по короткому имени
  значило незаметно подменить весь эксперимент"). The traps section (lines 194) retells the same
  anecdote almost beat-for-beat ("ровно та, что чуть выше чуть не подменила весь эксперимент через
  короткое имя флага"). Compare this to the other two traps in the same bullet list (self-report
  50x error, cache-token mislabeling), which are genuinely *foreshadowed* in methodology (one
  vague clause each, line 60) and only *fully told* once, in the traps section — that's the right
  pattern, and this bullet should match it: trim the first telling to a forward-pointer, or trim
  the second to a one-line callback instead of a full re-narration.

- **Methodology runs 1,042 words (≈22% of the piece) before the first finding lands, and it carries
  genuine infra-debugging texture (flag defaults, a shared non-personal config file, checksum
  restore-and-verify) that reads more like a dataset README than a blog narrative** — lines 24–69.
  This is defensible given the ship-bar's confound/50x/n=1 requirement, and the content isn't
  wrong, but the *level* of operational detail (specifically the config-checksum paragraph, lines
  57–58) is denser than the stated audience ("не обязан знать жаргон... решают, стоит ли
  вкладываться") needs to trust the result. The piece already has a natural release valve for this:
  the linked dataset (`workain/research-results`, already cited for "методологией, оговорками и
  разбивкой по задачам," line 212) is exactly where this level of detail belongs. Consider cutting
  the checksum mechanics to one clause ("снимок настроек перед прогоном, с проверкой после") and
  pointing the rest at the dataset link — this also removes the redundancy flagged above for free.

- **Precise two-decimal averages (0,84 / 1,16 / 1,17 / 1,14) are presented unhedged in "Один рычаг,
  а знак разный" (lines 135–153), and the "this is one measurement per cell, don't over-trust the
  decimal" caveat doesn't arrive until the "Почему одной цифре..." section, ~60 lines later** (line
  206: "каждая цифра выше измерена один раз... не говорит, насколько часто"). A reader hits the
  precise-looking ratios and the worked multiplication (1,16×1,14≈1,32) well before being told how
  much grain of salt they deserve. The piece's own hedging vocabulary ("примерно," "где-то") is
  used inconsistently here — the genre-effect numbers are stated as flat decimals, not "≈0,84."
  — **Fix:** either round these to the same "примерно"-hedged form used elsewhere, or move a
  one-line version of the n=1 caveat up to where these numbers are first used.

- **The infra-noise anecdote's payoff number doesn't clearly land.** Line 200: "чистый прогон...
  занял 874 секунды и 35 обращений к модели — быстрее, чем тот же агент на заметно более дорогой
  модели в другом раунде измерений (1124 секунды)." The paragraph's actual point (shared-machine
  memory pressure corrupted some runs; discard and re-run; that's why seconds aren't the main
  metric) is fully made in the surrounding sentences without this comparison. The 874s/1124s pair
  doesn't itself prove the clean run was noise-free (the discard-and-rerun context does that) and
  reads as a dropped-in factoid competing for attention with the real point. Cut it, or state
  explicitly what it's meant to demonstrate.

- **Carried over, unresolved:** the brief/outline flagged "9–16×" as the repeat-run variance
  figure; this draft caps at "до 9,3×" (line 91) / "почти до девяти раз" (line 204). Still no
  confirmation on record that 16× was a withdrawn/corrected number rather than a quietly dropped
  one — not visible in the text itself, but worth a one-line confirmation from whoever ran the
  numbers before shipping, same as the prior roast flagged.

## Minor / polish

- The self-report-is-unreliable thread is split across two sections by agent — Claude Code's
  three-mismatched-counters issue lives in "Чем агенты отличаются" (lines 96–100), Hermes's
  cache/fresh-token conflation lives in the traps section (line 196) — reasonable since one is an
  "agent character" trait and the other is a "measurement trap," but a reader assembling "which
  agents can I trust to self-report?" has to do that assembly themselves across ~100 lines.
- "Три счётчика токенов" (lines 96–100) and the cheap-model subsections are Claude-Code/Hermes-
  heavy by necessity (dsh wasn't tested on the expensive model), which is explicitly flagged in-
  text (line 127) — fine, just noting it's the reason dsh reads thinner in that part of the piece,
  unlike finding #1 above where the thinness isn't flagged.

## What works (briefly)

- **Thesis is now genuinely in paragraph 1.** Line 5 is a clean three-sentence paragraph ending in
  "быстрой, однозначной победы харнеса не нашёл" — the external SWE-bench hype-numbers are pushed
  to paragraph 2 as colour, not load. Ship-bar item 1 is met; the prior roast's #1 Critical is
  resolved.
- **The causal "Hermes's price-win = corner-cutting" sentence flagged by the prior roast is gone.**
  Grepped for it and its pattern — not present. The Hermes 0/2-with-0-files finding (line 184) now
  stays descriptive and explicitly declines to speculate on cause ("отдельный вопрос, на который
  этот эксперимент не отвечает").
- **Zero DO-NOT violations found on this pass**, specifically re-checked for the expanded material:
  no leaked `agent-lab-manager`, no process leakage (`ROAST`, `alm#`, script names), no mention of
  `agent-harness-registry` (correctly reserved for part 2, confirmed via grep), no explicit harness
  verdict, no hype language, and the earlier fact-check's flagged industry-wide overclaim ("почти
  любой харнес в индустрии...") has been narrowed to "у харнесов, которые мы смотрели" — now
  correctly scoped to the n=3 sample.
- **Process/quality-effect separation holds throughout**, including in the new material — the
  Hermes 0/2-but-4x-costlier passage (line 184) and the task-J passage (line 170) both explicitly
  state tokens moved and correctness didn't, in two separate clauses, never conflated into one.
- **Now four tables** (agent-divergence summary, genre×ratio, agent "узор," equal-price capability)
  — resolves the prior roast's "only one table" complaint.
- **Claude Code gets real, specific warts of its own** (three mismatched token counters, 50x
  self-report error, halved quality on the cheap model) — this keeps the "Hermes always looks
  worst" risk the prior roast flagged from compounding in this draft; the added material is
  reasonably balanced across agents, not piled onto one.
- **The worked arithmetic (1,16×1,14≈1,32 vs. 0,84×1,17≈0,98, lines 151–153) earns its place** —
  it's the one passage in the new material that turns a confusing null result into a legible
  mechanism, exactly the kind of concrete payoff the brief's ship-bar asks for.

## Verdict: REVISE

substance_fraction: 8/9
one-line: Give dsh its actual (or explicitly null) result in the task-J "mirror effect" section, and fold the quality-header's 3-of-9-tasks caveat into the header itself — both are fixable without touching the piece's structure or length.
