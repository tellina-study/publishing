# LinkedIn — самостоятельный пост: структура не зависит от языка

Не анонс статьи. Ось — мысль владельца, дословно:

> **Восхищение в том, что структура не зависит от языка — при том что язык считается
> фундаментальным свойством, которое определяет в том числе сознание человека.**

Философы (Выготский, Витгенштейн, Сепир–Уорф, Хайдеггер) стоят в посте как **ожидание**, которое
проверяется, а не как доказательство: сильная версия языковой относительности в науке не принята,
слабая подтверждена частично — это сказано в самом тексте. Измерения служат мысли: чисел в посте
четыре, не больше. Финал — вопрос без готового ответа.

Речь о **языковых моделях**, не о людях; границу пост называет вслух. Два прежних варианта
(технический и «про людей») забракованы владельцем и лежат ниже с разбором, чем именно плохи.

Постит Макс со своего профиля. Ниже — готовый текст, копипастить целиком.
Источники: `notes/research/student-questions/prompt-language/` (файлы `00`, `07`, `08`, `10`) в
воркспейсе исследования #216. Полная сверка числа-к-источнику — в блоке «ЗАБРАКОВАН №2» ниже,
она не переписывалась: числа те же, роль у них другая.

---

## RU — готово к копипасте

Как лучше разложить задачу для модели — от языка не зависит. Пребываю в лёгком шоке: язык ведь считается тем, что формирует само мышление.

Сто лет об этом и говорят. Выготский: речь не упаковывает готовую мысль, она перестраивает мышление. Витгенштейн: границы моего языка — границы моего мира. Гипотеза Сепира–Уорфа. Хайдеггер с языком как домом бытия. Сильную версию этой идеи наука, впрочем, не приняла, слабую подтвердила частично. Так что это не доказательство, а ожидание.

И если язык правда так работает, то у модели, выученной на текстах, удачная раскладка задачи должна меняться вместе с языком. Меняться тут есть чему: Lu и коллеги (ACL 2022) переставили в промпте одни и те же четыре примера, больше ничего не трогали — точность упала с «выше 85%» до «около 50%». С обученной модели до монетки.

Не меняется. Факториальный тест на переводе газетных статей — четыре типа промпта × три языка промпта, GPT-5.2: «prompt language had a negligible impact». Menschikov и коллеги проверили позиционное смещение на пяти типологически разных языках, включая русский: оно «primarily model-driven», а гипотезу про порядок слов авторы отвергли сами.

🧪 Ну и чем ещё в пятницу заняться — прогнал сам. 176 вызовов, четыре порядка блоков × два языка. Лучший порядок вышел один и тот же в русском и английском. И тут же его цена: три прогона одной и той же комбинации на неизменном промпте дали 13, 10 и 12 из 16. Значит разницу меньше трёх заданий читать нельзя вообще, а мой замер — пилот, не доказательство.

🙇 А вот что по языкам действительно расходится — вежливость. Насколько вежливо попросить: в английском, китайском и японском оптимум разный — правда, у модели посильнее он сошёлся для всех трёх. Выходит, в языке уцелел социальный слой, а не логический.

Это про раскладку задачи для модели, не про человеческое мышление. Философов тут никто не опроверг.

Но вопрос остался. Это говорит что-то про модели — или про сам язык? Либо структура задачи лежит глубже языка. Либо модель выучила общее ядро и отбросила ровно то, чем языки друг от друга отличаются. Ответа у меня нет.

🔗 https://arxiv.org/abs/2505.16134

#LLM #AI #Language #Linguistics

---

## EN — готово к копипасте

How best to lay out a task for a model doesn't depend on the language you write it in. Which leaves me mildly stunned: language is supposed to be the thing that shapes thought itself.

A century of thinking says so. Vygotsky: speech doesn't package a finished thought, it rebuilds thinking. Wittgenstein: the limits of my language are the limits of my world. Sapir–Whorf. Heidegger, language as the house of being. Science never accepted the strong version of that idea; the weak one it partly confirmed. So this isn't proof. It's an expectation.

And if language really works that way, then for a model raised on text the best layout of a task should move when the language moves. There is something here to move: Lu and colleagues (ACL 2022) reordered the same four examples in a prompt and touched nothing else — accuracy fell from above 85% to about 50%. From trained model to coin flip.

