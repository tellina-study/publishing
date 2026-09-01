# Roast: transformers-vaswani (RU, near-final)

Function-framed adversarial pass on `ru.md`. Not fact-checking citations, not line-style — those run
elsewhere. Judging thesis, structure, altitude, honesty, calibration, ending.

## Critical (must fix before ship)

1. **11 inline `[проверить...]` editorial notes are still in reader-facing prose.** — lines 35, 52,
   53, 55, 93, 94, 96, 97, 98, 102. — These are raw notes-to-self bleeding into the body. Line 35 is
   the worst: `«внимание»... дописал в заключение Бенжио, почти между делом [проверить: рассказ
   Богданова через Turing Post]` — an unverified anecdote sitting mid-sentence with its own scaffolding
   visible. Line 102 has a `[проверить: ни одна лаборатория не раскрыла архитектуру...]` inside the most
   hedge-sensitive sentence of the piece. This is a hard ship-blocker independent of the fact-check:
   even if every claim verifies, the markers must be removed and the underlying claims either confirmed
   or cut. A skeptical reader who sees one `[проверить]` stops trusting the other 40 uncited assertions.

2. **The "12 лет / День ИИ" pretext leans on a coincidence the text over-sells as destiny.** — lines
   9, 11 (`Дата бьёт сама`), 112. — The honest read is: Bahdanau et al. was *submitted* to arXiv on
   1 Sep 2014, and 1 Sep happens to be День знаний. The piece frames this as "лучшего повода не
   придумаешь / дата бьёт сама" — but an arXiv submission date is an administrative timestamp, not a
   birthday of an idea (the work existed before submission; the idea "began" arguably at ICLR 2015
   acceptance, or when Bengio wrote the word in). The brief explicitly calls this "warm pretext, not a
   literal fact" — but the body treats it as if the date itself *proves* something ("дата бьёт сама").
   A sharp reader will call this a cherry-picked coincidence dressed as significance. Fix: keep the
   warmth but drop the note of inevitability — own it as a nice accident, not a cosmic alignment. Right
   now `Дата бьёт сама` is the single line most likely to read as gimmick.

