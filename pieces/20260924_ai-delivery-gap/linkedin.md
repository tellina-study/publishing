# LinkedIn — анонс статьи «ИИ ускоряет каждую часть разработки — и может замедлить целое»

Статья: https://tellian.io/2026/09/25/ai-delivery-gap/
Постит Макс со своего профиля. Ниже — готовый текст, копипастить целиком.

**Актуальный вариант — первый.** Два прежних лежат ниже как забракованные, не для использования.

---

# ВАРИАНТ 3 (актуальный) — тезис статьи + что с этим делать

## EN — готово к копипасте

AI speeds up every part of building software. The whole thing can still come out slower.

Harvard went through five years of telemetry from 718 firms — 300 million real work events, not a survey. After those teams moved to AI agents they wrote 30% more code. The number of tasks they actually finished didn't move.

Every station on the line got faster. The same amount comes off the end of it.

From inside a team none of this shows. In there things are going well: documentation better, code better, review faster — that's DORA's 2024 survey, teams rating themselves. Look at what those ratings are made of. Nobody measures code quality; you read a linter. Nobody measures whether a change got reviewed; you read how fast the review closed. Behind every one of those numbers sits a check reporting on itself.

🟢 A green build. Is it green because the code is fine, or because the tests quietly stopped catching things? From outside those look the same. Google went back over 1,502 of its own high-priority bugs — every change that introduced one was already covered by the existing tests.

I wrote the long version up: where the gap goes, and what to watch instead.

🔗 https://tellian.io/2026/09/25/ai-delivery-gap/

Take one number your team stares at every week and ask who outside the team ever wanted it. A finished task has someone. A line, a commit, a PR don't.

🔨 Then go break something on purpose. Write the change your gate is supposed to reject, and push it. A fire code tests a smoke detector with smoke. Not with a self-check — with smoke. Nobody asks that of your pipeline, so you have to ask it yourself.

When did your pipeline last refuse to ship something? Not "it's green" — actually refuse.

#SoftwareEngineering #AI #EngineeringLeadership #CodeQuality

## RU — готово к копипасте

ИИ ускоряет каждую часть разработки. Целое при этом может выйти медленнее.

Гарвард разобрал пять лет телеметрии 718 фирм — 300 млн настоящих рабочих событий, а не опрос. Команды перешли на ИИ-агентов и стали писать на 30% больше кода. Закрытых задач у них столько же, сколько было.

Каждый участок конвейера стал быстрее. С конца выходит столько же.

Изнутри команды этого не видно — там всё хорошо: документация лучше, код лучше, ревью быстрее. Это опрос DORA за 2024 год, команды оценивают себя сами. А теперь посмотрите, из чего сделаны такие оценки. Качество кода никто не измеряет — вы смотрите на линтер. Было ли ревью, тоже никто не измеряет — вы смотрите, за сколько оно закрылось. За каждой цифрой стоит проверка, которая отчитывается сама о себе.

🟢 Зелёная сборка. Она зелёная потому, что с кодом всё в порядке, — или потому, что тесты тихо разучились что-то ловить? Снаружи это одно и то же. Google перебрал 1502 своих высокоприоритетных бага: каждое изменение, которое такой баг приносило, уже было покрыто тестами.

Я написал об этом статью: куда девается разрыв и на что смотреть вместо.

🔗 https://tellian.io/2026/09/25/ai-delivery-gap/

Возьмите одну цифру, на которую команда смотрит каждую неделю, и спросите, кому за пределами команды она была нужна. У закрытой задачи такой человек есть. У строки, коммита и PR — нет.

🔨 А потом сломайте что-нибудь нарочно. Напишите то изменение, которое ваш гейт обязан отклонить, и отправьте его. Пожарная норма проверяет дымовой датчик дымом. Не самопроверкой — дымом. С вашего пайплайна такого никто не требует, так что спросить придётся самому.

Когда ваш пайплайн в последний раз отказался что-то выпускать? Не «всё зелено», а именно отказался.

#SoftwareEngineering #AI #EngineeringLeadership #CodeQuality

## Первый комментарий со ссылкой

**EN:**

The piece: https://tellian.io/2026/09/25/ai-delivery-gap/ — where each of these numbers comes from, six stages of development, and how to feed a defect into your own gates at each one.