It doesn't move. A factorial test on newspaper translation — four prompt types × three prompt languages, GPT-5.2: "prompt language had a negligible impact." Menschikov and colleagues checked position bias across five typologically different languages, Russian among them: it is "primarily model-driven," and they threw out the word-order hypothesis themselves.

🧪 And what else is a Friday for — I ran it myself. 176 calls, four block orders × two languages. The best order came out the same in Russian and English. And right away what that is worth: three runs of one combination, same prompt, gave 13, 10 and 12 out of 16. So anything under three tasks can't be read at all, and my run is a pilot, not proof.

🙇 What does split by language is politeness. How politely you ask has a different optimum in English, Chinese and Japanese — though on a stronger model even that converged into one. So what the language kept is its social layer, not its logical one.

This is about laying out a task for a model, not about human thought. Nobody here refuted the philosophers.

The question stays, though. Does this say something about models, or about language itself? Either the structure of a task sits deeper than language — or the model learned the common core and dropped exactly what makes languages differ from each other. I don't have the answer.

🔗 https://arxiv.org/abs/2505.16134

#LLM #AI #Language #Linguistics

---

## Первый комментарий (ссылки — если Макс решит убрать ссылку из тела)

**RU:** Работы по порядку: порядок few-shot примеров — arxiv.org/abs/2104.08786 ·
факториальный тест «структура × язык промпта» — arxiv.org/abs/2607.03160 ·
позиционное смещение на 5 языках, включая русский — arxiv.org/abs/2505.16134 ·
вежливость по языкам — arxiv.org/abs/2402.14531 (и два более свежих замера, которые с ней
не сходятся: arxiv.org/abs/2604.16275, arxiv.org/abs/2512.12812).

**EN:** The papers, in order: few-shot example order — arxiv.org/abs/2104.08786 ·
the factorial structure × prompt-language test — arxiv.org/abs/2607.03160 ·
position bias across 5 languages incl. Russian — arxiv.org/abs/2505.16134 ·
politeness across languages — arxiv.org/abs/2402.14531 (plus two later measurements that
disagree with it: arxiv.org/abs/2604.16275, arxiv.org/abs/2512.12812).

---

## Где прежний вариант подменил мысль техникой (ШАГ 0, разбор перед переписыванием)

Владелец: «ты оскопил и высушил мою мысль, перевёл её в какую-то технику». Конкретно, по местам:

| Место | Что было | Почему это техника, а не мысль |
|---|---|---|
| Первая строка | «Anthropic, OpenAI и Google по-разному отвечают, куда класть большой блок данных» | Хук про расхождение вендорских гайдов. Он обещает читателю пост о промпт-инжиниринге — и пост его выполняет. Мысль владельца в тексте не появляется **ни разу** |
| Рамка | отсутствует | Нет ожидания — значит нечему и рухнуть. «Язык не влияет» без «язык считается тем, что определяет мышление» — это нулевой результат в отчёте, а не поворот |
| Философы | нет ни одного | Удивление владельца держится ровно на них. Без Выготского и Витгенштейна «ноль по языку» — техническая деталь |
| Числа | ~10 штук: 85%→50%, 7,5 п.п., >70 п.п., +12/+5/−23, 14/16, 11/16, 9/16, 10/16, 176, 13/10/12 | Доказательство заняло место содержания. Три абзаца подряд — колонка цифр; мысли между ними нет |
| «Социальный слой» | одна строка **только в забракованном варианте про людей**, в техническом её нет вовсе | Это вторая половина мысли (уцелело социальное, не логическое) — и она была выброшена |
| Финал | «Куда вы кладёте большой блок данных — до инструкции или после? И откуда знаете, что так лучше?» | Вопрос-анкета по технике. Закрывает тему вместо того, чтобы открыть её |
| Практический вывод | «данные вперёд, инструкцию после» | Совет по промптам. Тема другого поста |

---

## Что внутри нового поста и почему (ШАГ 0)

