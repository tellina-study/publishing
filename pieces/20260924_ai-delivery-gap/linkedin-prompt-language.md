# LinkedIn — самостоятельный пост: формулировка важна, язык почти нет

Не анонс статьи. Ось — мысль владельца: формулировка и структура описания задачи влияют сильно,
но это влияние почти не зависит от языка; между языками расходятся **предпочтения**, а не
понимание и не результат.

Постит Макс со своего профиля. Ниже — готовый текст, копипастить целиком.
Трасса по LLM-стороне: `tasks/20260923_sdlc-ai-pitfalls/materials/prompt-language-structure.md`.

---

## RU — готово к копипасте

Как сформулирована задача — важно. На каком языке — почти нет.

Между языками расходится вкус, а не понимание. Это проверяли прямым опытом, причём на людях, а не на моделях.

Qian Li и коллеги из Университета Твенте дали читателям один и тот же текст про холодильники в двух вариантах: сначала аргументы, вывод в конце — или вывод сразу, аргументы за ним. Три группы: китайцы в Китае, китайцы в Нидерландах, западные читатели. Смотрели, сколько человек читал, что запомнил и как оценил текст.

От порядка изложения не сдвинулись ни время чтения, ни припоминание: во всех шести условиях люди отвечали правильно примерно на шесть вопросов из восьми. А оценки разошлись — китайские читатели назвали текст с выводом в конце и более понятным, и более убедительным; западные между вариантами разницы не увидели. Формулировка авторов: привычный способ раскладывать текст не влияет на способность прочесть и понять его, но может влиять на мнение о нём.

👀 В соседнем их опыте (инструкция к Excel, 127 человек) задачи выполнили одинаково при обеих раскладках — а глаза двигались иначе: китайские участники меньше смотрели в оглавление и заголовки, больше — на картинки.

Структура при этом не безделица. Chen и соавторы (ICML 2024) переставили посылки в задаче на рассуждение — ни одного нового факта, только другой порядок — и качество упало больше чем на 30%. Только настраивается этот порядок под модель, а не под язык. Языкозависимым оказывается регистр: кросс-языковая работа про вежливость нашла, что оптимальный уровень вежливости в английском, китайском и японском разный. Правда, у самой сильной модели в той выборке оптимум был один и тот же во всех трёх языках — ярко языковым это выходило у моделей послабее. И работ про вежливость уже четыре, с четырьмя разными ответами.

Чего нет совсем: структурные эффекты никто не воспроизводил на русском. Прямых сравнений «русский против английского» просто не существует — мы переносим по аналогии и честно это говорим.

Язык дольше всего держит социальный слой: что считается вежливым, что приятно читать. Логика ломается от перестановки абзацев одинаково у всех.

🔗 https://journals.sagepub.com/doi/10.1177/1050651920932192

Когда вас в последний раз раздражал текст, который вы при этом прекрасно поняли?

#PromptEngineering #LLM #AI #TechnicalCommunication

---

## EN — готово к копипасте

How a task is worded matters. What language it's worded in — barely.

What splits between languages is taste, not understanding. It has been tested directly — on people, not models.

Qian Li and colleagues at the University of Twente gave readers the same text about refrigerators in two versions: arguments first and the recommendation at the end, or the recommendation first. Three groups — Chinese living in China, Chinese living in the Netherlands, Westerners. They tracked reading time, recall, and what readers thought of the text.

The order moved neither reading time nor recall: in all six conditions people got about six of the eight content questions right. The ratings moved. Chinese readers called the version with the recommendation at the end both easier to read and more convincing; Westerners saw no difference between the two. The authors' own wording: a culturally preferred way of organizing a text does not affect readers' ability to read and understand it, but it may affect their opinion of it.

👀 In their other experiment (an Excel manual, 127 people) people did the tasks just as well under either structure — but their eyes moved differently: the Chinese participants spent less time on the table of contents and headings, more on the pictures.