**RU:**

Статья: https://tellian.io/2026/09/25/ai-delivery-gap/ — откуда каждая из этих цифр, шесть стадий разработки и как на каждой подать дефект в свой гейт.

## План варианта 3 (ШАГ 0)

| Элемент | Что взято |
|---|---|
| Первая строка | Тезис статьи дословно: части быстрее, целое может выйти медленнее. Сначала мысль, доказательство — со второй строки |
| Доказательство | Гарвард, телеметрия 718 фирм: +30% кода, закрытых задач столько же. Источник стоит перед цифрой |
| Почему изнутри не видно | DORA-2024 без процентов (самооценка): локальные показатели сняты с проверок, а не с результата |
| Картинка вместо формулировки | Зелёная сборка: не знаешь, она зелёная от порядка в коде или от того, что тесты разучились ловить |
| Число-доказательство | Google, 1502 высокоприоритетных бага: каждое вносящее изменение уже было покрыто тестами |
| Что делать (вторая половина) | (1) взять цифру недели и спросить, кому она нужна за пределами команды; (2) нарочно отправить изменение, которое гейт обязан отклонить |
| Образ | Пожарная норма — две короткие фразы внутри второго действия, не хук |
| Закрытие | Вопрос, который задают вслух: когда пайплайн в последний раз отказался что-то выпускать |
| Причинность | «+49% ко времени ревью» не взято вовсе — чтобы рядом с «+30% кода» не читалось как следствие |
| Длина | EN ~300 слов, RU ~270 |

---

# ЗАБРАКОВАН — вариант 2: части в плюсе, целое на месте

**Чем именно плох:** фокус верный, изложение нейрослопное — открывается данными вместо
утверждения, абзацы склеены машинными связками («Отсюда две вещи.», «Если коротко:», «Спросить
сами команды — картина хорошая.»), «что делать» подано симметричными буллетами с эмодзи, финальный
вопрос звучит как пункт опроса.

## EN

Telemetry from 718 firms: teams that moved to AI agents wrote 30% more code and closed the same number of tasks. In the same data, review time rose 49%.

Ask the teams themselves and it looks good. In DORA's 2024 survey, every 25% more reliance on AI came with documentation +7.5%, code quality +3.4%, review speed +3.1%. That is their own rating, not a measurement.

Every part of the work got better. The whole didn't.

The new piece is about why that happens and what to watch instead. Short version: nobody measures documentation or code quality directly. Behind each of those numbers there is a control — a linter, a test, a review, a CI gate. You are reading the control, not the result. And a control has a state that looks exactly like working: silence.

Two things follow.

📍 Watch what reaches the user, not what got produced. Easy test: does it have a customer outside the team? A closed task does. A line, a commit, a PR doesn't.

📍 Test the control itself. Fire codes don't call a smoke detector tested until smoke has gone inside it — an electronic self-check doesn't count. Software has no such rule. Google went back through 1,502 of its high-priority bugs, and every change that brought one in was already covered by the tests. All green. So put a defect in on purpose and see whether your gate catches it.

🔗 https://tellian.io/2026/09/25/ai-delivery-gap/

Of the numbers your team looks at every week, which ones have a customer outside the team?

#SoftwareEngineering #AI #DeveloperProductivity #CodeQuality #EngineeringLeadership

## RU

Телеметрия 718 фирм: команды, которые перешли на ИИ-агентов, стали писать на 30% больше кода и закрывать столько же задач. В тех же данных время ревью выросло на 49%.

Спросить сами команды — картина хорошая. В опросе DORA за 2024 год каждые +25% опоры на ИИ идут вместе с +7,5% к качеству документации, +3,4% к качеству кода, +3,1% к скорости ревью. Это их собственная оценка, а не замер.

Каждая часть работы стала лучше. Целое — нет.

Новая статья — про то, почему так выходит и на что смотреть вместо этого. Если коротко: качество документации и качество кода никто не меряет напрямую. За каждой такой цифрой стоит контроль — линтер, тест, ревью, гейт в CI. Вы читаете контроль, а не результат. А у контроля есть состояние, неотличимое от рабочего: молчание.

Отсюда две вещи.

