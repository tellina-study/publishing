# Reader reaction: 20260620_prompting-recommendations  (channel: blog)

## First bounce point
- I made it through, but the **first real wobble is the "Праймер" section** (line 22-30). Three
  terms land almost at once: "Аллокация токенизатора", "BPE", "fertility". BPE is dropped with zero
  gloss — I have no idea what it is, just that it "режет текст на токены". "Fertility" gets a
  parenthetical ("среднее число токенов на слово") which saved me — good. But "BPE" is the cold spot:
  a normal reader doesn't know it's "byte-pair encoding," and even spelled out it wouldn't mean much.
- Second wobble: **"харнесс / harness"** (line 52, 67). The header "английский харнесс" hits before
  the term is really anchored. It IS defined on line 52 ("Агентный harness — постоянный слой...
  инструкции, скилы, тул-дефиниции, память"), but that definition is itself dense — "скилы",
  "тул-дефиниции" are jargon-on-jargon. For a pure ChatGPT user this is the paragraph where I start
  feeling "oh, this isn't really for me."
- Acronyms that flash by without expansion in the body: **MoE** (line 211 — "MoE-роутингу", never
  unpacked), **MECW** (only appears in the Sources list line 293 as a label, never in the body — so
  if I went looking for what MECW means I'd find nothing). **RAG** (line 53) is also unglossed.
- "Caveman / пещерный" — actually handled WELL. It's translated, quoted, and explained on first use
  (line 10, then line 100). No bounce there.

## Hook
- The blockquote opener (lines 3-16) earns the click. Three concrete questions I've genuinely
  wondered ("does the language matter," "do I need tags," "where do I put the question?") plus the
  promise that "half the clever advice fails the test." That's a good hook — it's curiosity + a
  debunking promise. The bulleted "Коротко — что выяснили" is almost TOO complete; it kind of
  gives away the whole article up front, so my reason to read on becomes "show me the proof," not
  "tell me the answer." That's fine for a reference piece, less gripping as a narrative.
- The author's "Я пакую большие инструкции каждый день" (line 18) is a good credibility beat —
  real products named — but w4check / mentor / "свой курс" mean nothing to me as a stranger; it
  reads slightly like self-promo. Doesn't hurt much.

## Where it gripped / dragged
- **Gripped:** the myth-busting beats. "Китайский на 40% дешевле — нет" (line 36), "−75% caveman
  на самом деле ~15-20%" (line 104-111), "эмодзи занимают больше места, чем экономят" (line 11/176).
  These are crisp, surprising, and satisfying — the payoff the hook promised.
- **Gripped:** "Кстати, эта статья сама собрана по этому принципу" (line 44, repeated line 283).
  The self-referential "the middle is skippable, and I built this article that way" is charming and
  memorable — it made me trust the author and smile.
- **Gripped:** the dedicated box "Для тех, кто просто пользуется чат-ботом" (lines 217-224). This is
  the single best thing for a non-engineer like me — four plain rules, no jargon. Honestly I wish it
  were near the TOP, because by the time I reached it (~85% through) I'd already half-checked out
  during the engineering middle.
- **Dragged / skimmed:** the citation density. Almost every sentence in the primer and in Приёмы 1-4
  carries a bracketed arXiv link with a date and a stat. By the third "[Работа (2026)](...) показывает,
  что..." I started skimming the citations and just reading the bolded takeaways. It reads more like
  a literature review than a blog post in places.
- **Dragged hard for me as a non-engineer:** Приём 3 (формат: YAML/JSON/XML/TOON, lines 123-143) and
  "Как работают разные модели" (lines 200-213). TOON, MoE-routing, kv-cache "статику вверх", tool
  definitions — I skimmed all of it. It's clearly competent, but it's a different reader's section.
- The **mid-section "Сколько из этого — реальность"** (lines 192-196) is actually a highlight of
  honesty, but it arrives late and is abstract ("log-likelihood", "LLM-судья") — I half-skimmed.

## My one-sentence takeaway
- "Write your prompt in whatever language you think in, put the actual question at the END (especially
  after a long pasted text), don't bother with emoji/fancy formatting, and ask it to be brief —
  everything fancier is for people building AI systems, not me."
- (I CAN form it — but note: my one sentence is basically the "for casual users" box, not the article's
  main body. The 80% of the article aimed at prompt engineers I could not compress, and wouldn't try.)

## Share / read-on? meh — 
- As a casual chatbot user: I'd save it, maybe screenshot the casual-user box, but I wouldn't read it
  end-to-end again, and I'm not sure I'd share it — too long and too engineer-heavy for most friends
  who "just use ChatGPT." The dual-audience promise only half works: the casual reader is technically
  served (one box + the summary bullets), but the body, the primer, and two whole sections are
  unmistakably for engineers, and a normal user starts feeling like a tourist around the "harness /
  tool-definitions / MoE" material. If I built with AI, this jumps to a clear "yes, bookmark and
  share" — the master table, decision rules and pre-send checklist are genuinely useful reference.
- Fix that would move me from meh to yes (as a casual reader): pull the "для тех, кто просто
  пользуется" box up near the top and tell me explicitly "casual user? read this box and stop;
  the rest is for builders." Right now I have to wade through engineer-land to discover the part
  meant for me was at the back.
