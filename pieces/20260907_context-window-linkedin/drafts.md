<!-- Channel: LinkedIn (EN). Announce of Lecture 2 "How Modern Large Models Work" —
     https://lessons.tellian.io/en/lectures/lec-02/
     Angle (Max): the U-curve ("lost in the middle") no longer holds, but the context-WINDOW
     problem remains. Source = lec-02 slides 26–27 (owner's own material).
     Canon: blueprint/channels/linkedin.md. Simple language, hook first, CTA без «if». -->

# LinkedIn — лекция 2, контекстное окно. Пост

## ✅ PUBLISHED 2026-09-07
https://www.linkedin.com/feed/update/urn:li:share:7502683319256580097/
Опубликованная версия — раунд 8 (голос Макса: 🎉→🤷‍♂️ двумя ударами; грамматика вычищена). Точная
формулировка Congrats/Congratz и Bench/benchmark — на усмотрение Макса при постинге.

> Stop shortening your prompts to protect facts — but keep them short to protect reasoning.
>
> Congrats 🎉! The old problem — models "losing the middle" of a long input — is solved. Top models now find a fact anywhere in a million-token window about 99% of the time.
>
> But there's a nuance 🤷‍♂️. Finding a fact and reasoning across a long text are two different things. The second still breaks. Ask the model to connect facts across a long context, not just look them up, and it gets worse fast.
>
> The NoLiMa benchmark (Long-Context Evaluation Beyond Literal Matching) sees most models fall below half their accuracy by 32,000 tokens — well before the window is full.
>
> So now don't worry about where a fact sits. Worry about how much you ask the model to reason over at once. A bigger window lets it read more, not think more.
>
> I get into this in my lecture on how modern models actually work — what a context window really gives you, and what it doesn't.
>
> 👉 https://lessons.tellian.io/en/lectures/lec-02/
>
> Where do you still trust a model across a long context, and where do you split it up? (раунд 2 — регистр Макса: полезный совет, не «гоча»)

## POST (основной, раунд 7 — название статьи в тексте, ссылка только на лекцию)

You can stop keeping your prompts short to protect facts. You still need to keep them short to protect reasoning.

The old problem — models "losing the middle" of a long input — is mostly solved. Top models now find a fact anywhere in a million-token window about 99% of the time.

But finding a fact and reasoning across a long text are two different things. The second still breaks. Ask the model to connect facts across a long context, not just look them up, and it gets worse fast. A benchmark built for this — NoLiMa: Long-Context Evaluation Beyond Literal Matching — sees most models fall below half their accuracy by 32,000 tokens, well before the window is full.

So don't worry about where a fact sits. Worry about how much you ask the model to reason over at once. A bigger window lets it read more, not think more.

I get into this in my lecture on how modern models actually work — what a context window really gives you, and what it doesn't.

👉 https://lessons.tellian.io/en/lectures/lec-02/

Where do you still trust a model across a long context, and where do you split it up?

---

## Альтернативные первые строки (грабы)
1. Quietly, one of the classic LLM limits got solved this year — and a lot of teams are still building around it.
2. Stop rationing your context to dodge the "lost in the middle" problem. It's basically gone. Here's what to watch instead.
3. That habit of putting the important stuff at the top or bottom of a long prompt? You don't need it anymore. But don't celebrate yet.

---

## Заметки
- Раунд 3 по правке Макса (2026-09-07): хук должен цеплять профи, который **пропустил новость** —
  назвать его устаревшую практику («ты всё ещё держишь контекст коротким») → выдать новость +
  **конкретную цифру как пруф** (99% / 1M — это «поверил автору», не «гоча»: цифра успокаивающая,
  доказывает, что проблема решена) → полезный разворот (что осталось: рассуждение поперёк, не поиск).
  Польза: «перестань беспокоиться, ГДЕ факт; беспокойся, СКОЛЬКО просишь связать за раз».
- Факт-якоря (lec-02): 99% needle @ 1M решено; NoLiMa — 11/13 ниже половины уже на 32k; window ≠
  effective length. В теле оставлена только 99% (пруф-цифра); NoLiMa свёрнута в «starts early / before
  the window is full», чтобы не грузить бенчмарками. Вернуть 32k при желании — как якорь достоверности.

## Факт-якоря (lec-02, слайды 26–27 — материал Макса)
- Буквальный needle-in-haystack: до 99% на полном окне 1M токенов (флагманы). U-кривая на простом
  поиске — снята.
- NoLiMa (поиск БЕЗ лексического совпадения, нужен вывод): 11 из 13 моделей ниже половины своей
  короткой точности, уже на 32 000 токенов.
- «Окно ≠ длина рассуждения»: advertised window (сколько модель читает) ≫ effective length
  (на скольких токенах ещё связывает факты).
- ⚠️ Facts принадлежат лекции (первоисточник поста). NoLiMa — реальный бенчмарк 2025; при желании
  вынести цифру в самостоятельный пост — прогнать fact-checker на первоисточник NoLiMa.