3. **"12 лет" arithmetic is internally shaky and the piece flags its own doubt.** — lines 5, 9, 84,
   112. — Body says 2014→2026 = "двенадцать лет" (correct, 12) but *also* says the 2017 core holds
   "восемь лет спустя" (line 84: 2017→2025 = 8, but from 2026 it's 9). From the stated present of
   1 Sep 2026, Vaswani is 9 years old, not 8. Either the piece is pretending it's 2025 or the numbers
   were written at different times. Pick a reference year and make every interval consistent (12 for
   2014, 9 for 2017 if "today" is 2026). A reader who does the subtraction catches this instantly.

## Should fix

4. **Two stats without a clean baseline — the brief's own ship-bar flags this and it's unmet.** —
   line 78. — `прежние чемпионы стоили в разы, а то и в десятки раз дороже` and `в малую долю их
   стоимости` are comparative claims with no anchor number for the *competitors* — only the
   Transformer's own 3.5 days × 8 GPUs is given. "В разы, а то и в десятки раз" is a wide, unsourced
   range doing load-bearing work ("это... было главным сигналом"). Either give the competitor figure or
   soften to what the paper actually claims. The brief explicitly required "стат без базы/знаменателя"
   to be avoided; this is one.

5. **The scaling-laws leap is asserted, not earned, and slightly over-claims.** — lines 72–74. —
   `это предсказуемо превращается в качество... по довольно ровной зависимости` then the pull-quote
   `Теперь во многом хватало добавить вычислений и данных — и ждать`. For a non-engineer this is the
   most important causal claim in the piece (parallelism → scaling → ChatGPT), and it's stated as fact
   with two citations bolted on. The honesty problem: scaling laws are empirical regularities with known
   breakdowns (data walls, diminishing returns — the Chinchilla citation itself is a *correction* to
   Kaplan). "Хватало добавить вычислений и данных — и ждать" is exactly the "just add compute" folk
   claim the field has since complicated. One clause of calibration would inoculate it.

6. **Momentum sags in the middle: two adjacent sections re-explain the same two-part idea.** —
   §"2017: убрать всё лишнее" (46–61) and §"Что открыло дорогу: две находки" (63–70). — The "attention
   (2014) + removal of recurrence (2017), only work as a pair" point is made in the 2017 section, then
   made *again* as its own section with bullets. It's the cleanest idea in the piece, but stating it
   twice in a row dilutes it. The second section's real new content is the parallelism→GPU→scaling
   chain; consider folding the redundant "two findings" restatement and leading that section straight
   into scaling.

7. **The closing "urок" over-reaches into aphorism the body only half-supports.** — line 110. — `Мы
   привыкли искать большой сдвиг там, где что-то громко добавили и звонко назвали. А он часто в
   обратном — в том, что кто-то решился убрать лишнее.` This is a satisfying turn, but the piece's own
   2017 section (lines 48–57) spends a paragraph showing Vaswani *added* a careful assembly of borrowed
   parts (ResNet, layer norm, Adam, multi-head). So the lesson "the real shift is removal, not addition"
   is contradicted by the text's own richer story ("removal of the engine + assembly of proven bricks").
   The aphorism flattens the better, truer point the piece already made. Either narrow the claim ("иногда
   сдвиг — в том, чтобы убрать...") or don't universalize it into "как вообще двигаются технологии."

## Minor / polish

- **Line 84 "восемь лет спустя" vs title/frame "двенадцать лет"** — see #3; also a reader may briefly
  conflate the two intervals (idea = 12, architecture = 8/9). Worth one clause distinguishing them.
- **"[Луонг]... довёл его до ума"** (line 51) — mild over-claim; Luong offered variants, "довёл до ума"
  implies Bahdanau's was unfinished. Low stakes but a specialist will wince.
- **The «Для тех, кто хочет глубже» aside (line 80)** is well-placed and correctly quarantined — but it's
  dense (QKV, √d, softmax gradients, O(n²), multi-head) all in one block. Altitude is fine *because* it's
  fenced off; no change needed, just confirming it earns its place. It does.
- **"семеро его коллег" / "Ашиш Васвани и семеро"** (line 48) — fine, but note the paper's "equal
  contribution" footnote means singling out Vaswani as lead is a known sensitivity. The piece handles
  it lightly enough; acceptable.

## What works (briefly)

- The lead earns the read: line 5 blockquote + lines 7–13 land the thesis (2014 idea → ChatGPT) inside
  20 seconds. Thesis is clear.
- The "переполненная ячейка / бутылочное горлышко" metaphor (21–25, 31) is genuinely good and carries a
  non-engineer through the hardest concept without a formula.
- The honesty boundary the brief demanded is *substantively* intact: line 44 explicitly says 2014 was
  "надстройкой поверх старого устройства" and did NOT solve slowness; line 104 keeps Mamba to niches and
  keeps the throne with attention. The frontier-is-still-attention hedge (line 102) is honest in
  substance — it just has a `[проверить]` scar on it.
- The two-findings-in-a-pair framing (67–70) is the correct, non-hype way to explain the shift.

## Verdict: REVISE

Not SHIP: the 11 inline `[проверить]` markers alone block it (#1), and the date-inevitability framing
(#2) plus the 8-vs-9-years arithmetic (#3) are honesty/credibility issues a sharp reader catches fast.
None require rewriting the piece — they're a cleanup pass plus three calibration edits. The spine, the
metaphors, and the honesty boundary are solid; this is a strong draft with visible scaffolding still
attached.

substance_fraction: ~0.85 (7 of 8 numbered findings are substance; the marker cleanup is mechanical but
genuinely ship-blocking, not a nitpick)

one-line: Strip every `[проверить]` from the body (confirm or cut the claim under each), then soften
"дата бьёт сама" and fix the 8-vs-9-years arithmetic — after that it ships.