| Элемент | Что взято |
|---|---|
| Первая строка | Сама мысль, без разбега: раскладка задачи от языка не зависит — и тут же «пребываю в лёгком шоке», потому что язык считается тем, что формирует мышление. Регистр владельца сохранён дословно |
| Рамка | Сто лет мысли: Выготский (речь перестраивает мышление), Витгенштейн (границы языка = границы мира), Сепир–Уорф, Хайдеггер (язык — дом бытия). Названы, но **в роли ожидания**: сразу сказано, что сильную версию наука не приняла, слабую подтвердила частично |
| Переход к проверке | «Если язык правда так работает, то у модели раскладка должна меняться вместе с языком» — ожидание становится проверяемым |
| Единственная оставленная техника | Lu et al.: те же четыре примера в другом порядке, >85% → ~50%. Одной строкой, и строго ради одного — показать, что меняться **чему есть**. Без неё «не меняется» ничего не стоит |
| Поворот | «Не меняется», отдельным абзацем из двух слов. Факториальный тест 4×3 на GPT-5.2 («negligible impact») + позиционное смещение «primarily model-driven» на пяти языках, включая русский, с отвергнутой самими авторами гипотезой про порядок слов |
| Своё | 176 вызовов, четыре порядка × два языка, лучший порядок один и тот же — и в том же абзаце его цена: 13/10/12 из 16 на неизменном промпте, меньше трёх заданий читать нельзя, это пилот. Ограничение не вынесено в сноску и не отложено |
| Вторая половина мысли | Вежливость — единственное языкозависимое; значит уцелел социальный слой языка, а не логический. Это не оговорка в конце, а содержательный шаг |
| Граница честности | «Это про раскладку задачи для модели, не про человеческое мышление. Философов тут никто не опроверг» — ровно то, что делает пост честным |
| Финал | Вопрос без ответа: это про модели или про сам язык? Две развилки названы, выбор не сделан, «ответа у меня нет». Не анкета, аудиторию ни о чём не просят |
| Чего нет | Вендорского расхождения, FormatSpread, PromptPrism (+12/+5/−23), совета «куда класть данные», симметричных буллетов, связок-лесов |
| Эмодзи | Два в теле (🧪 свой прогон, 🙇 вежливость) + 🔗 на ссылку |
| Числа | Четыре: 85%→50% (одна строка), 4×3 «negligible impact», 176 вызовов, 13/10/12 из 16. Процентов про вежливость нет — их не удалось резолвнуть, и без них мысль держится |
| Длина | RU 340 слов / 2153 знака, EN 396 слов / 2314 знаков — внутри лимита 3000 знаков LinkedIn |
| Ссылка в теле | arXiv:2505.16134 (позиционное смещение на пяти языках, включая русский) — работа, ближе всех стоящая к самой мысли. Прежняя ссылка вела на FormatSpread, которого в посте больше нет |

---

# ЗАБРАКОВАН №2: технический вариант — мысль переведена в промпт-инжиниринг

**Чем именно плох:** см. разбор «Где прежний вариант подменил мысль техникой» выше. Текст сохранён
целиком — **сверка числа-к-источнику в нём честная и остаётся рабочей трассой** для нового поста
(числа те же, роль другая).

## LinkedIn — самостоятельный пост: структура промпта важна, язык — почти нет

Не анонс статьи. Ось — мысль владельца: **формулировка и структура описания задачи влияют на
понимание и результат сильно — но это влияние почти не зависит от языка. Между языками
расходятся предпочтения, а не понимание и не результат.**

Речь о **языковых моделях**, не о людях. Версия про людей забракована владельцем и лежит ниже.

Постит Макс со своего профиля. Ниже — готовый текст, копипастить целиком.
Источники: `notes/research/student-questions/prompt-language/` (файлы `00`, `07`, `08`, `10`) в
воркспейсе исследования #216 + `tasks/20260923_sdlc-ai-pitfalls/materials/prompt-language-structure.md`.

---

### RU — готово к копипасте

Anthropic, OpenAI и Google по-разному отвечают, куда в промпте класть большой блок данных. Замер не показывает ни один.

Сама структура при этом — не мелочь. Lu и коллеги (ACL 2022) переставили местами одни и те же четыре примера в промпте, больше ничего не меняли: точность на классификации тональности гуляла от «выше 85%» до «около 50%» — от уровня обученной модели до монетки. Sclar и коллеги прогнали 53 задачи в равнозначных оформлениях — различается только типографика: медианный разброс 7,5 пункта, на отдельных задачах — больше семидесяти.

🔀 Только настраивается это под модель, а не под язык. Jeoung и коллеги из AWS перенесли блок инструкции в конец промпта: +12% у Claude Sonnet 3.5, +5% у Llama 3.2 3b, −23% у Mixtral 8x7b. Один и тот же сдвиг, три разных знака.