📍 Смотреть на то, что дошло до пользователя, а не на то, что произвели. Простая проверка: есть ли у этого заказчик за пределами команды? У закрытой задачи есть. У строки, коммита и PR — нет.

📍 Проверять сам контроль. Пожарная норма не считает датчик проверенным, пока дым не попал внутрь, — электронная самопроверка не засчитывается. В разработке такого правила нет. Google перебрал 1502 своих высокоприоритетных бага: каждое изменение, которое такой баг приносило, уже было покрыто тестами. Всё зелёное. Значит, надо подать дефект нарочно и посмотреть, сработает ли гейт.

🔗 https://tellian.io/2026/09/25/ai-delivery-gap/

Из цифр, на которые ваша команда смотрит каждую неделю, у каких есть заказчик за пределами команды?

#SoftwareEngineering #AI #DeveloperProductivity #CodeQuality #EngineeringLeadership

---

# ЗАБРАКОВАН — вариант 1: фокус на проверке контролей

**Чем именно плох:** не тот фокус — ведёт самым ярким эпизодом статьи (пожарная норма + число
Google), поднимает разговор про тестирование и обещает читателю не тот текст, который он получит;
тезис статьи — разрыв между частями и целым — в посте не звучит вовсе.

## EN

A smoke detector isn't tested until smoke gets inside its chamber. The fire code is blunt about it: an electronic self-check doesn't count.

Software has no such rule. We look at a green pipeline and take it as proof.

Google went back through 1,502 of its own high-priority bugs. Every change that brought one in was already covered by the existing tests. All green. Planting small defects into that same code would have caught 1,043 of those bugs — 70%. What they wrote about coverage: it "had exhausted its usefulness."

A green check only tells you the control is quiet. And quiet looks the same whether nothing is broken or the detector is dead. One way to tell them apart: put a defect in on purpose and see if it gets caught.

The new piece is about that missing second check — not "did the gate say no," but "when did we last see that it can?" Six stages, from requirements to monitoring: what has actually been measured at each one, what AI changes there, and how to feed a defect in yourself. Code got cheap to write. The gates at the end of the line are the old ones, and hardly anyone checks that they still work.

🔗 https://tellian.io/2026/09/25/ai-delivery-gap/

When did one of your checks last say no — and how would you know if it stopped being able to?

#SoftwareEngineering #AI #CodeQuality #Testing #EngineeringLeadership

## RU

Дымовой датчик не считается проверенным, пока дым не попал внутрь камеры. Норма пожарной безопасности говорит прямо: электронная самопроверка не засчитывается.

В разработке такого правила нет. Мы смотрим на зелёный пайплайн и принимаем его за доказательство.

Google перебрал 1502 своих высокоприоритетных бага. Каждое изменение, которое приносило такой баг, уже было покрыто существующими тестами. Всё зелёное. Если бы в тот же код нарочно сажали мелкие дефекты, это поймало бы 1043 бага — 70%. Про покрытие авторы написали так: оно «исчерпало свою полезность».

Зелёная галочка говорит только одно: контроль молчит. А молчание выглядит одинаково — и когда всё цело, и когда датчик мёртв. Отличить можно единственным способом: подать дефект нарочно и посмотреть, поймают ли.

Новая статья — про эту недостающую вторую проверку. Вопрос не «сработал ли гейт», а «когда мы в последний раз видели, что он может сработать». Шесть стадий, от требований до мониторинга: что на каждой измерено, что там меняет ИИ и как самому подать дефект. Писать код стало дёшево. Гейты в конце конвейера остались прежние, и почти никто не проверяет, что они ещё работают.

🔗 https://tellian.io/2026/09/25/ai-delivery-gap/

Когда ваша проверка в последний раз сказала «нет» — и как вы поймёте, если она разучится?

#SoftwareEngineering #AI #CodeQuality #Testing #EngineeringLeadership

## Первый комментарий со ссылкой (для варианта 1)

**EN:** The piece: https://tellian.io/2026/09/25/ai-delivery-gap/ — six stages of development, what has been measured at each, and where no ready way to seed a defect exists yet.

**RU:** Статья: https://tellian.io/2026/09/25/ai-delivery-gap/ — шесть стадий разработки, что на каждой измерено и где готового способа подать дефект пока просто нет.