None of which makes structure a small thing. Chen et al. (ICML 2024) permuted the premises in a reasoning problem — no new facts, just a different order — and performance dropped by over 30%. You tune that order to the model, though, not to the language. Register is the part that is language-dependent: a cross-lingual study of politeness found the best politeness level differs across English, Chinese and Japanese. Although the strongest model in that set landed on the same level in all three languages — the vivid language effect showed up in the weaker ones. And politeness now has four papers with four different answers.

What is missing entirely: nobody has reproduced the structural effects in Russian. No direct "Russian vs English" comparison exists — we carry the findings over by analogy and say so.

Language holds on to the social layer longest: what counts as polite, what is pleasant to read. Reshuffle the paragraphs and the logic breaks the same for everyone.

🔗 https://journals.sagepub.com/doi/10.1177/1050651920932192

When did a text last annoy you even though you understood every word of it?

#PromptEngineering #LLM #AI #TechnicalCommunication

---

## Первый комментарий (опционально — если Макс решит убрать ссылку из тела)

**RU:** Работы: читатели и структура текста — https://journals.sagepub.com/doi/10.1177/1050651920932192 ·
инструкция к Excel и айтрекинг — Technical Communication 68(1), 2021 ·
порядок посылок у LLM — https://arxiv.org/abs/2402.08939 ·
вежливость по языкам — https://arxiv.org/abs/2402.14531

**EN:** The papers: readers and text structure — https://journals.sagepub.com/doi/10.1177/1050651920932192 ·
the Excel manual with eye-tracking — Technical Communication 68(1), 2021 ·
premise order in LLMs — https://arxiv.org/abs/2402.08939 ·
politeness across languages — https://arxiv.org/abs/2402.14531

---

## Что проверено своими руками, а что нет (2026-10-02)

**Verified this run (резолвнуто в этот прогон).**

- **Абстракт Li, Karreman, de Jong (JBTC 2020)** — дословно, через репозиторий Твенте
  (research.utwente.nl, запись публикации; сам SAGE отдаёт 403). Подтверждено: план 2×3,
  независимые переменные — структура текста (индуктивная/дедуктивная) × культурный фон
  (китайцы в Китае, китайцы в Нидерландах, западные читатели); зависимые — **припоминание,
  время чтения, мнения о тексте**; выходные данные — JBTC **34(4), 335–363, 2020**. Фраза
  владельца подтверждена дословно: «culturally preferred organizing principles do not affect
  readers' ability to read and understand texts but that these principles might affect their
  opinions about the texts»; и «Chinese readers rated readability and persuasiveness higher
  when the text was structured inductively whereas Western readers rated these aspects equally
  high».
- **Результаты того же опыта в деталях** — из диссертации Qian Li (ris.utwente.nl,
  `Thesis_Q_Li.pdf`, глава 6; тот же эксперимент): «No effect of text structure on reading
  time was found»; по припоминанию — «no main effects of the participants' cultural background
  and of text structure, nor an interaction effect», и во всех шести условиях «about six out
  of eight questions about the text content correctly». Отсюда цифра «шесть из восьми» в посте.
- **Соседняя работа — она же и есть источник исхода «выполнение задачи».** Li, de Jong,
  Karreman, «Cultural Differences and the Structure of User Instructions», **Technical
  Communication 68(1), февраль 2021** — PDF опубликованной статьи прочитан целиком
  (ris.utwente.nl). Дословно: «A 3x2 randomized experiment (**N = 127**)»; зависимые
  переменные — **task performance, user satisfaction, information selection**; «Regarding task
  performance and user satisfaction, **no significant main and interaction effects** were
  found»; «Chinese users pay less attention to structuring elements (table of contents and
  headings) and more attention to visuals». Айтрекинг — оттуда же.
- **Chen, Chi, Wang, Zhou, «Premise Order Matters in Reasoning with Large Language Models»,
  ICML 2024** (arXiv:2402.08939) — абстракт резолвнут независимо от трассы; «permuting the
  premise order can cause a performance drop of over 30%» — дословно.
