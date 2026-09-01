# Roast (storyline) — outline v3 «День ИИ»

Function: find what breaks the NARRATIVE before we spend a draft on it. Not style, not citations.
Judging the arc, the hook, the payoff, the ending, and honesty-under-positive-tone.

## Critical (must fix before drafting)

1. **The load-bearing conceit is arbitrary and a smart reader will catch it — §1.**
   "Современному ИИ ровно 12 лет" is anchored to the arXiv *submission date* of one paper
   (1409.0473, 2014-09-01). The problem isn't the fact — it's that *nothing in the arc justifies
   why THIS date is the birthday* over the obvious rivals:
   - Cho et al. encoder-decoder — **June 2014** (arXiv:1406.1078), earlier, and the outline itself
     leans on Cho as a pillar (§5, §3). If the "root" is the seq2seq/encoder-decoder line, the
     birthday is June, not September.
   - 2017 (the thing that *actually* scaled) — the outline's OWN payoff says the real shift was 2017.
   - 2012 AlexNet — the more conventional "modern deep-learning began" marker.
   The outline is aware of this (it lists Cho as a base) but never *defends the choice on-page*. Right
   now the birthday rests on "it's a nice arXiv timestamp that happens to be Sept 1 = День знаний."
   That is coincidence dressed as discovery. **A wide-but-thinking reader smells a gimmick the moment
   they realize the date was picked because it's convenient, not because it's the causal origin.**
   FIX: the piece must earn the date *inside the arc* — pick ONE honest claim and commit:
   either (a) "we're not claiming a true birthday, we're using a nice coincidence as a doorway —
   and here's the real lineage" (owns the gimmick, defuses it), or (b) make a defensible causal
   argument that *attention specifically* (not seq2seq) is the seed, and Bahdanau is where attention
   is born → then Sept 1 is genuinely attention's birthday. Option (b) is stronger for the spine but
   requires §3 to explicitly say "Cho gave the encoder-decoder; Bahdanau gave *attention* — and it's
   attention, not encoder-decoder, that survives to today's frontier (§7 confirms this)." Without one
   of these, the hook is the weakest link in the whole piece.

2. **The central payoff still smuggles the negative "not-the-title" framing — §1, §5, §8.**
   Owner's hard requirement: deliver the shift as EXPANSION, not as debunking. But three separate
   beats phrase it as *contradiction of the label*:
   - §1: "настоящий сдвиг был **не там, где написано на табличке**"
   - §5: "статья поворотная — **но не из-за того, что в заголовке**. Внимание тут не новое."
   - §8: "большой сдвиг часто не в том, что *добавили и назвали*"
   Each of these is the "the title oversells / the famous thing isn't the real thing" move — i.e. the
   *rejected* takedown angle, just softened. §6 does the addition correctly ("не вместо, а вместе"),
   but §5's "внимание тут не новое" actively deflates the very mechanism the title celebrates, and
   §1 promises a "gotcha" the owner said not to promise. **The arc currently peaks on a reveal that
   the label is wrong.** That IS the negative angle wearing a party hat.
   FIX: reframe the payoff as *what got added*, never as *what the title got wrong*. The exciting
   thing is "они убрали двигатель и дали идее простор → параллелизм → масштаб" — that's pure
   expansion and needs no "но не в заголовке" to land. Cut the label-correction phrasings; let the
   removal-of-recurrence be a triumph, not a correction.

3. **§7 is a second climax that deflates the first — the ending is not yet earned.**
   The emotional peak is §6 (idea breaks free → scaling → ChatGPT). Then §7 is ~340 words —
   the single longest section — of "what got quietly rewritten" (pre-norm, RoPE, decoder-only,
   FlashAttention, GQA, MoE) + a careful, hedge-heavy Mamba/frontier survey. This is a *frontier
   status report*, not a story beat. After the reader has just felt "and that's how we got ChatGPT,"
   §7 says "well actually the 2017 blueprint is half-rewritten and here are 6 arXiv ids and a hedged
   debate about SSM hybrids that isn't settled." **The adventure has a triumphant summit at §6, then
   a long technical descent that flattens the affect before §8 tries to re-inflate it for the
   birthday toast.** The "с Днём ИИ" lands on a tired reader.
   FIX (structural, pick one):
   - Cut §7 to ~150 words: ONE idea — "the skeleton (attention) still holds the throne 8 years on;
     everything around it got upgraded; that longevity is the real monument." Drop the 6-item rewrite
     catalog and the full Mamba debate into the врез/footnotes or a follow-up piece.
   - OR move a compressed §7 *before* §6, so the arc ends on the emotional summit + birthday, not on
     the frontier caveats.
   As written, §7's honesty (which is good) is bought at the cost of narrative momentum.

