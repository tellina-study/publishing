# Reader reaction: prompting-recommendations  (channel: blog)

## The opening
Reads like a real person, not a marketer — and that's a relief. The first paragraph
opens on concrete annoyances ("правда ли «пещерный» промпт экономит 75%?", "китайский
дешевле — миф?") and a believable motive ("работаю с большими промптами каждый день,
гадать надоело — сел и перепроверил"). That "I got tired of guessing so I checked"
energy is exactly what makes me want to read on. It promises *findings*, not a lecture.
Good hook. I kept going.

One small snag: "Вышло небольшое исследование, из которого и собралась эта статья" is
the one phrase that drifts toward self-presentation. It's mild, but it's the first whiff
of "look what I produced" rather than "here's what I found."

## First bounce point
The summary itself is fine, but the very next block — "Праймер: почему язык, форма и
место стоят денег" with BPE / fertility / "аллокация токенизатора" — is where a casual
chatbot user (someone who just uses ChatGPT) would slow down hard. As a builder I'm fine;
as a pure "I just type into ChatGPT" reader, paragraph 24–28 is the first place I'd think
"this got technical fast, is the rest for me?" The intro promised practical, the primer
delivers a tokenizer lecture. Not a hard bounce, but the first wobble.

## Does the 💬/⚙️/🤖 per-point tagging work?
Mostly yes — and I prefer it to a separate "for you" box. The legend in line 5 ("💬 чат ·
⚙️ системный промпт · 🤖 агент") is clear, and each bullet then tells me directly. As a
casual user I can scan for 💬 and the italic asides actually speak to *me* in plain terms:
"в чате просто пишите как удобно", "вопрос в конец, если выше длинный текст". That's the
best part — the casual-user advice is spelled out, not just tagged.

Where it half-works: the tags tell me a point is "for chat," but several of those same
points then say "в чате это не критично" / "незачем" (Форма, Сжатие). So the honest signal
is "skip most of this if you're casual" — which is useful, but it also quietly tells a
casual reader that only ~2 of the 6 bullets really matter for them. That's fine if I'm
honest with myself, but a casual reader might feel the article isn't really aimed at them
after all. I didn't feel *lost* without a dedicated box — the per-point tags carried it.

Tiny thing: the legend uses 💬⚙️🤖 but bullets also introduce 🌐📍🧱✂️🔣🪜 as topic icons.
Two icon systems in one list. I worked it out, but for half a second I wondered if 🌐 was
also an audience tag.

## Where it gripped / dragged
- Gripped: the myth-busting framing throughout — "китайский дешевле — миф", "−75% это
  лучший случай по выходу, реально ~15–20%", "русский в 2–2,5 раза дороже". Concrete,
  surprising, debunk-y. The "Сработало / Отбросили" section near the end is the single
  most shareable chunk — it's the whole article as a cheat sheet.
- Gripped: the two "из практики" callouts (структура окупается дважды; пример бьёт запрет).
  Those feel earned and human, not showy.
- Dragged: the middle "Приём 1–5" sections are dense with bracketed citations — sometimes
  3–5 arxiv links in one paragraph (line 40, line 32). As a casual reader I skimmed those
  hard; they read like a literature review. A builder will mine them; a casual user glazes.
- Dragged: "Как работают разные модели" — useful for builders, pure skim for everyone else.

## Lecturing / showing off?
- Line 32 and line 40 are the densest — back-to-back citations start to feel like
  "look how much I read" rather than "here's the point." Not arrogant, just heavy.
- The repeated meta-notes that the article *itself* follows its own rules (lines 42, 191,
  280, "Середину можно пролистать") are charming the first time and slightly self-satisfied
  by the third. One would land better than three.
- Otherwise the tone stays collegial — lots of "честно", "не спешите", "не закладывайтесь",
  hedging on single studies. That honesty is the opposite of showing off and it's the
  article's biggest trust-builder.

## My one-sentence takeaway
Where you put the important stuff (edges, not middle) and how you format it matter more
than what language you write in — and "tricks" like caveman/Chinese/emoji save far less
than the hype, so optimize placement and format first and compression last.

## Share / read-on? yes — for the right person
yes, but qualified: I'd share it with a colleague who builds prompts/agents in a heartbeat —
it's a genuinely useful, sourced, myth-busting reference, and the final tables + decision
rules are keeper material. For a purely casual ChatGPT user I'd send only the intro summary
and the "Отбросили" list, because the body is heavier than they need. I'd follow the author
for more. The honesty ("verify big reproduced effects, not viral percentages") is what would
make me trust the next piece.
