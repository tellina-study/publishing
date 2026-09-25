# Translation log — ru.md → en.md (20260924_ai-delivery-gap)

Дата: 2026-09-25. Источник: `ru.md` (7471 слово, 844 строки). Результат: `en.md` (9354 слова по
`wc -w`, 901 строка). Разница в счёте слов — обычная для RU→EN (артикли, предлоги, разбитые
периоды), не признак добавленного содержания: структура и все числа совпадают (см. §4).

---

## 1. Заголовок

**Выбран:** `AI speeds up every part of software development — and can slow the whole down`

Несёт обе половины русского заголовка: части ускоряются, целое — нет и может проседать.
«the whole» подхвачено в первом же подзаголовке (`Every part is faster. The whole is not`), так что
пара «part / whole» работает как сквозной термин.

**Запасные варианты:**

1. `Every part of software development got faster. Delivery didn't.` — бьёт сильнее и короче для
   соцсетей, но теряет «может замедлить»: только констатация отсутствия прироста.
2. `AI makes every part of delivery faster — and the whole of it slower` — самый резкий; берёт
   минус DORA как утверждение, а статья его аккуратно хеджирует тремя оговорками. Годится только
   если владелец готов к более жёсткой рамке.

---

## 2. Словарь терминов (держится одинаково по всему тексту)

| RU | EN | Примечание |
|---|---|---|
| часть / целое | part / whole | сквозная пара, вынесена в заголовок и в H2 |
| доставка | delivery | |
| пропускная способность / стабильность доставки | throughput / delivery stability | как в DORA |
| опора на ИИ (+25% опоры) | reliance on AI (+25% of reliance) | DORA-шкала самоотчёта |
| выпущенный результат | the shipped result | |
| контур контроля | the control loop | H2: «take the human out of the loop» |
| контроль (линтер/тест/ревью/гейт) | a control | совпадает с цитатой «whether a control will enforce it» |
| **молчащий контроль** | **a control that has gone quiet** | основная форма; прилагательное — «silent» / «goes quiet»; «девять недель молчаливого мусора» → «nine weeks of quiet garbage» |
| гейт | gate / quality gate | |
| засев (заведомого дефекта) | seeding (a known defect) | «рецепт засева» → «seeding recipe» |
| заведомый дефект | a planted defect / a defect on purpose | формула «подать в контроль заведомый дефект» → «feed the control a defect on purpose» — держится дословно одинаково во всех 5 повторах |
| заведомо негодный (манифест, HCL, миграция) | known-bad | |
| bebugging | bebugging | |
| мутационное тестирование / мутант / мутационный балл | mutation testing / mutant / mutation score | |
| сцепленность (с реальными багами) | coupling (coupled to) | |
| принуждающий контроль | an enforcing control | из цитаты «a control will enforce it» |
| файл инструкций | instruction file / agent instruction file | |
| задача-провокация | provocation task | |
| откат | rollback | |
| дифф | diff | |
| канареечный выпуск / канарейка | canary release / the canary | |
| раскатка, выкатка | rollout | |
| ускоритель билда | build accelerator | |
| политики как код | policy as code | |
| fitness-функция | fitness function | |
| ADR | ADR | расшифровка при первом употреблении сохранена |
| code smell | code smell | |
| когнитивная сложность | cognitive complexity | |
| запахи требований | requirements smells | |
| staggered difference-in-differences / matched event study | без перевода | |
| абляция | ablation | определение в тексте сохранено |
| ложные флаги | false flags | |
| пропуск (17% опасных действий) | miss / miss rate | |
| усталость от подтверждений | approval fatigue | термин самой Anthropic |
| окна разрешений | permission prompts | термин самой Anthropic |
| находка (анализатора) | finding | |
| дефициты (PCAOB) | deficiencies | |
| ослепление | blinding | |
| dead man's switch | dead man's switch | |
| «Вывод:» / «Общий вывод:» | «Takeaway:» / «Overall takeaway:» | 26 + 1 = 27, как в оригинале |
| «Итог блока» / «Счёт по этапам» / «Граница измеренного» | «Section in short» / «The stage-by-stage tally» / «The edge of what's measured» | 6 карточек |