## Should fix

4. **The arc has two protagonists and the birthday only belongs to one — tension in the spine.**
   Brief insists on "два героя-статьи равного веса" (2014 and 2017). But the hook, the title, and
   the toast all celebrate *2014*. §7 works hard to give 2017 its due ("это буквально результат
   Васвани-2017"). The result: the story wants to crown 2014 (birthday) AND reassure that 2017 is
   the real engine — and the reader feels the outline hedging between them. A single-protagonist
   adventure ("one idea, 2014→ChatGPT") is cleaner than "two equal heroes, but we party for the
   younger one." Decide: is the hero *the idea of attention* (born 2014, matured 2017, still reigns)?
   If so, say that — then 2017 isn't a co-hero, it's the coming-of-age chapter, and the equal-weight
   framing should be dropped from the brief. The current "equal heroes" instruction fights the
   single-idea spine.

5. **Momentum sags between §2 and §4 — three explainer sections back-to-back.**
   §2 (what is attention), §4 (what is recurrence/why it's slow), plus §5's convolution aside are all
   *tutorial* beats. §3 is the only pure-story beat in the first half. The "adventure" doesn't really
   start moving until §5-§6. For a wide reader promised an adventure, that's a lot of "let me explain
   a concept" before the plot accelerates. Consider folding the recurrence explanation (§4) into the
   §3 story ("the model read word-by-word — and *that's* why the great idea couldn't grow") so the
   concept arrives as a plot obstacle, not a lecture slide.

6. **"Тадам — вот находка" tells the reader to feel delight instead of earning it — §1.**
   The outline stage-directs the payoff ("*Тадам*", "Логика находки ведёт читателя за руку"). In a
   draft this risks reading as the author congratulating themselves on the coincidence. The discovery
   only feels like a discovery if the *date genuinely is the root* (see #1). If it's a chosen doorway,
   "тадам" oversells it. Tie the tone of the reveal to whichever honesty-choice you make in #1.

7. **The RNNsearch / "Bengio penciled in the word attention" anecdote may undercut the birthday — §3.**
   The charming detail — "attention" was an almost-accidental note added by Bengio at the last pass —
   is fun, but it cuts against the conceit: if the *word* was a casual afterthought, why is the
   *paper's submission date* the sacred birthday of AI? The anecdote quietly says "the naming was
   incidental," which strengthens the "label doesn't matter" (negative) read and weakens the "this is
   the birth" (positive) read. Keep it, but land it as "the seed was planted almost without fanfare"
   (humility that supports the adventure) rather than as trivia that makes the naming look arbitrary.

## Minor / polish

- §8's "виден он не сразу" (the shift is only visible in hindsight) is a mild restatement of the
  rejected "memory got it wrong" theme. Watch that the conclusion's "lesson" doesn't drift back into
  "everyone misremembers where the shift was."
- Title says "выросла в ChatGPT" but the body's true climax is *removing recurrence → scaling*, not
  ChatGPT itself (ChatGPT is the endpoint, not the mechanism). Title is fine as a hook, but make sure
  §6 doesn't let ChatGPT steal the spotlight from the actual mechanism the piece is about.
- §7's Mamba hedging is factually careful but the *volume* of caveats ("осторожно", "оговорка чести",
  "спор не закрыт", "честный якорь в обе стороны") signals anxiety. In an adventure piece, that many
  hands-up hedges reads as the author bracing for attack. Fewer, firmer.

## What works (keep)

- The spine "one idea from an applied problem grows into ChatGPT" is a genuinely good adventure shape
  — narrow, concrete origin (translate a long sentence) → world-changing endpoint. That's a real arc.
- §6's "не вместо, а вместе" (attention + removal-of-recurrence = the pair that opened the door) is
  the correct, honest, expansion-framed payoff. This is the model the rest of the piece should match.
- The honesty guardrails in the header ("что держим честно") are exactly right and the outline mostly
  respects them — the 2014=bolt-on boundary is held.
- §3's "fixed-length vector is a bottleneck" as the diagnostic turning point is a strong, concrete
  story beat — the one place the first half genuinely moves.

## Verdict: REVISE

Not HOLD — the spine is sound and most of the material is here. But three things are load-bearing and
currently broken: the birthday is not earned on-page (#1), the payoff still phrases itself as
label-correction i.e. the rejected negative angle (#2), and §7 deflates the ending (#3). Draft from
this and you'll draft those flaws in.

substance_fraction: ~0.85 (findings 1–5 are structural/spine; 6–7 are real; only the 3 minors are polish)

one-line: **Earn the September-1 birthday inside the arc (or openly own it as a doorway), stop
phrasing the payoff as "the title is wrong," and cut §7 so the adventure ends on its summit — not on a
frontier status report.**