- **Yin, Wang, Horio, Kawahara, Sekine (arXiv:2402.14531)** — абстракт резолвнут независимо;
  «The best politeness level is different according to the language» — дословно.

**Не подтвердилось / не поставлено в текст.**

- **«Около 365 участников» — НЕ ПОДТВЕРЖДАЕТСЯ.** Числа 365 нет ни в абстракте, ни в главе
  диссертации по этому опыту; в самой диссертации «365» встречается только как номер страницы
  в списке литературы. В посте никакого числа участников нет — сознательно.
- **Сколько участников было на самом деле.** В версии этого опыта из диссертации — **158**
  человек (49 западных + 55 китайцев в Нидерландах + 54 китайца в Китае; по припоминанию
  29+25+32+23+24+25 = 158). Число в **опубликованной** версии JBTC я подтвердить не смог:
  SAGE отдаёт 403 и на HTML, и на PDF. Почему это не мелочь: у соседнего, Excel-опыта тех же
  авторов выборка между диссертацией и печатью изменилась (**158 → N = 127**, видимо отсев по
  айтрекингу). Поэтому «158» в пост не ставлю, а 127 ставлю — оно из самой опубликованной
  статьи.
- **Исход «выполнение задачи» — не из той работы, на которую ссылается пост.** Он из
  Technical Communication 2021 (инструкция к Excel), а не из JBTC 2020 (описание холодильника,
  там припоминание / время чтения / мнения). В посте они разведены: ссылка в теле ведёт на
  JBTC 2020, Excel-опыт назван отдельным предложением как «соседний».
- **Разрыв «лучший−худший уровень вежливости» (0,9–5,2 п.п. у GPT-4) и оптимум на уровне 4 во
  всех трёх языках** — это арифметика нашей трассы по Table 1 работы, а не утверждение авторов.
  Поэтому в посте только качественно: «у самой сильной модели в той выборке оптимум был один и
  тот же». Сами авторы пишут рядом: «in advanced models, the politeness level of the prompt may
  have a lesser impact on model performance».
- **«Четыре работы с четырьмя разными ответами» про вежливость** — из нашей трассы
  (2402.14531, 2510.04950, 2604.16275, 2512.12812), сам в этот прогон перепроверил только
  первую. Поэтому в посте это подано как «ответы разные», без выбора одного.
- **«Структурные эффекты никто не воспроизводил на русском»** — отсутствие, а не находка;
  опирается на GAPS трассы (§7.1–7.2). В посте названо вслух как дыра, а не как вывод.
- **Сильное отрицание нигде не утверждается.** «Порядок не влияет» в тексте нет; наоборот,
  стоит «+30% падения от перестановки» и формулировка «настраивается под модель, а не под язык».

## Что внутри поста и почему (ШАГ 0)

| Элемент | Что взято |
|---|---|
| Первая строка | Мысль владельца в лоб, двумя короткими фразами: формулировка важна, язык — почти нет |
| Вторая строка | То, что расходится — вкус, а не понимание; и сразу: проверяли на людях |
| Доказательство | Твенте: один текст в двух сборках × три группы; источник назван до цифры |
| Цифра | «Шесть из восьми во всех шести условиях» — припоминание не поехало от порядка |
| Айтрекинг | Соседний опыт: результат одинаков, а глаза ходят по-разному — предпочтение видно физически |
| Что на моделях | Порядок посылок: >30% (ICML 2024); настраивается под модель, не под язык |
| Оговорка | У сильной модели языковой разрыв по вежливости почти исчез; работ четыре, ответы разные |
| Дыра | На русском структурные эффекты не воспроизводились — сказано вслух |
| Философия | Язык держит социальный слой дольше логического — без пафоса, одной строкой |
| Закрытие | Живой вопрос про текст, который понял, но он бесит (ровно расхождение «мнение ≠ понимание») |
| Эмодзи | Два разных (👀 🔗), не столбик одинаковых маркеров |
| Длина | RU ~300 слов, EN ~330 |