А вот язык в этом самом месте измеряли — и вышел ноль. Факториальный тест на переводе газетных статей, четыре типа промпта × три языка промпта, GPT-5.2: «prompt language had a negligible impact». Menschikov и коллеги проверили позиционное смещение на пяти типологически разных языках, включая русский: оно «primarily model-driven», а гипотезу про порядок слов авторы отвергли сами. Там же моя любимая деталь: подсказка «самый релевантный фрагмент помечен как 1» при наличии отвлекающих фрагментов точность не поднимала, а снижала — одинаково во всех пяти языках.

🧪 Мы прогнали это сами: 176 вызовов, четыре порядка блоков × два языка × 16 заданий, парами. Лучший порядок вышел один и тот же в русском и английском. Худший — тот же: большой блок данных после инструкции (в английском он делит последнее место с двумя другими). Единственное, что в этом замере совпало между языками: данные вперёд, инструкцию после.

🎲 И сразу цена этого вывода. Три прогона одной комбинации — тот же язык, тот же порядок, те же задания, тот же промпт: 13 из 16, 10 из 16, 12 из 16. Размах три задания на входе, который не менялся. Значит различие меньше трёх заданий толковать нельзя вообще, а наш замер — пилот, не доказательство. Это ограничение мне дороже самих цифр.

Единственное, что в литературе действительно разошлось по языкам, — вежливость формулировки (английский, китайский, японский). Да и там: у модели посильнее оптимум оказался один для всех трёх, а работ про вежливость уже несколько, и ответы у них не сходятся.

🔗 https://arxiv.org/abs/2310.11324

Куда вы кладёте большой блок данных — до инструкции или после? И откуда знаете, что так лучше?

#PromptEngineering #LLM #AI

---

### EN — готово к копипасте

Anthropic, OpenAI and Google give three different answers to where the big block of data goes in a prompt. None of them shows a measurement.

Structure is no small thing. Lu and colleagues (ACL 2022) reordered the same four examples and changed nothing else: accuracy on a sentiment task swung from above 85% down to about 50% — from trained model to coin flip. Sclar and colleagues ran 53 tasks in layouts that mean the same and differ only in typography: median spread 7.5 points, over seventy on some tasks.

🔀 But you tune that to the model, not the language. Jeoung and colleagues at AWS moved the instruction block to the end: +12% for Claude Sonnet 3.5, +5% for Llama 3.2 3b, −23% for Mixtral 8x7b. Same move, three different signs.

Language, in that same spot, has been measured — and came out zero. A factorial test on newspaper translation, four prompt types × three prompt languages, GPT-5.2: "prompt language had a negligible impact." Menschikov and colleagues checked position bias across five typologically different languages, Russian among them: it is "primarily model-driven," and they threw out the word-order hypothesis themselves. My favourite detail is in that same paper: telling the model "the most relevant passage is marked 1" made accuracy worse once distractors were in play — the same in all five languages.

🧪 We ran it ourselves: 176 calls, four block orders × two languages × 16 tasks, paired. The best order came out the same in Russian and English. So did the worst — the big data block sitting after the instruction (in English it shares last place with two others). The one thing that matched across both: data first, instruction after.

🎲 And straight to what that costs. Three runs of one combination — same language, same order, same tasks, same prompt: 13 of 16, 10 of 16, 12 of 16. Three tasks of spread on an input that never moved. So anything under three tasks can't be read at all, and our run is a pilot, not proof. That limit matters to me more than the numbers.

The one thing the literature did split by language is how politely you phrase it (English, Chinese, Japanese). Even there: the stronger model landed on the same level in all three, and politeness now has several papers that disagree.

🔗 https://arxiv.org/abs/2310.11324

Where do you put the big block of data — before the instruction or after? And how do you know?

#PromptEngineering #LLM #AI

---

### Первый комментарий (ссылки — если Макс решит убрать ссылку из тела)

**RU:** Работы по порядку: порядок few-shot примеров — arxiv.org/abs/2104.08786 ·
разброс по оформлению (FormatSpread) — arxiv.org/abs/2310.11324 ·
порядок блоков промпта по моделям (PromptPrism, AWS) — arxiv.org/abs/2505.12592 ·
факториальный тест «структура × язык промпта» — arxiv.org/abs/2607.03160 ·
позиционное смещение на 5 языках, включая русский — arxiv.org/abs/2505.16134 ·
вежливость по языкам — arxiv.org/abs/2402.14531, arxiv.org/abs/2604.16275,
arxiv.org/abs/2512.12812 · рекомендации вендоров: Anthropic «Long context prompting»,
OpenAI GPT-4.1 Prompting Guide, Google Gemini «Prompt design strategies».