---

## 3. Места, где пришлось отойти от буквального перевода

Содержание не менялось нигде; ниже — все сознательные отступления от подстрочника.

1. **«устоявшегося русского перевода нет, дальше — засев заведомого дефекта».** В английском это
   утверждение бессмысленно: bebugging — родной термин. Заменено на введение термина без
   русско-специфической ремарки: *«The literature calls this bebugging; below it is mostly seeding a
   known defect.»* Факт (Миллз, 1972, оценка ненайденных дефектов) и оговорка «эта версия наша»
   сохранены дословно.
2. **Русские длинные периоды разбиты на два-три предложения** там, где английский иначе провисает:
   абзац про RADAR, абзац про RAMP, абзац про Gatekeeper/conftest/terraform, финальный абзац про
   инциденты. Порядок фактов внутри абзаца не менялся.
3. **«не мерил почти никто» → «almost nobody has measured directly»**, а не «nobody has measured» —
   по требованию 6. Так же: «мы не нашли» → «we did not find» (4 места: доли правил с тестами,
   миграции, работы про отказ ИИ-функции, единственная работа за пределами кода).
4. **«коды ответа двухсотые» → «the response codes are 200s»**, **«отдаёт пятисотки» → «returns
   500s»**, **«стопроцентный отказ» → «a 100% outage»**. Русские числительные-слова, в английском
   естественнее цифрой; третий случай вдобавок ближе к источнику (SRE Workbook: *«a 100% outage
   consumes only 1.4% of the budget»*). Это единственные три числа, которых нет в `ru.md` (см. §4).
5. **«Спор „убирать человека или нет“ в общем виде неразрешим»** → «The argument … cannot be settled
   in general». Русское «неразрешим» в лоб («unsolvable») звучало бы сильнее, чем есть; речь о том,
   что данные не позволяют закрыть спор.
6. **«Человек тут формально в контуре, но способность заметить дефект у него падает — а это и
   подразумевают под „модель подстрахует“»** → в английском связка развёрнута: «…and that ability is
   exactly what "the model will back you up" is supposed to protect». Без этого «that is exactly what
   … is supposed to mean» читалось двусмысленно. Утверждение то же.
7. **«из которых собираются 9095 (29%)»** → «of which 9,095 (29%) build». «Собираются» здесь —
   компилируются/собираются в сборку; «build» сохраняет ту же неоднозначность, что и оригинал.
8. **Курсив и жирный перенесены один в один**, включая пять пометок *Our proposal* (в двух случаях с
   уточнением, как в оригинале: *Our proposal, not industry practice* и *Our proposal, a harness on
   top of promptfoo*), и два «формулировка наша» → «this version is ours» / «the framing is ours».
9. **Цитаты.** Русские кавычки «…» → английские "…". Все дословные английские цитаты возвращены к
   оригиналам по `fact-check.md`, а не переведены обратно (см. §4). Знаки препинания внутри цитат —
   как в источнике; точка вынесена за кавычку там, где в источнике цитируется фрагмент фразы.
10. **Заголовки разделов** переведены по смыслу, а не пословно, где пословный вариант не работает:
    «Ответ индустрии: человека убирают из контура» → «The industry's answer: take the human out of
    the loop» (идиома). «Что видно со всех шести сразу» → «What the six stages show together».
    Нумерация и количество заголовков совпадают (8 × `##`, 19 × `###`).

---

## 4. Сверка

### Ссылки

| | ru.md | en.md |
|---|---|---|
| вхождений ссылок | 87 | 87 |
| уникальных URL | 74 | 74 |
| расхождений | **0** | **0** |

Сверено скриптом: множества URL совпадают посимвольно, включая кратности (13 URL встречаются
дважды — в теле и в «Further reading»). Ни один URL не менялся.

### Числа