**EN:** The papers, in order: few-shot example order — arxiv.org/abs/2104.08786 ·
format-induced spread (FormatSpread) — arxiv.org/abs/2310.11324 ·
prompt block order across models (PromptPrism, AWS) — arxiv.org/abs/2505.12592 ·
the factorial structure × prompt-language test — arxiv.org/abs/2607.03160 ·
position bias across 5 languages incl. Russian — arxiv.org/abs/2505.16134 ·
politeness across languages — arxiv.org/abs/2402.14531, arxiv.org/abs/2604.16275,
arxiv.org/abs/2512.12812 · vendor guidance: Anthropic "Long context prompting,"
OpenAI GPT-4.1 Prompting Guide, Google Gemini "Prompt design strategies."

---

### Что проверено и откуда (2026-10-03)

Все числа поста — из материалов исследования #216, раунд 2. Ничего не добавлено «по смыслу».

**Структура значима — измерено многократно.**

- **Порядок few-shot примеров.** Lu, Bartolo, Moore, Riedel, Stenetorp, «Fantastically Ordered
  Prompts and Where to Find Them», ACL 2022 (Outstanding Paper), **arXiv:2104.08786**. SST-2,
  GPT-семейство: одни и те же четыре примера, разные перестановки — от **>85%** точности
  (сопоставимо с supervised baseline) до **~50%** (случайное угадывание). Источник: файл `07`,
  строка таблицы #5.
- **Разброс от оформления.** Sclar, Choi, Tsvetkov, Suhr, «Quantifying LMs' Sensitivity to
  Spurious Features in Prompt Design» (FormatSpread), ICLR 2024, **arXiv:2310.11324**. 53 задачи
  Super-NaturalInstructions, 10 случайных форматов на задачу: **медианный спред 7,5 п.п.**,
  отдельные задачи — **спред >70 п.п.**; держится независимо от размера модели и
  instruction-tuning. Файл `07`, строки #1–#3. Это ссылка в теле поста.

**Знак эффекта переключает модель, а не язык.**

- Jeoung et al. (Amazon AWS), «PromptPrism: A Linguistically-Inspired Taxonomy for Prompts»,
  **arXiv:2505.12592** (v2, 2026-01-23). Перенос блока Instruction в конец: Claude-Sonnet-3.5
  **+12%** (56,49 → 63,37), Llama3.2-3b-inst **+5%**, Mixtral-8x7b-inst **−23%**. Одна задача
  (Task067, abductive NLI) — в посте это не выдаётся за широкий замер, только за три знака.
  Файл `07`, строка #8.
- В посте **намеренно не использован** куда более громкий результат той же работы
  (перенос блока Request/Question в середину: **−76%** у Claude-Sonnet-3.5) — он про другой блок
  и легко читается как «инструкцию в конец = катастрофа», то есть прямо противоположный совет.

**Измеренный ноль по языку — именно ноль, а не отсутствие данных.**

- Факториальный тест 4 типа промпта × 3 языка промпта × 4 статьи (перевод редакционных статей
  *El País* на китайский, GPT-5.2), **arXiv:2607.03160**: **«Prompt language had a negligible
  impact under both evaluation paradigms»** — и по BLEU/BERTScore, и по человеческой MQM-оценке.
  Единственный найденный прямой факториальный тест взаимодействия «структура × язык». Файл `08`,
  §1.1. Список авторов в раунде не резолвлен — поэтому в посте работа названа по дизайну, а не
  по фамилии.
- Menschikov, Kharitonov, Kotyga, Porvatov, Zhukovskaya, Kagramanyan, Shvetsov, Burnaev,
  «Beyond Early-Token Bias: Model-Specific and Language-Specific Position Effects in Multilingual
  LLMs», **arXiv:2505.16134** (v3, 2025-05-21). Пять типологически разных языков (EN SVO,
  DE V2, HI преимущественно SOV, VI изолирующий, **RU** со свободным порядком). Position bias —
  **«primarily model-driven»**; Appendix E, дословно: «we find no evidence to suggest that
  position bias influences models to favor specific word orders». Там же: инструкция «самый
  релевантный фрагмент помечен как 1» при наличии дистракторов **снижала** точность — одинаково
  во всех пяти языках. Файл `09`, строки #1–#2, и файл `00`, строка 46.