Сверено скриптом с нормализацией разделителей (ru `725 938` / `60,31` ↔ en `725,938` / `60.31`),
URL исключены из счёта, чтобы цифры внутри адресов не искажали результат.

| | ru.md | en.md |
|---|---|---|
| числовых токенов вне URL | 308 | 311 |
| различных значений | 163 | 164 |
| есть в ru, нет в en | **0** | — |
| есть в en, нет в ru | — | **3** |

Все три расхождения — односторонние и объяснимы (§3.4): `100` (ru: «стопроцентный отказ» словом),
`200` (ru: «двухсотые» словом), `500` (ru: «пятисотки» словом). Ни одного числа не потеряно, не
изменено и не добавлено по существу. Проценты, выборки, годы, страницы отчётов (стр. 37, 39–40, 30,
50) перенесены один в один.

### Дословные английские цитаты

Все 24 проверены на присутствие в `en.md` автоматически (после схлопывания переносов строк):

`small positive, but statistically insignificant` · `AI is hurting delivery performance` ·
`AI is associated with an increase in software delivery instability` ·
`No faults were intentionally seeded… All faults are naturally occurring` ·
`These tests are all designed to fail` · `neither concrete nor actionable` ·
`we have no way to consistently and reliably measure problem similarity or relevance` ·
`no evidence to support` · `code coverage had exhausted its usefulness` ·
`was covered by the existing tests` · `this alert could never fire` ·
`an electronic check (magnets, analog values, etc.) is not sufficient to comply with this requirement` ·
`almost never proactively retrieve the contribution rules` ·
`never refuse to contribute in AI-banned repositories under any condition` ·
`no measurable improvement in correctness on either agent` ·
`on consecutive runs only new violations will be reported` ·
`Expected failures only apply to user-defined custom conditions` ·
`a typical bug that introduces a privacy violation similar to {diff}` ·
`mostly involving algorithmic changes or code deletion` ·
`a developer writes a security rule but gets no feedback on whether a control will enforce it` ·
`calibration as needed` · `Halt … success rate 69.17% < 99%` ·
`Rolling back … failed checks threshold reached 10` · `no severe incident was caused by a bad rollout`

Пять из них в `ru.md` стояли в русском переводе и восстановлены по `fact-check.md` до английских
оригиналов: «покрытие исчерпало свою полезность» → *code coverage had exhausted its usefulness*;
«каждое такое изменение было покрыто существующими тестами» → *was covered by the existing tests*;
«он не конкретен и не подсказывает действия» → *neither concrete nor actionable*; «этот алерт не смог
бы сработать никогда» → *this alert could never fire*; «электронная проверка (магниты, аналоговые
значения и т. п.) требованию не удовлетворяет» → *An electronic check (magnets, analog values,
etc.) is not sufficient to comply with this requirement*; плюс NIST «калибруем по необходимости» →
*calibration as needed* и диагноз авторов про правила безопасности → *a developer writes a security
rule but gets no feedback…*

### Структура

| Элемент | ru.md | en.md |
|---|---|---|
| `##` | 8 | 8 |
| `###` | 19 | 19 |
| карточки `> 📌` | 6 | 6 |
| строки `→ **Вывод/Takeaway:**` | 27 (26 + 1 «Общий») | 27 (26 + 1 «Overall») |
| курсивные пометки «наше предложение» | 5 | 5 |
| блок `**TL;DR**` | 1 | 1 |
| «рассуждение, а не замер» | 3 | 3 |
| «применение, а не рекомендация» | 2 | 2 |
| кириллица в `en.md` | — | 0 символов |
| `# H1` в теле | — | нет (заголовок подставит публикатор) |

### Frontmatter

Соответствует ТЗ дословно: `title` (английский), `slug: ai-delivery-gap`, `status: draft`,
`categories: [AI, Software Engineering]`, `tags: [AI in SDLC, Code Review, Mutation Testing, DORA,
Quality Gates]`. `wp_post_id` не выставлен (пишется публикатором после первой отгрузки).