**Три вендора противоречат друг другу (хук поста).** Файл `07`, строки #11–#14, все три
первоисточника прочитаны напрямую в том раунде, 2026-10-02:

- **Anthropic** («Long context prompting»): документ сначала, запрос в конец — «queries at the
  end can improve response quality by up to 30 percent in tests», **без ссылки на тест и методику**.
- **OpenAI** (GPT-4.1 Prompting Guide): инструкция **и в начале, и в конце**; если только один
  раз — то **в начале** («above… works better than below»). Чисел нет.
- **Google** (Gemini «Prompt design strategies»): «supply all the context first. Place your
  specific instructions or questions at the very end». Чисел нет.
- То есть по вопросу «если один раз — где» Anthropic и Google говорят «в конце», OpenAI —
  «в начале». Методику не публикует ни один из трёх. Отсюда формулировка хука: **«Замер не
  показывает ни один»** — это про отсутствие опубликованного замера, а не про отсутствие цифры
  у Anthropic (цифра есть, методики за ней нет).

**Наш собственный замер.** Файл `10`, предрегистрация записана до прогона.

- Модель `haiku` через `claude -p --model haiku`, CLI Claude Code 2.1.197, прогон 2026-10-02.
  Температура через CLI не управляется — зафиксировано как confound.
- Парный дизайн: 4 порядка блоков (`role_first`, `task_first`, `constraints_last`,
  `resources_last`) × 2 языка (RU/EN) × 16 заданий. **176 вызовов** на сложной версии задачи
  (128 основная сетка + 16 калибровка + 32 контрольных повтора). Плюс 96 вызовов на простой
  версии — там **24/24 во всех четырёх проверенных ячейках**, то есть на лёгкой задаче вопрос
  о порядке блоков не имеет смысла. Всего по всем прогонам 272 вызова, сбоев 0.
- Результат: `constraints_last` лучший и в RU (**14/16**), и в EN (**11/16**). `resources_last`
  («большой блок данных в конец») — худший в RU (**9/16**) и не лучше остальных в EN (10/16).
  Ни одна из 6 пар порядков не дала противоположного знака между языками.
- **Формулировка в посте выбрана слабая намеренно:** «единственное, что в этом замере совпало
  между языками», а не «инвариантно по языку». В файле `10` прямо сказано, что сказать «знаки
  совпали 6 из 6» было бы overclaim — в трёх парах EN-разница равна нулю, и согласие знаков там
  не определено. H1 (взаимодействие) не подтверждена; H0 **согласуется** с данными, но не доказана.
- **Шум, который в посте назван прямо.** Одна и та же комбинация RU/`role_first`, те же 16
  заданий, три независимых прогона: **13/16 → 10/16 → 12/16**, размах **3 задания = 18,8 п.п.**
  на неизменном входе. McNemar для лучшего против худшего в RU: **p = 0,062** — не значимо на
  уровне 0,05; та же пара в EN — p = 1,0. Файл `10` называет это «возможно, самым полезным
  результатом эксперимента»; пост поэтому ставит ограничение в отдельный абзац, а не в сноску.

**Вежливость — единственное реально языкозависимое.**

- Yin et al., «Should We Respect LLMs? A Cross-Lingual Study on the Influence of Prompt
  Politeness on LLM Performance», EMNLP 2024 Workshop SICon, **arXiv:2402.14531**: «the best
  politeness level is different according to the language» (сверено с абстрактом).
- Оговорка в посте — из разбора в `materials/prompt-language-structure.md`: у **GPT-3.5**
  оптимум по языкам 8 / 5 / 2 (EN / ZH / JA), у **GPT-4 — уровень 4 во всех трёх**; авторы:
  «in advanced models, the politeness level of the prompt may have a lesser impact on model
  performance». Отсюда «у модели посильнее оптимум оказался один для всех трёх».
- «Работ несколько, и ответы не сходятся»: **arXiv:2604.16275** («No Universal Courtesy»,
  EN/HI/ES, 22 500 пар — вежливость даёт до ~11%, но в испанском выигрывает *Positive
  Impoliteness*) и **arXiv:2512.12812** («Does Tone Change the Answer?» — «tone effects diminish
  and largely lose statistical significance… modern LLMs are broadly robust to tonal variation»).
  Точные дельты из 2402.14531 в том раунде извлечь не удалось — поэтому в посте нет ни одного
  процента про вежливость.

**Чего в посте сознательно нет.**

- Ни слова про исследования на людях — владелец развернул на модели.
- Нет утверждения «порядок не влияет»: первый же содержательный абзац показывает, что влияет.
- Нет нашего пилота в роли доказательства языковой инвариантности — в файле `10` это прямо
  заблокировано.
- Нет цифры −76% из PromptPrism (другой блок, противоположный совет — см. выше).
- Нет соблазнительной интерпретации «русский чувствительнее к структуре» (разброс 5 заданий
  в RU против 1 в EN): файл `10` помечает её как НЕОПРЕДЕЛЁННОЕ — EN-ячейки почти плоские,
  ранжировать там нечем, а шум сопоставим с эффектом.

---

### Что внутри поста и почему (ШАГ 0, вариант про модели)

| Элемент | Что взято |
|---|---|
| Первая строка | Разногласие трёх вендоров + «замер не показывает ни один». Конкретный факт, не лозунг; небанально и для специалиста |
| Доказательство «структура значима» | Lu et al. (>85% → ~50% на той же четвёрке примеров) + FormatSpread (медиана 7,5 п.п., хвост >70). Источник перед цифрой |
| Разворот | PromptPrism: три знака у трёх моделей на одном и том же сдвиге — настраивать под модель, не под язык |
| Измеренный ноль | Факториальный тест 4×3 на GPT-5.2 + position bias «primarily model-driven» на 5 языках, включая русский. Сказано, что это ноль измеренный, а не отсутствие данных |
| Любимая деталь | «Самый релевантный помечен как 1» снижает точность — одинаково во всех пяти языках. Живая, запоминается, работает на ось |
| Своё | 176 вызовов, парный дизайн; практический вывод «данные вперёд, инструкцию после» |
| Ограничение | 13/16 → 10/16 → 12/16 на неизменном промпте; меньше трёх заданий толковать нельзя; пилот, не доказательство. Отдельным абзацем, не сноской |
| Языковое, что всё-таки нашлось | Вежливость — с двумя оговорками (у сильной модели сжимается; работ несколько, ответы разные) |
| Закрытие | Вопрос, который задают вслух: куда кладёте данные и откуда знаете, что так лучше. Без «if you've…», без анкеты |
| Эмодзи | Три, разные, как маркеры поворотов: 🔀 переключение знака, 🧪 свой замер, 🎲 шум |
| Длина | RU 390 слов / 2452 символа, EN 416 слов / 2405 символов (с хэштегами и ссылкой) — внутри лимита 3000 знаков LinkedIn |

---
# ЗАБРАКОВАН №1: про людей, а не про модели

**Чем именно плох:** ось ушла в исследование на людях (читатели, айтрекинг, культурные
предпочтения) — владелец прямо развернул на языковые модели. Текст сохранён целиком: разбор
источников в нём честный и может пригодиться для отдельного материала про людей (issue #219).

## LinkedIn — самостоятельный пост: формулировка важна, язык почти нет

Не анонс статьи. Ось — мысль владельца: формулировка и структура описания задачи влияют сильно,
но это влияние почти не зависит от языка; между языками расходятся **предпочтения**, а не
понимание и не результат.

Постит Макс со своего профиля. Ниже — готовый текст, копипастить целиком.
Трасса по LLM-стороне: `tasks/20260923_sdlc-ai-pitfalls/materials/prompt-language-structure.md`.

---

### RU — готово к копипасте

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

### EN — готово к копипасте

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

### Первый комментарий (опционально — если Макс решит убрать ссылку из тела)

**RU:** Работы: читатели и структура текста — https://journals.sagepub.com/doi/10.1177/1050651920932192 ·
инструкция к Excel и айтрекинг — Technical Communication 68(1), 2021 ·
порядок посылок у LLM — https://arxiv.org/abs/2402.08939 ·
вежливость по языкам — https://arxiv.org/abs/2402.14531

**EN:** The papers: readers and text structure — https://journals.sagepub.com/doi/10.1177/1050651920932192 ·
the Excel manual with eye-tracking — Technical Communication 68(1), 2021 ·
premise order in LLMs — https://arxiv.org/abs/2402.08939 ·
politeness across languages — https://arxiv.org/abs/2402.14531

---

### Что проверено своими руками, а что нет (2026-10-02)

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

### Что внутри поста и почему (ШАГ 0)

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
