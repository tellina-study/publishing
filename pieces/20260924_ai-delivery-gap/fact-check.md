# Fact-check: 20260924_ai-delivery-gap

Проверено **95 несущих утверждений**. Метод: резолвил первоисточник сам (PDF/страница), читал
нужное место, сверял формулировку в тексте с формулировкой источника. «Трасса так пишет» за
подтверждение не считал. Все 42 ссылки статьи резолвятся (ACM и BMJ отдают 403 боту — содержание
проверено по авторским копиям: Microsoft Research и James Lind Library).

Вердикты: **Verified this run** — открыл источник, он говорит ровно это. **Inferred** — следует из
прочитанного, но дословно не сказано. **Not verified** — не подтверждено (обычно утверждение об
отсутствии). **Wrong** — источник говорит другое.

---

## §1. Хук: прирост упирается в ревью

| # | Утверждение как в тексте | Источник | Цитата / свидетельство | Вердикт | Правка |
|---|---|---|---|---|---|
| 1 | Chen & Stratton, Гарвард, август 2026; 300 млн событий, 725 938 работников, 718 фирм, янв.2021–март 2026 | [fion.ac/jellyfish.pdf](https://fion.ac/jellyfish.pdf), «Artificial Intelligence in the Firm: Bottlenecks in Software Production», Fiona Chen, James Stratton, Harvard, current version August 4, 2026 | «covering 300 million work events — including GitHub coding activity, Jira issues, and Google Calendar events — across 718 firms»; «There are 725,938 workers across 718 firms … between January 2021 and March 2026» | **Verified** | — |
| 2 | Метод — staggered DiD по дате включения; телеметрия, не опрос | там же | «We use a staggered difference-in-differences design, exploiting variation in firm-level adoption timing» | **Verified** | — |
| 3 | Агенты: +30% строк, +20% коммитов, +23% PR | там же, Introduction | «AI agents lead to large and significant increases in all three measures: 30% for lines of code, 20% for commits, and 23% for pull requests» | **Verified** | — |
| 4 | Выпущенный результат — «small positive, but statistically insignificant»; данные исключают прирост >12% | там же | «We find small positive, but statistically insignificant, effects on both measures»; «our estimates rule out an increase in output of larger than 12% of the baseline mean» | **Verified** | — |
| 5 | Ревью +49%, доля PR с запросом правок почти удвоилась, комментариев +35% | там же | «The average time to review a pull request increases by 49%, the share of pull requests with changes requested nearly doubles, and the number of comments per pull request increases by 35%» | **Verified** | — |
| 6 | Затык сохраняется даже после внедрения ИИ-инструментов для ревью | там же | «This bottleneck persists following the adoption of AI code review tools.» | **Verified** | — |
| 7 | NBER WP 35275, 500 000+ разработчиков, matched event study: коммиты +240%, проекты +80%, релизы +30% | [nber.org/papers/w35275](https://www.nber.org/papers/w35275), Demirer, Musolff, Yang, «Writing Code vs. Shipping Code», май 2026, ред. сент. 2026 | 500 000+ GitHub-разработчиков; matched event study; +240% коммиты / +80% проекты / +30% релизы (кумулятивно по трём поколениям инструментов); «large task-level AI productivity gains have translated only partially into shipped and used software» | **Verified** | Можно добавить одно слово: прирост **кумулятивный по трём поколениям инструментов**, а не эффект одного включения |
| 8 | DORA-2024, стр. 39–40: −1,5% пропускной способности, −7,2% стабильности на +25% опоры | [2024_final_dora_report.pdf](https://services.google.com/fh/files/misc/2024_final_dora_report.pdf), стр. 39–40 | Заголовок стр. 39: «AI is hurting delivery performance». Стр. 40: «an estimated 1.5% reduction for every 25% increase in AI adoption. The negative impact on delivery stability is larger (an estimated 7.2% reduction for every 25% increase in AI adoption)» | **Verified** | — |
| 9 | Стр. 37: +7,5% качество документации, +3,4% качество кода, +3,1% скорость ревью | там же, стр. 37 | «A 25% increase in AI adoption is associated with a… 7.5% increase in documentation quality / 3.4% increase in code quality / 3.1% increase in code review speed» | **Verified** | — |
| 10 | «+25% опоры» — латентная шкала самоотчёта из семи пунктов | там же, стр. 30 | «The strong commonality and covariance among these seven items suggests an underlying factor that we call AI adoption» | **Verified** | — |
| 11 | В 2025 семь пунктов заменены тремя, включая «доверие»; сам DORA этой оговорки не делает | [dora.dev/dora-report-2025](https://dora.dev/dora-report-2025/) + методология 2025 (reliance / trust / reflexive use) | Три пункта подтверждены. Что «DORA этой оговорки не делает» — утверждение об отсутствии | **Inferred** | Оставить, но формулировать как «в отчёте 2025 такой оговорки мы не нашли» |
| 12 | Отчёт 2025 фиксирует разворот знака по пропускной способности | DORA 2025 PDF, стр. 42 | «AI's relationship with software delivery throughput has turned from negative to positive» | **Verified** | — |
| 13 | «−7,2% стабильности 2026 год не подтверждает и не опровергает. Сопоставимым методом её никто не померил» | DORA 2025 PDF, стр. 38, 39, 43 | Стр. 39: «AI is associated with an increase in software delivery instability». Стр. 43: «it continues its detrimental relationship with software delivery stability» | **Wrong (вводит в заблуждение)** | **ОБЯЗАТЕЛЬНО.** Отчёт 2025 воспроизводит **направление** находки по стабильности (эффект в стандартизованном виде, процентной оценки нет). Текст сообщает читателю только про разворот по пропускной способности и умалчивает, что по стабильности находка устояла. Правка: «В 2025 DORA развернул знак по пропускной способности, а связь ИИ с нестабильностью доставки сохранил — но уже в стандартизованных эффектах, без процентов и на другой шкале. Так что именно цифру −7,2% сопоставимым методом никто не перепроверял» |

---

## §2. Вывод человека из контура

| # | Утверждение | Источник | Цитата | Вердикт | Правка |
|---|---|---|---|---|---|
| 14 | RADAR: 535 тыс. диффов, 331 тыс. заленденных | [arXiv:2605.30208](https://arxiv.org/abs/2605.30208), «Automating Low-Risk Code Review at Meta», 28.05.2026 | «RADAR has reviewed 535K+ diffs and landed 331K+» | **Verified** | — |
| 15 | Порог p25→p50 → автоодобрение 60,31% | там же | «Relaxing the Diff Risk Score threshold from the 25th to the 50th percentile increased the approve rate to 60.31%» | **Verified** | — |
| 16 | Откаты — треть от не-RADAR, инциденты — одна пятидесятая | там же | «The revert rate for RADAR-reviewed diffs is 1/3 that of non-RADAR diffs, and the Production Incident rate is 1/50 that of non-RADAR diffs» | **Verified** | — |
| 17 | Оговорка: диффы отбираются по риску, это не рандомизация | там же | «a multi-stage funnel that classifies each diff by authorship and source type, applies eligibility gates…»; оценка — «observational before-after comparisons» | **Verified** | — |
| 18 | DORA-2019, стр. 50: внешнее одобрение → в 2,6 раза чаще низкоэффективные; «no evidence to support» | [2019-dora-report.pdf](https://dora.dev/research/2019/dora-report/2019-dora-accelerate-state-of-devops-report.pdf), стр. 50 | «Survey respondents were 2.6 times more likely to be low performers if their organization had this kind of formal approval process in place»; «we found no evidence to support this hypothesis» | **Verified** | Ссылка в тексте ведёт на страницу capabilities, а не на PDF со стр. 50. Поставить ссылку на PDF отчёта |
| 19 | Выборка ~1000 респондентов того года | там же | «With almost 1,000 respondents, our analyses have a 3% margin of error» | **Verified** | — |
| 20 | Anthropic: 93% запросов на разрешение одобряют | [anthropic.com/engineering/claude-code-auto-mode](https://www.anthropic.com/engineering/claude-code-auto-mode), 25.03.2026 | «Claude Code users approve 93% of permission prompts»; «Over time that leads to approval fatigue» | **Verified** | — |
| 21 | 0,4% ложных срабатываний на 10 000 реального трафика | там же | «0.4% FPR», «Real internal traffic (n = 10,000)» | **Verified** | — |
| 22 | «17% пропущенных опасных действий» на n=52 | там же | «17% FNR» на «Real overeager actions (n=52)» | **Verified** | — |
| 23 | RAMP: 441 репозиторий, +28–38% коммитов у всех | [arXiv:2608.25241](https://arxiv.org/abs/2608.25241), «A Few Pages of Markdown», 26.08.2026 | «Across 441 repositories…»; «agents accelerate development regardless of maturity (28-38% more commits)» | **Verified** | — |
| 24 | Без закоммиченной конфигурации сложность +53% против +27%, предупреждений ×1,7 | там же | «among agent-first repositories, where the contrast is identified, those without committed AI configuration show roughly twice the increase in cognitive complexity (+53% versus +27%) and 1.7x the increase in static-analysis warnings» | **Verified с потерянным условием** | **ОБЯЗАТЕЛЬНО.** В тексте выпала оговорка «среди agent-first репозиториев, где контраст вообще идентифицируется», и авторская рамка: «Because maturity is observational … we present these findings as hypothesis-generating». Добавить оба |
| 25 | 73,8% артефактов конфигурации пишутся один раз | там же | «73.8% of artifacts are committed once and never modified» | **Verified** | — |
| 26 | Debt Behind the AI Boom: 302,6 тыс. коммитов из 6299 репозиториев | [arXiv:2603.28592](https://arxiv.org/abs/2603.28592), 30.03.2026 | «a dataset of 302.6k verified AI-authored commits from 6,299 GitHub repositories» | **Verified** | — |
| 27 | Больше 15% коммитов вносят находку, 22,7% из них доживают до последней версии | там же | «more than 15% of commits from every AI coding assistant introduce at least one issue»; «22.7% of tracked AI-introduced issues still survive at the latest version» | **Verified, знаменатель размыт** | «из них» читается как «из коммитов». В источнике 22,7% — доля **прослеженных находок**, не коммитов. Правка: «…а 22,7% всех прослеженных находок доживают до последней версии» |
| 28 | 89,3% находок — code smells | там же | «code smells are by far the most common type, accounting for 89.3% of all issues» | **Verified** | — |
| 29 | В пересечении репозиториев без ревью 28,92% агентских PR против 34,52% человеческих | [arXiv:2605.02273](https://arxiv.org/abs/2605.02273), «These Aren't the Reviews You're Looking For», EASE 2026, Table 1 | AI agent, R∩: 9616 PR, 2781 (28.92%) без ревью. Human, R∩: 5574 PR, 1924 (34.52%) без ревью | **Verified** | — |
| 30 | 25,92% человеческих реплик под агентскими PR — команды агенту (ссылка на arXiv:2607.13196) | **тот же arXiv:2605.02273**, Table 2 и §RQ2 | «agent-steering commands are far more common when reviewing agent-authored pull requests (25.92%) than human-authored ones (1.63%)» | **Wrong (атрибуция)** | **ОБЯЗАТЕЛЬНО.** 25,92% — из той же работы, что и 28,92/34,52, а не из «второй работы на ту же тему». В 2607.13196 («From Human-Centric to Agentic Code Review», 1,02 млн PR, 207 проектов) этой цифры нет. Убрать ссылку на 2607.13196 или переписать, отдав обе цифры одной работе |
| 31 | «Формально ревью происходит чаще» | там же | В полной популяции R_pop **61,38%** агентских PR не получают ревью вообще. В R∩ у агентских PR только **8,08%** ревью — чисто человеческие (у человеческих — 25,21%), а 57,63% — чисто агентские | **Flag** | Стейлмен честный, но однобокий: выигрыш по «доле без ревью» держится только в пересечении, а по составу ревьюеров он сразу разворачивается. Одну фразу про 61,38% / 8,08% добавить стоит — она усиливает вашу же мысль |
| 32 | Microsoft Teams, SoCC 2022: 152 инцидента severity ≤2 за год; 27,7% — наша сумма трёх категорий | [3542929.3563482.pdf](https://www.microsoft.com/en-us/research/wp-content/uploads/2022/09/3542929.3563482.pdf) (авторская копия), Figure 4 | «we … study 152 high severity incidents (severity 0, 1 and 2)». Detection Failure Category: Monitor Bug — 10.5%, No Monitors — 8.6%, Telemetry Coverage — 8.6%. Сумма = **27,7%** | **Verified, включая оговорку** | Арифметика сходится точно; честность про «посчитано нами» на месте. Образец того, как надо |

---

## §3. Молчание детектора

| # | Утверждение | Источник | Цитата | Вердикт | Правка |
|---|---|---|---|---|---|
| 33 | Миллз, 1972: сажать дефекты и по доле найденных судить **о чувствительности контроля, а не о качестве артефакта** | Harlan D. Mills, «On the Statistical Validation of Computer Programs», IBM FSD 1972 | Смысл метода у Миллза: по доле найденных подсаженных ошибок **оценить число оставшихся ненайденных ошибок в программе** — то есть как раз суждение об артефакте | **Wrong (переворот смысла) + ссылки нет** | **ОБЯЗАТЕЛЬНО.** Миллз мерил именно артефакт. «Судить о чувствительности контроля» — позднейшая переинтерпретация, и она ваша, а не его. Правка: «…и по доле найденных оценивать, сколько дефектов осталось. Современное прочтение развернуло ту же арифметику: та же доля — это мера чувствительности самого контроля». И поставить ссылку |
| 34 | Google ICSE 2021: ~400 тыс. мутантов, >33 млн прогонов, 1502 бага, 1043 (70%) | [arXiv:2103.07189](https://arxiv.org/abs/2103.07189) | «our coupling analysis involves 1502 bugs, almost 400 thousand mutants, and over 33 million test target executions»; «We found that for 1043 (70%) of the bugs, mutation testing would have reported a fault-coupled mutant in the bug-introducing change» | **Verified** | — |
| 35 | «каждое такое изменение было покрыто существующими тестами», «покрытие исчерпало свою полезность» | там же | «Recall that each bug-introducing change was covered by the existing tests, suggesting that code coverage had exhausted its usefulness.» | **Verified (дословно)** | — |
| 36 | Tricorder: ≥10% — испытательный срок, >25% — отключается | [Tricorder, ICSE 2015](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43322.pdf) | «A rate ≥10% puts the analyzer on probation… If the rate goes above 25%, we **may decide** to turn the analyzer off immediately. **In practice, we typically work with the analyzer writers to fix the problem instead of immediately disabling an analyzer.**» | **Verified с ослаблением** | «>25% — отключается» звучит жёстче источника. Правка: «>25% — анализатор могут выключить» |
| 37 | DocComments сломали на 24-й неделе 2014, починили к 33-й — девять недель | там же | «there was a bug introduced in week 24, which resulted in a sharp increase in NOT USEFUL clicks… the fix was finally released in week 33»; данные кликов — «in the year 2014» | **Verified** | — |
| 38 | «Порог отключения задан заранее и в цифрах… у автора анализатора в этом споре нет права вето» | там же | Источник прямо говорит обратное: «In practice, we typically work with the analyzer writers to fix the problem instead of immediately disabling an analyzer» | **Wrong** | **ОБЯЗАТЕЛЬНО.** Снять «нет права вето» — источник описывает ровно переговорную практику. Правка: «Порог задан заранее и в цифрах, так что спор начинается с данных, а не с мнения» |
| 39 | NFPA 72 требует, чтобы дым **физически вошёл в измерительную камеру** | [pottersignal NFPA-72 deck](https://www.pottersignal.com/resources/conference/presentations/nfpa-72.pdf) | В цитируемом источнике есть только: «Use smoke or a listed and labeled product acceptable to the manufacturer or in accordance with their published instructions» — NFPA 72 2016, Table 14.4.3.2. Формулировки про вход в измерительную камеру там нет (она есть в полном тексте Table 14.4.3.2: «ensure smoke entry into the sensing chamber») | **Not verified по этой ссылке** | **ОБЯЗАТЕЛЬНО.** Либо подставить источник с полным текстом Table 14.4.3.2, либо переписать под то, что цитируемый документ реально говорит. Заметьте: следующая фраза про CO-датчики в этом же источнике есть дословно — на неё вся конструкция и может опереться |
| 40 | Родственная норма для CO: электронная самопроверка требованию не удовлетворяет | там же | «carbon monoxide tests shall be performed at initial acceptance and annually by the introduction of carbon monoxide into the sensing chamber or element. An electronic check (magnets, analog values, etc.) is not sufficient to comply with this requirement.» — NFPA 720 2015, 8.4.5.1 | **Verified (дословно)** | — |
| 41 | EICAR: «всё равно что поджечь урну в офисе, чтобы узнать, работает ли дымовой датчик» | [eicar.org](https://www.eicar.org/download-anti-malware-testfile/) | «Using real viruses for testing in the real world is rather like setting fire to the dustbin in your office to see whether the smoke detector is working.» | **Verified (дословно)** | — |

---

## §4. Проход по этапам

| # | Утверждение | Источник | Цитата | Вердикт | Правка |
|---|---|---|---|---|---|
| 42 | Porter/Votta/Basili, TSE 1995: 48 участников, 16 команд по трое, документы с 42 и 26 дефектами | [drum.lib.umd.edu](https://drum.lib.umd.edu/bitstreams/332d6328-bdce-4726-9102-e00bac748f9a/download) | «Forty eight graduate students in computer science participated in the experiment. They were assembled into sixteen, three-person teams.»; «42 faults in the WLMS SRS; and 26 in the CRUISE SRS» | **Verified** | — |
| 43 | Команды находят 24–57% | там же, Table III | Средние по методу × спецификации: WLMS .43 / .41 / .57; Cruise .31 / **.24** / .45 | **Verified** | — |
| 44 | Собрание команды даёт нулевой чистый прирост | там же | «Collection meetings produced no net improvement in the fault detection rate — meeting gains were offset by meeting losses.» | **Verified (дословно)** | — |
| 45 | «24–57% — доля от известных дефектов, **заложенных в документ заранее**» | там же | «No faults were intentionally seeded into the specifications. All faults are naturally occurring.» | **Wrong — и противоречит вашему же §7** | **ОБЯЗАТЕЛЬНО.** Статья цитирует эту же фразу в финале как аргумент. Правка: «24–57% — доля от дефектов, которые в документе **уже знали** (их нашли и каталогизировали заранее, а не подсадили); про неизвестные эксперимент молчит» |
| 46 | Фейган: инспекции забирают 20–30% усилий первой половины разработки | [Fagan02.pdf](https://eden.dei.uc.pt/~mvieira/Fagan02.pdf) | «**They note that** inspections use 20 - 30% of the effort during the first half of product development and, they fear, this will add to the development cycle… **Although experience has shown this concern to be a myth**…» | **Verified с оговоркой по атрибуции** | Фейган пересказывает возражение практиков и тут же называет страх мифом. Правка: «Цену называют сами скептики, и Фейган её в ретроспективе не оспаривает: 20–30% усилий первой половины разработки» |
| 47 | Крупнейший датасет — 4316 ADR из 547 проектов — устаревание не меряет, авторы признают | [arXiv:2609.07375](https://arxiv.org/html/2609.07375), 07.09.2026 | «dataset consists of 4316 ADRs from 547 (unique) projects»; «**Since our analysis does not focus on temporal evolution**, …» | **Verified частично** | «Крупнейший» — **Not verified** (превосходная степень ниоткуда). Плюс контекст: «given that 40% of the projects are from 2020 (the last year of the dataset)» — корпус доведён до 2020 года. Правка: убрать «крупнейший», добавить «корпус доведён до 2020 года» |
| 48 | Google TSE 2021: 16,9 млн мутантов, >24 тыс. разработчиков | [arXiv:2102.11378](https://arxiv.org/abs/2102.11378) | «The mutant dataset contains 16,935,148 mutants across 10 programming languages»; «used by more than 24,000 developers on more than 1,000 projects» | **Verified** | — |
| 49 | До фильтрации 85% бесполезны, после — 82% полезны | там же | «developers at Google initially classified 85% of reported mutants as unproductive»; «82% of all surfaced mutants with feedback were labeled as productive by developers» | **Verified** | — |
| 50 | Доводка заняла шесть лет ручных правил под каждый язык | там же | «Over the past six years, we have developed a scalable mutation testing approach and mutant suppression rules that increased the ratio of productive mutants … from 15% to 89%»; правила «curated manually for each programming language» | **Verified** | — |
| 51 | Мутационный балл Google отверг — «ни конкретно, ни применимо к действию» | там же | «we were also unable to find a good way to surface it to the developers in an actionable way, as it is neither concrete nor actionable, and it does not guide testing» | **Verified** | — |
| 52 | 3,9% ссылок устарели (7910 из 201 852), затронуты 28,9% проектов | [arXiv:2212.01479](https://arxiv.org/abs/2212.01479) | «In the top1000 dataset, 3.9% (7910/201852) of the code element references detected are currently outdated… 28.9% (265/918) of the projects contain at least one outdated document» | **Verified** | Стоит назвать датасет: это top1000, у google-датасета там же 2,7% / 5,4% |
| 53 | **Медианный** возраст устаревания — 4,7 года | там же | «**On average**, the references are currently outdated for 4.7 years for projects in the top1000 dataset»; и в резюме RQ1: «with the references outdated for 4.7 and 4.2 years **on average** respectively» | **Wrong** | **ОБЯЗАТЕЛЬНО.** Это **среднее**, не медиана. Заменить «медианный» на «средний». (Это то расхождение, которое писатель вынес на проверку — трасса `stage-controls.md` права, текст нет.) |
| 54 | MSR 2024: 10 проектов, 2237 gap mutants, 0,11–23,50%, 69% детерминированных | [msr2024_zeng.pdf](https://rebels.cs.uwaterloo.ca/papers/msr2024_zeng.pdf) | «Our analysis of ten open-source projects uncovers 2,237 gap mutants… the gap mutants account for 0.11%–23.50% of the studied mutants… 69% of gap mutants survive CI acceleration due to deterministic reasons that can be classified into six fault patterns» | **Verified** | — |
| 55 | Martin & Xie, WWW 2007: 11 политик, 906 мутантов | [paper447.pdf](https://archives.iw3c2.org/www2007/papers/paper447.pdf), Table 2 и Table 4 | «We used 11 XACML policies collected from three different sources as subjects». Сумма колонки «# Mut» в Table 4 = 906 | **Verified** | — |
| 56 | **98,6% структурного покрытия при 47% убитых мутантов** | там же, Table 3 и Table 4 | Table 3, строка «average»: 98.60% (Pol %) и 98.60% (Rule %) — это набор запросов **Cirg**. Table 4, строка «average»: Random **47.07%**, Selected Random 38.27%, **Cirg 59.00%**. У Random покрытие — 90.91% / 88.81% | **Wrong** | **ОБЯЗАТЕЛЬНО — цифры из двух разных наборов запросов.** Честные пары: «98,6% покрытия при 59% убитых мутантов» (Cirg) **или** «90,9% покрытия при 47,1% убитых» (Random). Первая пара сильнее для вашего тезиса. Добавить можно и то, что у Cirg покрытие условий — всего 21,21% |
| 57 | Вывод авторов: высокое покрытие не означает способности находить дефекты | там же | «although structural coverage is indeed correlated to fault-detection capability, structural coverage is not strong enough to achieve an acceptable level of fault detection» | **Verified (пересказ точен)** | Слово «дословно» в тексте лучше снять — это пересказ, не цитата |
| 58 | SRE Workbook: при цели 90% и пороге «2% бюджета за час» стопроцентный отказ съедает 1,4% → «этот алерт не смог бы сработать никогда» | [sre.google/workbook/alerting-on-slos](https://sre.google/workbook/alerting-on-slos/) | «Because a 100% outage consumes only 1.4% of the budget in that hour, this alert could never fire.» | **Verified (дословно)** | — |
| 59 | «**Там же** прямо сказано: код мониторинга — по тем же стандартам тестирования… широко принятой системы нет» | [sre.google/workbook/monitoring](https://sre.google/workbook/monitoring/) — **другая глава** | «In an ideal world, monitoring and alerting code should be subject to the same testing standards as code development.»; «While Prometheus developers are discussing developing unit tests for monitoring, there is currently no broadly adopted system that allows you to do this.» | **Verified по содержанию, Wrong по ссылке** | **ОБЯЗАТЕЛЬНО.** Две разные главы. Поставить вторую ссылку и **датировать цитату**: книга 2018 года, а `promtool test rules` появился позже — иначе читатель решит, что канон не знает про инструмент, который вы сами абзацем выше и рекомендуете. Правка: «И там же, в главе про мониторинг (книга 2018 года, до появления `promtool test rules`): …» |
| 60 | Gandalf отчитывается полнотой 100%, определённой как «ни один высокоимпактный инцидент не вызван плохой выкаткой» | [nsdi20spring_li_prepub.pdf](https://www.usenix.org/system/files/nsdi20spring_li_prepub.pdf) | «achieved a precision of 92.4% with 100% recall (no high-impact incidents were caused by bad rollouts)» | **Verified** | 100% — для **раннего этапа data-plane выкаток**; на другом этапе работа даёт 94,9% / 99,8%. Добавить «на одном из этапов» |
| 61 | Слов «inject», «synthetic», «seed» в работе нет вовсе | там же | Извлечённый текст PDF (1590 строк): 0 вхождений каждого из трёх слов | **Verified this run** | — |

---

## §5. Файл инструкций

| # | Утверждение | Источник | Цитата | Вердикт | Правка |
|---|---|---|---|---|---|
| 62 | 1650 сессий, 16 050 наблюдений на уровне функции, две кодовые базы | [arXiv:2605.10039](https://arxiv.org/abs/2605.10039), Damon McMillan, 11.05.2026 | «1,650 Claude Code CLI sessions (16,050 function-level observations) on two TypeScript codebases, three frontier models» | **Verified** | Можно добавить, что кодовые базы — TypeScript, а моделей три |
| 63 | Без файла 0 раз из 524, верхняя граница 0,73% | там же, §4.3 | «The no-configuration baseline (BL-01) produced 0 compliant functions out of 524 across 50 runs (ICR = 0.0%; Wilson 95% upper bound 0.73%)» | **Verified** | — |
| 64 | С файлом — 67,7% (n=529) | там же | «the matched with-configuration condition ME-03 (n = 529, ICR = 67.7%)» | **Verified** | — |
| 65 | Ни размер (25–500 строк), ни позиция, ни дробление эффекта не дают | там же | «file size 25 to 500 lines»; «None of the four structural variables or three two-way interactions produces a detectable contrast after multiple-testing correction» | **Verified** | — |
| 66 | Соблюдение падает **на 5,6% с каждой следующей функцией**; отсюда — «гоняйте до конца длинной сессии, первая функция ничего не доказывает» | там же | «approximately 5.6% lower **odds** of compliance per generation step (OR = 0.944), **though the relationship is non-monotonic rather than a constant per-step effect**… **a substantial share of the attenuation concentrates in the first three to four generated functions (median first omission at generation position 4)** rather than accumulating gradually» | **Wrong в практическом выводе** | **ОБЯЗАТЕЛЬНО.** Два расхождения. (1) 5,6% — это **шансы (odds)**, а не вероятность; (2) источник прямо говорит, что падение **не** накапливается постепенно, а сосредоточено в первых трёх-четырёх функциях (медиана первого нарушения — позиция 4). Совет «гоняйте до конца длинной сессии, первая функция — самая лёгкая проверка» ровно наоборот: проверка ломается уже на четвёртой. Правка: «…шансы соблюдения падают примерно на 5,6% с каждой следующей функцией, причём падение не растянуто — большая его часть приходится на первые три-четыре функции, медиана первого нарушения — четвёртая. Практический вывод: гонять минимум до пятой-шестой функции; одной функции мало» |
| 67 | Препринт одного автора, без рецензирования | там же | Единственный автор — Damon McMillan; arXiv-препринт | **Verified** | — |
| 68 | 481 CLAUDE.md: только 4,4% правил безопасности (ДИ 2,6–6,7%) имеют принуждающий контроль | [arXiv:2608.23550](https://arxiv.org/abs/2608.23550), Ting Yan, 24.08.2026 | 481 файл; «4.4% (95% CI: 2.6-6.7%)» при **строжайшем** критерии совпадения; «approximately 4-16% … depending on matching strictness» | **Verified, но выбрана крайняя точка** | 4,4% — нижний край диапазона 4–16%. Правка: «…4,4% (ДИ 2,6–6,7%) при самом строгом критерии совпадения — и до 16% при мягком» |
| 69 | «разработчик пишет правило безопасности и не получает никакой обратной связи о том, будет ли хоть что-то его обеспечивать» | там же | «a developer writes a security rule but gets no feedback on whether a control will enforce it» | **Verified (дословно)** | — |
| 70 | 2303 файла из 1925 репозиториев | [arXiv:2511.12884](https://arxiv.org/abs/2511.12884), «Agent READMEs» | «2,303 agent context files from 1,925 repositories» | **Verified** | — |
| 71 | Ни одно из двух корпусных исследований **не нашло** в репозиториях тестов на сами правила | arXiv:2511.12884 + [arXiv:2512.18925](https://arxiv.org/abs/2512.18925) («Beyond the Prompt», 401 репозиторий с cursor rules) | В полном тексте «Agent READMEs» слово «enforce» не встречается ни разу; вопрос о проверке самих правил там не ставится. «Beyond the Prompt» — таксономия содержания правил на 401 репозитории | **Not verified (не нулевой результат, а незаданный вопрос)** | **ОБЯЗАТЕЛЬНО.** «Не нашло» читается как измеренный ноль. Правка: «Ни одно из двух корпусных исследований файлов инструкций … вопроса о тестах на сами правила не ставит вовсе. Правил много, обратной связи по ним нет — и мерить её пока никто не пробовал». Заодно снять «второе» как безымянное: у него другой предмет (cursor rules, 401 репозиторий) |

---

## §6. Развязка: генератор дефекта вне кода

| # | Утверждение | Источник | Цитата | Вердикт | Правка |
|---|---|---|---|---|---|
| 72 | 851 реальный баг с контролем утечки обучающих данных | [arXiv:2406.09843](https://arxiv.org/abs/2406.09843) (v5, TOSEM) | «851 real bugs from two Java real-world bug benchmarks (i.e., 605 bugs from 12 projects of Defects4J 2.0 and 246 bugs of ConDefects)»; «To prevent data leakage, we use data from the four most recent months following the release of the LLMs» | **Verified** | Есть авторская оговорка, которой в тексте нет: «only the most recent model, DeepSeek-V3-731b, cannot guarantee data leakage-free». Полстроки стоит |
| 73 | LLM-мутанты обнаруживают дефекты в 76,5% случаев против 44,2% | там же, аннотация | «LLM-based approaches reach a detection rate of 76.47%, compared to 44.15% for rule-based techniques» | **Verified** | В теле работы (Answer to RQ1) базовая линия взвешена иначе — 41,64%. Цифра 44,2% законна (это аннотация), но если кто-то откроет RQ1, он увидит другое число. Сноска не помешает |
| 74 | Сцепленность 51,5% против 24,4% | там же, Answer to RQ1 | «real bug detection rate and coupling rate are 41.64% and 24.37%… LLM-based approaches reach 76.47% and 51.54%» | **Verified** | Пара 51,54/24,37 идёт из RQ1, где базовая линия — 41,64%. Смешение с 44,15% из аннотации технически допустимо, но лучше взять одну пару |
| 75 | 49 типов синтаксических узлов против двух | там же | «LLMut (DS-236b) and LLMut (DS-671b) … newly introducing 49 different AST node types. In comparison, rule-based approaches like Major introduce only 2 new node types» | **Verified** | — |
| 76 | ACH: 10 795 классов, 31 677 сгенерированных дефектов, 9095 (29%) собираются | [arXiv:2501.12862](https://arxiv.org/abs/2501.12862), Table 2 | Totals: 10,795 / 31,677 / 9,095 (29%). Текст: «ACH generates 9,095 mutants that **build and pass** from 10,795 classes under test» | **Verified** | Точнее «собираются и проходят тесты» |
| 77 | **571 тест заведён в продакшен** / «571 тест в продакшене на выходе» | там же | «ACH was able to generate an additional 571 unit tests» — это **сгенерированные** тесты. Про продакшен сказано только: «All tests that were acceptable for usefulness were landed into production» — а отсмотрен был 191 тест, принято 140 | **Wrong** | **ОБЯЗАТЕЛЬНО.** Правка: «…и 571 тест на выходе. В продакшен из них доехали те, что прошли ручной смотр: из 191 отсмотренного инженерами приняли 140». Воронку это не ослабляет — наоборот, делает честнее |
| 78 | Из 191 теста 73% приняты, 36% релевантны приватности | там же, Table 4 | Overall Total: 191 отсмотрено на полезность, 140 принято / 51 отклонено → 73% / 27%. «only approximately 36% were deemed to be either possibly or definitely related to privacy» | **Verified** | 36% считается от 175 тестов, отсмотренных на релевантность, а не от 191. Полстроки |
| 79 | 277 из 571 (49%) тестов, уникально убивающих мутанта, не добавляют ни строки покрытия | там же, Table 8 | «Of these 571 tests, 277 would have been discarded had we chosen to focus solely on the line coverage test adequacy criterion»; «a large proportion (49%) of test cases that uniquely additionally kill a mutant, do not also add line coverage» | **Verified** | — |
| 80 | Промпт ACH: «a typical bug that introduces a privacy violation similar to {diff}» | там же | «…version of that method that contains a typical bug that introduces a privacy violation similar to {diff}» | **Verified (дословно)** | — |
| 81 | «we have no way to consistently and reliably measure problem similarity or relevance» | там же, Mutant Relevance | «One difficulty here is that we have no way to consistently and reliably measure problem similarity or relevance.» | **Verified (дословно)** | — |
| 82 | Just и соавторы, FSE 2014: 357 дефектов, 321 тыс. строк, 17% не сцеплены, «mostly involving algorithmic changes or code deletion» | [mutants_real_faults_fse_2014.pdf](https://homes.cs.washington.edu/~rjust/publ/mutants_real_faults_fse_2014.pdf) | «Our experiments used 357 real faults in 5 open-source applications that comprise a total of 321,000 lines of code»; «However, 17% of real faults, mostly involving algorithmic changes or code deletion, are not coupled to any mutants» | **Verified (дословно)** | — |
| 83 | Доля удаляющих мутаций у LLM — 0,1–5,5% против 15,3% | [arXiv:2406.09843](https://arxiv.org/abs/2406.09843), таблица распределения и RQ1 | «all LLM-based approaches generate deletion mutants at a rate below 6%»; таблица даёт значения от 0,1% до 5,5%; «0.3% for LLMorpheus (GPT-4o) versus 15.3% for Major» | **Verified** | — |
| 84 | 34 участника, crossover, байесовский анализ: LLM ухудшил обнаружение, время не сократил; оговорка про начинающих | [arXiv:2608.21298](https://arxiv.org/abs/2608.21298), 21.08.2026 | «controlled crossover design experiment with 34 participants»; «one Bayesian regression model per outcome variable»; «LLM support negatively affects smell detection accuracy but has no significant effect on smell classification or task duration»; «may, instead, hinder it for novice inspectors» | **Verified** | Предмет — обнаружение **requirements smells**, не «дефектов» в общем смысле. Одно слово |
| 85 | «За пределами кода работ ноль… Единственная мутация не-кодового артефакта — исполняемая модель» | — | Утверждение об отсутствии; отдельным поиском не подтверждается и не опровергается | **Not verified** | Смягчить до «мы таких работ не нашли» — статья сама учит не выдавать молчание за сигнал |

---

## §7. Три способа и понедельник

| # | Утверждение | Источник | Цитата | Вердикт | Правка |
|---|---|---|---|---|---|
| 86 | PCAOB-2024: дефициты 39%, у крупной четвёрки 20%, у мелких триеннальных 61% | [PCAOB Spotlight, март 2025](https://pcaobus.org/documents/staff-update-2024-inspection-activities-spotlight.pdf) | «the aggregate Part I.A deficiency rate decreased to 39% in 2024»; «for the Big Four U.S. firms … decreased to 20% in 2024»; «Aggregate deficiency rates at **NAF** triennially inspected firms decreased from 67% in 2023 to 61% in 2024, **and GNF triennially inspected firms decreased from 35% in 2023 to 26%**» | **Verified с оговоркой** | 61% — только у не-аффилированных фирм триеннального цикла; у сетевых триеннальных 26%. Правка: «…у не-аффилированных фирм триеннального цикла — 61%» |
| 87 | «Знаменатель важен: выборка инспекций отбирается **по риску, а не случайно**» | там же | «we use a **risk-based and random-based** selection process»; и раздельная отчётность: «In 2024, 76% of the **randomly selected** public company audit engagements resulted in at least one deficiency»; «74% … of our **risk-based** public company audit selections» | **Wrong** | **ОБЯЗАТЕЛЬНО** (это третье расхождение, вынесенное на проверку — оговорка из трассы не верна). PCAOB отбирает **и по риску, и случайно**, и отчитывается по обеим ветвям отдельно. Правка: «Знаменатель важен: часть заданий PCAOB отбирает по риску, часть случайно, и отчитывается по этим ветвям отдельно — агрегированные 39% смешивают обе» |
| 88 | **NIST GMP 11** объявляет формулировку «калибруем по необходимости» неприемлемой | [NIST IR 6969-2019](https://doi.org/10.6028/NIST.IR.6969-2019) | Фраза «Statements such as "calibration as needed" are unacceptable for both laboratory measurement equipment and measurement standards» стоит в **GLP 4 – 2019**, стр. 2, а не в GMP 11 | **Wrong (атрибуция раздела)** | **ОБЯЗАТЕЛЬНО.** Правка: «NIST IR 6969: GLP 4 объявляет формулировку «калибруем по необходимости» неприемлемой, а GMP 11 выводит интервал из целевой надёжности» |
| 89 | …и выводит интервал проверки из целевой надёжности | там же, GMP 11, §2.3.2.1–2.3.2.2 | «calibration intervals are determined to meet a 99 % reliability target» (критические параметры); «designed to meet a 95 % reliability target» (вторичные) | **Verified** | — |
| 90 | IEC 61508/61511 выражают это формулой `PFDavg ≈ λ_DU·T₁/2` | [61508.org, SIL Calculations](https://61508.org/wp-content/uploads/2024/11/10B-SIL-Calculations-and-use-of-IEC-61508-6.pdf) | В источнике для 1oo1: `PFD = (λ_DU + λ_DD)·t_CE`, где `t_CE` содержит `T1/2 + MRT`. Упрощения до `λ_DU·T₁/2` в цитируемом документе нет | **Inferred** | Это стандартное упрощение при пренебрежимых λ_DD и MRT, но подано как цитата стандарта. Правка: «…и в упрощённом виде для одноканальной схемы даёт `PFDavg ≈ λ_DU·T₁/2`» |
| 91 | Формула описывает случайные аппаратные отказы | там же | Заголовок раздела: «Quantifying Random Hardware Failures. IEC 61508-6:2010 Annex B: Examples of Technique for Evaluating Probabilities of Hardware Failure» | **Verified** | — |
| 92 | «Ошибки ПО тот же стандарт относит к систематическим и вероятностью принципиально не описывает» | там же | Слово «systematic» в цитируемом документе не встречается ни разу | **Not verified по этой ссылке** | Утверждение по сути верно для IEC 61508 (Part 3, systematic capability), но цитируемый источник его не несёт. Либо дать вторую ссылку, либо снять «тот же стандарт» и написать «IEC 61508 в части ПО» |
| 93 | Мета-исследование на 142 мета-анализах и 1153 РКИ не нашло средней разницы; два объяснения; ослепление рекомендуют сохранить | [BMJ 2020;368:l6802](https://doi.org/10.1136/bmj.l6802) (проверено по копии James Lind Library) | «The study included 142 meta-analyses (1153 trials)»; «No evidence was found for an average difference in estimated treatment effect between trials with and without blinded patients, healthcare providers, or outcome assessors. These results could reflect that blinding is less important than often believed **or** meta-epidemiological study limitations, such as residual confounding or imprecision. At this stage, replication of this study is suggested and blinding should remain a methodological safeguard in trials.» | **Verified (дословно, всё три части)** | — |
| 94 | «No faults were intentionally seeded… All faults are naturally occurring» | Porter/Votta/Basili | «No faults were intentionally seeded into the specifications. All faults are naturally occurring.» | **Verified (дословно)** | — |
| 95 | Утверждения об отсутствии: «доли неверных примеров в doctest-проектах не мерил никто»; «никто не меряет долю политик, которые ни разу ничего не заблокировали»; «доли правил, покрытых тестами алертинга, не мерил никто» | — | Проверке поддаётся только отрицательно | **Not verified** | Не ошибки, но каждое стоит перевести из «никто не мерил» в «мы таких измерений не нашли». Три штуки — можно одной сквозной формулировкой |

---

## Что надо снять или переписать до отправки дальше (16 пунктов)

**Меняют смысл — без правки нельзя:**

1. **#53 — «медианный» → «средний».** Источник: «On average, the references are currently outdated for 4.7 years». Одно слово.
2. **#56 — WWW 2007: 98,6% и 47% из разных наборов запросов.** Честно: 98,6% покрытия → 59% убитых (Cirg), либо 90,9% → 47,1% (Random).
3. **#30 — 25,92% приписано не той работе.** Цифра из arXiv:2605.02273, а не 2607.13196.
4. **#77 — «571 тест заведён в продакшен».** 571 — сгенерированные тесты; отсмотрен 191, принято 140.
5. **#13 — DORA-2025 по стабильности.** Отчёт 2025 воспроизводит направление находки («AI is associated with an increase in software delivery instability»). Сейчас текст сообщает только про разворот по пропускной способности, и это выглядит как умолчание в свою пользу.
6. **#45 — «дефектов, заложенных в документ заранее».** Прямо противоречит цитате, которую статья сама приводит в финале.
7. **#87 — PCAOB «по риску, а не случайно».** Отбор и по риску, и случайный, с раздельной отчётностью.
8. **#88 — «GMP 11» → «GLP 4»** для фразы про «калибруем по необходимости».
9. **#59 — «Там же» про стандарты тестирования мониторинга.** Другая глава SRE Workbook; и нужна дата (2018), иначе цитата спорит с `promtool`, который вы рекомендуете абзацем выше.
10. **#66 — 5,6% за функцию.** Это шансы, и падение сосредоточено в первых 3–4 функциях. Совет «гоняйте до конца длинной сессии» источнику противоречит.
11. **#71 — «не нашло тестов на сами правила».** Ни одна из двух работ такого вопроса не задавала.
12. **#33 — Миллз.** Он оценивал остаток дефектов в артефакте; «о чувствительности контроля, а не о качестве артефакта» — переворот. Плюс нужна ссылка.
13. **#24 — RAMP.** Потеряны условие «среди agent-first репозиториев» и авторская рамка «hypothesis-generating».
14. **#38 — Tricorder «нет права вето».** Источник прямо описывает обратное.
15. **#39 — NFPA 72 «дым физически вошёл в камеру».** В цитируемом документе этой формулировки нет.
16. **#92 — «тот же стандарт относит ошибки ПО к систематическим».** В цитируемом источнике слова «systematic» нет.

**Снимать совсем не нужно ничего.** Все шестнадцать — правки формулировки, ссылки или оговорки;
ни одно несущее утверждение не оказалось выдуманным, ни одна ссылка не битая.

---

## Флаги (не блокируют, но роаст спросит)

- **#31** — стейлмен про ревью берёт только пересечение репозиториев. В полной популяции 61,38% агентских PR не получают ревью вообще, а в самом пересечении лишь 8,08% ревью агентских PR — чисто человеческие (против 25,21% у человеческих). Ваша же мысль от этого только выигрывает.
- **#68** — 4,4% это нижний край диапазона 4–16%, зависящего от строгости сопоставления. Взята крайняя точка без диапазона — ровно тот жанр, который статья критикует.
- **#27** — «22,7% из них» читается как «из коммитов»; в источнике это доля прослеженных находок.
- **#47** — «крупнейший датасет» ничем не подтверждено; корпус ADR доведён до 2020 года.
- **#60** — полнота Gandalf 100% относится к одному этапу выкаток; на другом 99,8%.
- **#73/#74** — в работе две разные базовые линии для классических операторов (44,15% в аннотации, 41,64% в RQ1). Текст берёт одну для детекта и другую пару для сцепленности.
- **#86** — 61% относится только к не-аффилированным триеннальным фирмам.
- **#46** — 20–30% у Фейгана — пересказ возражения практиков, а не его собственная оценка цены.
- **#78** — 36% релевантных приватности считаются от 175, не от 191.
- **#90** — `PFDavg ≈ λ_DU·T₁/2` — стандартное упрощение, а не формула из цитируемого документа.
- **#8/#9** — оценки DORA-2024 байесовские, с 89%-ми интервалами неопределённости, и размер ИИ-подвыборки в отчёте не назван. У чисел −1,5 / −7,2 точного знаменателя нет. Статья это не скрывает, но и не говорит.
- **#95** — четыре утверждения об отсутствии («никто не мерил», «работ ноль») стоит перевести в «мы не нашли».

**Противоречий с `wiki/topics/anti-patterns.md` и прошлыми пиесами не найдено.** Наоборот: пункты
#68, #27, #86 — ровно тот антипаттерн «цифра без знаменателя», который там записан, и в этих трёх
местах статья сама в него наступает.

---

VERDICT: **16 claims must be fixed** (все — формулировка/ссылка/оговорка, ни одной выдуманной
цитаты и ни одной битой ссылки). После правок текст можно вести в роаст.

---

## Раунд 2: fitness-функции (абзац «Архитектура и ADR», ru.md, стр. 249–259)

Проверен ровно один абзац — тот, что остался нерезолвленным после раунда 1. Всё, что закрыто выше,
не переоткрывалось. Метод: подтверждено только то, что я открыл сам; для каждой ссылки ниже
проверен HTTP-статус.

| # | Утверждение в статье | Источник (резолвнутая ссылка) | Дословно | Вердикт | Заметка |
|---|---|---|---|---|---|
| F1 | «Практику ввели Нил Форд, Ребекка Парсонс и Патрик Куа в „Building Evolutionary Architectures" (2017)» | OpenLibrary, запись произведения: <https://openlibrary.org/works/OL19541931W> (HTTP 200) | `title: Building Evolutionary Architectures: Support Constant Change`, `author_name: ['Neal Ford', 'Rebecca Parsons', 'Patrick Kua']`, `first_publish_year: 2017` | **Verified this run** | Издатель O'Reilly, ISBN-13 978-1-4919-8636-3. 2-е издание — 2022/2023, там добавлен четвёртый автор, Прамод Садаладж. Канонический URL главы на oreilly.com отдаёт **403** — инлайном его ставить нельзя. |
| F2 | То же, подтверждение из независимого источника + дата попадания в отраслевой оборот | Thoughtworks Technology Radar, блип «Architectural fitness function»: <https://www.thoughtworks.com/radar/techniques/architectural-fitness-function> (HTTP 200) | «Borrowed from evolutionary computing, a fitness function is used to summarize how close a given design solution is to achieving the set aims. <…> An architectural fitness function, **as defined in Building Evolutionary Architectures**, provides an objective integrity assessment of some architectural characteristics, which may encompass existing verification criteria, such as unit testing, metrics, monitors, and so on.» | **Verified this run** | Блип впервые — **Nov 2017**, кольцо **Trial**; переподтверждён **May 2018**, то же кольцо; страница помечена «NOT ON THE CURRENT EDITION», last updated May 15, 2018. То есть за восемь лет Radar так и не вывел практику из Trial. Смежный блип «Evolutionary architecture» есть на Radar с **Jan 2010**, но fitness-функции в нём не упоминаются — то есть датировка «2017» для самой практики корректна. |
| F3 | «архитектурное требование формулируется как **исполняемая** проверка» | Гл. 2, «What is a Fitness Function?» (текст 1-го издания, зеркало: <https://ebrary.net/53995/economics/what_fitness_function>, HTTP 200) | «the fitness functions for evolutionary architecture **may not be implementable in software** (e.g., a required manual process for regulatory reasons), but architects must still define **manual fitness functions** <…> While automated checks are preferable, some projects cannot automate all fitness functions.» И: «Developers commonly express fitness functions using different kinds of mechanisms, such as **tests or metrics**.» | **Wrong (сужение)** | У авторов определение шире: фитнес-функция необязательно исполняемая и необязательно автоматическая. «Automated Versus Manual» — одна из семи заявленных категорий. |
| F4 | «архитектура жива ровно в той мере, в какой эти проверки прогоняются» | там же | Ближайшее, что есть: «The fitness functions **collectively denote what matters to us in our architecture**, allowing us to make the kinds of trade-off decisions that are both crucial and vexing» и «**Not all tests are fitness functions, but some tests are** — if the test helps verify the integrity of architectural concerns, we consider it a fitness function.» | **Not verified** | Формулы «архитектура жива ровно в той мере» в источнике нет — это авторская компрессия. Ближайшее *чужое* утверждение такого регистра — не у Форда, а в блипе Radar: «We **believe** architects can communicate, validate and preserve architectural characteristics in an automated, continual manner, which is the key to building evolutionary architectures». Это декларация веры Thoughtworks, не измерение. Либо снять, либо атрибутировать. |
| F5 | «В репозитории это обычный тест рядом с кодом, запускаемый в CI» | Гл. 2, «Categories / Atomic Versus Holistic»: <https://ebrary.net/53996/economics/categories>; «Static Versus Dynamic, Automated Versus Manual»: <https://ebrary.net/53998/economics/static_versus_dynamic> (оба HTTP 200) | «Atomic fitness functions run against a singular context <…> An excellent example of an atomic fitness function is **a unit test that verifies some architectural characteristic, such as modular coupling** <…> but **not all unit tests serve as fitness functions — only the ones that verify architecture characteristic(s)**.» «developers will execute most fitness functions within an automated context: **continuous integration, deployment pipelines**, and so on.» | **Verified this run — но только для одного подвида** | Описание точно попадает в atomic + triggered + static + automated. Полная авторская классификация — **семь осей**: Atomic/Holistic, Triggered/Continual, Static/Dynamic, Automated/Manual, Temporal, Intentional over Emergent, Domain-specific. Нужна оговорка «самый ходовой вид», иначе абзац выдаёт одну клетку за всю таблицу. |
| F6 | Пример «модуль оплаты не импортирует модуль отчётности» | там же + оглавление книги (раздел «Guarding Against Component Cycles») | «a unit test that verifies some architectural characteristic, such as **modular coupling**» | **Verified this run** | Жанр совпадает с авторским примером. |
| F7 | Пример «циклических зависимостей между пакетами нет» | Оглавление 1-го издания: раздел **«Guarding Against Component Cycles»** (глава про архитектурную связанность) | заголовок раздела дословно | **Verified this run** | Циклы компонентов — прямо названная авторами мишень. |
| F8 | Пример «время ответа на 95-м перцентиле не больше 300 мс» — **в составе перечня «обычный тест в CI»** | Гл. 2, «Triggered Versus Continual»: <https://ebrary.net/53997/economics/triggered_versus_continual> (HTTP 200); и «What is a Fitness Function?» | Про перформанс: «Consider a requirement that **all service calls must respond within 100ms**. We can implement a test (i.e., fitness function) that measures the response <…>». Но про транзакционное время: «**instead of using a triggered test**, developers build a fitness function that **simulates a transaction in production** while all the other real transactions run <…> Monitoring-driven development (MDD) <…> These **continual** fitness functions are more dynamic than standard triggered tests.» | **Wrong (не туда положено)** | Сам порог «p95 ≤ 300 мс» — легитимная фитнес-функция и точный аналог авторского «100 ms». Но авторы такие проверки относят к **continual** — они живут в мониторинге прода, а не в сборке. В статье пример стоит третьим в списке «обычный тест … запускаемый в CI» — и это ровно та путаница, которую книга разводит явно. |
| F9 | **«Сравнительных измерений эффекта мы не нашли <…> нет числа»** | (1) Knodel, Muthig, Rost, ICSM 2008, DOI [10.1109/ICSM.2008.4658077](https://doi.org/10.1109/ICSM.2008.4658077) (HTTP 202; абстракт резолвнут через OpenAlex: `https://api.openalex.org/works/doi:10.1109/ICSM.2008.4658077`), открытый пересказ с числом: <https://fb-swt.gi.de/fileadmin/FB/SWT/Softwaretechnik-Trends/Verzeichnis/Band_29_Heft_2/06-knodel.pdf> (HTTP 200, PDF прочитан целиком). (2) Olsson, Toll, Ericsson, Wingkvist, ECSA-W 2016, DOI 10.1145/2993412.3003391; открытая карточка с абстрактом: <https://urn.kb.se/resolve?urn=urn:nbn:se:lnu:diva-60472> (HTTP 200) | (1) Абстракт ICSM 2008: «An experiment with **six component development teams** gives evidence that this training pro-actively prevents architecture decay. **The three teams supported by the live compliance checking inserted about 60% less structural violations** into the architecture than did the three other development teams.» Он же, открытый PDF Knodel: «the number of architecture violations was, after an initial peak, **almost constantly 60% lower in the group that was supported by SAVE LiFe, compared to the control group** <…> **All teams invested approximately the same development effort**». (2) Абстракт ECSA-W 2016: «The service was evaluated in a **field experiment that consisted of eight student projects**. We found that **the four projects that used the service produced significantly fewer violations** compared to those that did not.» | **Wrong как написано** | Под самим именем «fitness function» измерений действительно нет (см. следующую строку). Но **механизм** — автоматическая проверка архитектурного правила прямо в рабочем цикле — измерен сравнительно **дважды**, и оба раза со свидетельством в пользу. Обе работы старше термина (2008 и 2016) и слова «fitness function» не употребляют — вот почему поиск по имени их не находит. Утверждение «нет числа» в текущей редакции просто неверно. |
| F10 | То же, но в узком чтении: «нет измерений **под именем fitness function**» | Отрицательные результаты поиска, выполненные в этом прогоне | Semantic Scholar `paper/search?query=architectural fitness function` → пустой `data`; запросы «fitness functions evolutionary architecture» / «evolutionary architecture fitness function case study» дают только генетические алгоритмы и NAS, ни одной работы по архитектурному управлению. Единственная академическая работа, употребляющая термин в нужном смысле, — [«Sustaining Research Software: A Fitness Function Approach», arXiv:2509.10085](https://arxiv.org/abs/2509.10085) (HICSS), и она **предлагает** набор фитнес-функций под FAIR, контрольной группы не имеет. SLR/мэппинга по теме не существует. | **Verified this run (отрицательный результат)** | Знаменатель отрицания честный: три поисковых системы (Semantic Scholar API, веб-поиск, arXiv через веб), плюс отдельная проверка по ArchUnit — эмпирики, меряющей эффект внедрения ArchUnit, тоже нет. |
| F11 | «у практики есть авторы, формулировка и **инструменты**» — инструмент не назван | ArchUnit, официальный сайт: <https://www.archunit.org/> (HTTP 200) | «ArchUnit is a **free, simple and extensible library for checking the architecture of your Java code using any plain Java unit test framework**. That is, ArchUnit can check **dependencies between packages and classes, layers and slices, check for cyclic dependencies** and more. It does so by analyzing given Java bytecode». Слоган сайта: «Unit test your Java architecture». | **Verified this run** | В абзаце (и во всём `ru.md` — проверено grep'ом) **ArchUnit не упоминается ни разу**. Слово «инструменты» висит без единого примера. ArchUnit — ровно то, чем его обычно называют: Java-библиотека, гоняющая архитектурные правила как обычные юнит-тесты; оба первых примера статьи (импорт между модулями, циклы между пакетами) — буквально её штатные проверки. Есть порт для .NET/C#. |

### Must fix before ship

- **F9 — «Сравнительных измерений эффекта мы не нашли <…> нет числа».** Неверно. Два сравнительных
  замера существуют и оба резолвятся. Это единственная правка в абзаце, которая меняет смысл, а не
  формулировку — и меняет его в пользу статьи: появляется число там, где сейчас стоит признание
  в его отсутствии. Оставить как есть нельзя: это ровно тот жанр «мы поискали и не нашли», который
  статья сама разбирает у других.
- **F3 — «формулируется как исполняемая проверка».** Авторы явно оговаривают ручные фитнес-функции.
  Нужна оговорка либо замена на авторское «объективная оценка целостности архитектурной характеристики».
- **F8 — p95 в списке «обычный тест в CI».** Книга относит такие проверки к continual/мониторингу
  и разводит их с triggered-тестами абзацем. Пример надо либо вынести, либо пометить.
- **F4 — «архитектура жива ровно в той мере, в какой эти проверки прогоняются».** В источнике этого
  нет. Либо снять кавычку доверия к источнику (это ваша мысль, не Форда), либо заменить на сорсабельное.

### Флаги

- **F5 / полнота классификации.** У авторов семь осей категорий. Абзац описывает одну клетку
  (atomic + triggered + static + automated) как «это». Достаточно двух слов — «самый ходовой вид».
- **F11 / «инструменты» без примера.** Утверждение об инструментах в абзаце, который именно и
  упрекает практику в бездоказательности, само остаётся без единого имени. ArchUnit закрывает дыру
  одной ссылкой.
- **Знаменатели у новых чисел (обязательно назвать).** 60% — это 3 команды против 3, один
  эксперимент, 2008 год, замер по числу структурных нарушений при примерно равных трудозатратах
  («All teams invested approximately the same development effort»). «Значимо меньше» у Ольссона —
  это 4 студенческих проекта против 4, размер эффекта в абстракте не назван. Подавать их без этих
  цифр — наступить в собственный антипаттерн «цифра без знаменателя»; с ними — это честное
  «дважды посмотрели, и оба раза в нужную сторону», а не «практика работает».
- **Хронология термина.** «Fitness function» заимствован из эволюционных вычислений, и авторы это
  сами проговаривают. «Практику ввели» — корректно; «термин ввели» было бы неверно.
- **Radar застрял в Trial.** Блип не выходил из Trial с ноября 2017 и с мая 2018 не пересматривался
  вовсе. Для абзаца, который спорит о зрелости практики, это сильная и бесплатная деталь.
- **Противоречий с `wiki/topics/anti-patterns.md` не найдено** — упоминаний fitness-функций и
  архитектурного управления там нет.
- **Связь с флагом #95 раунда 1.** Там было предложено перевести утверждения об отсутствии в «мы не
  нашли». Здесь случай хуже: формулировка уже была «мы не нашли», и она всё равно оказалась
  фактически неверной. Вывод для `lessons-learned`: «мы не нашли» — не индульгенция, а обещание, что
  искали; отрицание нужно перепроверять сменой ключевого слова (здесь помог отказ от термина
  «fitness function» в пользу «architecture conformance checking»).

### Готовая правка

Развёрнутый вариант — заменяет всё от «Практику ввели…» до конца абзаца:

> Практику ввели Нил Форд, Ребекка Парсонс и Патрик Куа в
> [«Building Evolutionary Architectures»](https://openlibrary.org/works/OL19541931W) (O'Reilly, 2017);
> тогда же она попала в
> [Technology Radar](https://www.thoughtworks.com/radar/techniques/architectural-fitness-function) —
> в кольцо Trial, откуда с мая 2018 года так и не вышла. Определение у авторов широкое: фитнес-функция
> даёт «объективную оценку целостности какой-то архитектурной характеристики» и может быть тестом,
> метрикой, монитором в проде или даже ручной процедурой. Самый ходовой её вид — обычный тест рядом
> с кодом, запускаемый в CI: «модуль оплаты не импортирует модуль отчётности», «циклических
> зависимостей между пакетами нет»; для Java это [ArchUnit](https://www.archunit.org/). Проверки
> вроде «время ответа на 95-м перцентиле не больше 300 мс» авторы относят к непрерывным — их место
> в мониторинге, а не в сборке.
>
> Под именем «fitness-функция» сравнительных измерений эффекта мы не нашли — ни одной работы с
> контрольной группой. Но сам механизм, автоматическую проверку архитектурного правила прямо в
> рабочем цикле, мерили дважды, и обе работы старше термина.
> [Кнодель, Мутиг и Рост (ICSM 2008)](https://doi.org/10.1109/ICSM.2008.4658077): шесть команд, три
> с живой проверкой в IDE, три без; у поддержанных
> [структурных нарушений «почти постоянно на 60% меньше»](https://fb-swt.gi.de/fileadmin/FB/SWT/Softwaretechnik-Trends/Verzeichnis/Band_29_Heft_2/06-knodel.pdf)
> при примерно равных трудозатратах.
> [Ольссон и соавторы (ECSA-W 2016)](https://urn.kb.se/resolve?urn=urn:nbn:se:lnu:diva-60472):
> восемь студенческих проектов, четыре с сервисом, проверяющим MVC на каждое изменение кода, —
> «значимо меньше нарушений», размер эффекта не назван. Знаменатели тут крошечные: шесть команд и
> восемь студенческих проектов. Это не «практика работает» — это «дважды посмотрели, и оба раза в
> нужную сторону».

Короткий вариант, если абзац нельзя раздувать (заменяет только последнее предложение):

> Под своим именем практика не измерена ни разу. Механизм — автоматическая проверка архитектурного
> правила в рабочем цикле — мерили дважды, до появления термина и на крошечных выборках:
> [шесть команд, 2008](https://fb-swt.gi.de/fileadmin/FB/SWT/Softwaretechnik-Trends/Verzeichnis/Band_29_Heft_2/06-knodel.pdf)
> — у трёх поддержанных структурных нарушений на 60% меньше;
> [восемь студенческих проектов, 2016](https://urn.kb.se/resolve?urn=urn:nbn:se:lnu:diva-60472) —
> у четырёх с автопроверкой «значимо меньше нарушений» без названного размера эффекта.

### Ссылки для инлайна (все проверены на статус в этом прогоне)

| Назначение | URL | HTTP |
|---|---|---|
| Книга (первоисточник практики) | `https://openlibrary.org/works/OL19541931W` | 200 |
| Отраслевая запись практики + определение | `https://www.thoughtworks.com/radar/techniques/architectural-fitness-function` | 200 |
| Инструмент (Java) | `https://www.archunit.org/` | 200 |
| Измерение 1 — DOI | `https://doi.org/10.1109/ICSM.2008.4658077` | 202 (IEEE, абстракт открыт) |
| Измерение 1 — открытый PDF с числом 60% | `https://fb-swt.gi.de/fileadmin/FB/SWT/Softwaretechnik-Trends/Verzeichnis/Band_29_Heft_2/06-knodel.pdf` | 200 |
| Измерение 2 — постоянная ссылка с абстрактом | `https://urn.kb.se/resolve?urn=urn:nbn:se:lnu:diva-60472` | 200 |

**Не ставить инлайном:** `https://www.oreilly.com/library/view/building-evolutionary-architectures/9781491986356/`
— отдаёт **403**; `https://doi.org/10.1145/2993412.3003391` — **403** (для ECSA-W 2016 использовать
URN-ссылку из таблицы выше); `https://ebrary.net/...` — это зеркало текста книги, годится для
верификации цитат, но не для публикации.

---

VERDICT (раунд 2): **4 claims must be fixed** — F9 (неверное утверждение об отсутствии измерений,
меняет смысл), F3, F8, F4 (сужения и несорсабельная формулировка). Ни одной выдуманной цитаты,
ни одной битой ссылки в самом абзаце — но и ни одной ссылки там сейчас вообще нет: абзац был
единственным местом статьи, где несущие утверждения стояли без источников. После правки —
шесть резолвимых ссылок и два числа со знаменателями.

---

# Раунд 3: долги

Два долга, оставшихся с раунда 2 и зафиксированных в
`tasks/20260923_sdlc-ai-pitfalls/materials/seeding-recipes.md` → GAPS. Оба закрыты **по
первоисточнику**: PDF скачаны и прочитаны в этом прогоне, числа сверены посимвольно. Где текстовый
слой PDF ронял цифры (Porter — LaTeX 1994 года без ToUnicode для цифр), страницы отрендерены в
изображение и прочитаны глазами; это отмечено в колонке «свидетельство».

## Долг 1 — Porter, Votta, Basili (инспекции требований)

**Что удалось открыть.** Первоисточник за пейволлом IEEE — да, но авторская версия открыта:
DRUM (UMD) → bitstream `CS-TR-3327.1.pdf`, item
[drum.lib.umd.edu/items/96204769-…](https://drum.lib.umd.edu/items/96204769-6905-4196-b903-709ad81148ee),
report numbers **CS-TR-3327.1 / UMIACS-TR-94-93**. Название и авторский состав совпадают с TSE
21(6):563–575, 1995 дословно: «Comparing Detection Methods For Software Requirements Inspections:
A Replicated Experiment», Adam A. Porter, Lawrence G. Votta, Jr., Victor R. Basili. 16 страниц,
прочитаны все нужные (1, 3, 5, 9, 12).
**Это техотчёт UMD, а не вёрстка IEEE** — см. флаг ниже.

| # | Утверждение как в тексте (`ru.md`) | Источник (резолвленный) | Дословная цитата / свидетельство | Вердикт | Правка |
|---|---|---|---|---|---|
| R3-1 | «48 участников» (стр. 342, 727) | CS-TR-3327.1, с. 1, Abstract | «Forty eight graduate students in computer science participated in the experiment.» | **Verified this run** | — (можно уточнить: аспиранты-первокурсники/второкурсники CS, не практики) |
| R3-2 | «16 команд по трое» (стр. 342) | там же, с. 1, Abstract | «They were assembled into sixteen, three-person teams.» | **Verified this run** | — |
| R3-3 | «два документа с 42 и 26 дефектами» (стр. 342) | там же, с. 5, §B.1 | «The authors discovered **42** faults in the WLMS SRS; and **26** in the CRUISE SRS.» (цифры прочитаны с отрендеренной страницы — текстовый слой их роняет) | **Verified this run** | — |
| R3-4 | «Команды находят 24–57% известных дефектов» (стр. 343, 727) | там же, с. 9, **Table III** «Team Fault Detection Rate Data» | Шесть ячеек средних: WLMS — Ad Hoc **.43**, Checklist **.41**, Scenario **.57**; Cruise — Ad Hoc **.31**, Checklist **.24**, Scenario **.45**. Min = .24, max = .57 | **Inferred from sources** | Числа верные, но фразы «24–57%» в работе нет: это min/max **средних по шести ячейкам** метод × документ. Разброс по **отдельным** командам шире: **.19 … .74**. Формулировку — уточнить (ниже) |
| R3-5 | «собрание команды даёт нулевой чистый прирост» / «не добавляет к этому ничего» (стр. 343, 727) | там же, с. 1 Abstract; с. 11 §E; с. 12 §E.3 и Conclusions п. 4 | Abstract: «(4) Collection meetings produced no net improvement in the fault detection rate – meeting gains were offset by meeting losses.» §E: «Our results indicate that collection meetings produce no net improvement.» Conclusions п. 4: «On the average, collection meetings contributed nothing to fault detection effectiveness.» | **Verified this run** | — (точечная оценка даже слегка отрицательна, см. R3-6 — наша формулировка консервативна, это ок) |
| R3-6 | (в тексте нет, но подпирает R3-5) величина прироста | там же, с. 12, §E.3 + Fig. 7 | «The average net meeting improvement is **−.9 ± 2.2** for WLMS inspections and **−1.2 ± 1.7** for CRUISE inspections.» Fig. 7: «The average meeting gain rate is **4.7 ± 1.3%** for the WLMS. (**3.1 ± 1.1%** for the CRUISE.)» | **Verified this run** | Опционально усилить абзац одним числом |
| R3-7 | Цитата «No faults were intentionally seeded… All faults are naturally occurring» (стр. 692) | там же, **с. 3, сноска 3** | Дословно: «The team and individual fault detection rates are the number of faults detected by a team or individual divided by the total number of faults known to be in the specification. The closer that value is to 1, the more effective the detection method. **No faults were intentionally seeded into the specifications. All faults are naturally occurring.**» | **Verified this run** | Цитата точна, многоточие элидирует «into the specifications». Оставить как есть |
| R3-8 | «24–57% — доля от дефектов, которые в документах **уже знали**» (стр. 349) | там же, с. 3 сноска 3 | «divided by the total number of faults **known to be in the specification**» | **Verified this run** | Знаменатель назван источником дословно. Это самое сильное место абзаца — не трогать |
| R3-9 | (второе место про засев) | там же, с. 5, §B.1 | «All faults present in these SRS appear in the original documents or were generated during the adaptation process; no faults were intentionally seeded into the document.» | **Verified this run** | Второе независимое подтверждение отказа от засева |

**Вердикт по долгу 1: CLEAR — 8 из 9 Verified this run, одно (R3-4) Inferred и требует правки
формулировки, не снятия.** `[UNVERIFIED]` из GAPS снимается полностью: таксономия дефектов тоже
открыта (omission/commission по 4 категории, с. 5, Appendix A), число засеянных дефектов = 0 и это
сказано дважды.

### Готовая правка для R3-4

Сейчас (стр. 342–343):

> 48 участников, 16 команд по трое, два документа с 42 и 26 дефектами. Команды находят
> 24–57% известных дефектов, а собрание команды даёт **нулевой чистый прирост** против
> того же чтения поодиночке

Предлагается:

> 48 участников, 16 команд по трое, два документа с 42 и 26 дефектами. В среднем команда находит
> от 24 до 57% известных дефектов — в зависимости от метода чтения и документа; отдельные команды
> укладываются в 19–74%. А собрание команды даёт **нулевой чистый прирост** против того же чтения
> поодиночке

И то же в «Что почитать» (стр. 727):

> 48 участников, 16 команд: в среднем находят от 24 до 57% известных дефектов, а общее собрание
> команды не добавляет к этому ничего.

Опционально — одно число в абзац на стр. 343–345, чтобы «нулевой» не выглядел округлением:

> собрание команды даёт **нулевой чистый прирост**: −0,9 ± 2,2 процентного пункта на одном
> документе и −1,2 ± 1,7 на другом — находки на встрече ровно съедаются потерями.

### Флаг по ссылке

Текст подписывает ссылку «Porter, Votta и Basili, **TSE 1995**», а ведёт она на **техотчёт UMD**
(CS-TR-3327.1 / UMIACS-TR-94-93). Содержательно это та же работа, но формально — препринт, и
числа проверены **по нему**, не по вёрстке IEEE. Честная подпись: оставить «TSE 1995» в названии
работы, а к ссылке добавить «(авторская версия, техотчёт UMD CS-TR-3327.1)» — либо в тексте, либо
в «Что почитать». Это не блокер, но подпись ссылки сейчас обещает больше, чем отдаёт.

---

## Долг 2 — arXiv:2602.11988 (файлы инструкций агенту)

**Важно: это утверждение стоит не в `ru.md` этой статьи, а в соседней —
`pieces/20260923_agent-config-ladder/ru.md`, стр. 31.** В `20260924_ai-delivery-gap/ru.md`
ни ID 2602.11988, ни Gloaguen, ни «+20% стоимости» не встречаются (grep по всему файлу — пусто);
там цитируются другие работы о файлах инструкций (arXiv:2605.10039, 2608.23550, 2511.12884,
2512.18925). Проверка сделана, вердикт ниже, но **править нужно другой файл** — передаю оркестратору.

**Что удалось открыть.** [arXiv:2602.11988](https://arxiv.org/abs/2602.11988) + полный PDF
(`arXiv:2602.11988v2 [cs.SE] 23 Jun 2026`, 24 страницы, помечен «Preprint»). Название:
**«Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?»**. Авторы:
Thibaud Gloaguen, Niels Mündler, Mark Müller (LogicStar.ai), Veselin Raychev (LogicStar.ai),
Martin Vechev — ETH Zurich. Прочитаны: abstract, §1, §4.1 (setup), §4.2 (main results), §4.3.

| # | Утверждение как в тексте (`agent-config-ladder/ru.md`, стр. 31) | Источник | Дословная цитата | Вердикт | Правка |
|---|---|---|---|---|---|
| R3-10 | Авторы и ID: «Gloaguen et al., arXiv:2602.11988» | PDF, с. 1 | «Thibaud Gloaguen … Niels Mündler … Mark Müller … Veselin Raychev … Martin Vechev»; `arXiv:2602.11988v2 [cs.SE] 23 Jun 2026` | **Verified this run** | — |
| R3-11 | «RCT — рандомизированное контролируемое испытание… две случайные группы» | PDF, §4.1 Settings | Рандомизации участников нет: это **within-instance сравнение трёх условий** (NONE / LLM / DEV) на одних и тех же задачах, значимость — Cochran–Mantel–Haenszel и стратифицированные пермутационные тесты (Tables 3, 6) | **Wrong** | «RCT» и «две случайные группы» — не то, что сделали авторы. Убрать медицинскую рамку (см. правку) |
| R3-12 | «дали одной группе агентов автосгенерированный обзор репозитория **в системном промпте**» | PDF, §4.1 Coding Agents | «For all agents, the context file is fed into their context, either by **writing it to AGENTS.md** for CODEX and QWEN CODE, or to **CLAUDE.md** for CLAUDE CODE.» | **Wrong** | Файл кладут **в репозиторий** под штатным именем, не вставляют в системный промпт. И это **файл инструкций целиком**, а не «обзор репозитория» — обзор лишь одна его секция |
| R3-13 | «другой не дали ничего» | PDF, §4.1 Settings | «NONE No context file is available, i.e., we remove developer-provided files for CTXBENCH.» | **Verified this run** | — |
| R3-14 | «Заметной разницы в успехе это не дало» | PDF, Abstract + §4.2 | Abstract: «providing context files **does not generally improve task success rates**». §4.2: «the average resolution rate is reduced by **0.5%** and **2%** on average on SWE-BENCH and CTXBENCH, respectively. With p-values of **87%** and **37%** … this indicates that they have **no significant effect on performance**.» | **Verified this run** | — (можно усилить точными числами) |
| R3-15 | «стоимость выросла больше чем на 20%» | PDF, Abstract + §4.2 + Table 2 | Abstract: «while **increasing inference cost by over 20% on average**». §4.2: «they increase the # steps in every setting, on average by 2.45 and 3.92, respectively, leading to a significant (p-value < 0.001%) cost increase of **20% and 23%** on average, respectively» | **Verified this run** | Верно — но только про **LLM-сгенерированные** файлы. У **developer-provided** рост «at most 19%» |
| R3-16 | Что такое «стоимость» | PDF, §4.1 Metrics | «we report the **total cost of LLM inference** required to complete a task. For QWEN3-30B-CODER, we estimate the cost from the average OpenRouter API price.» Table 2 — «execution cost (in USD, lower is better) per … instance» | **Verified this run** | Это деньги за инференс на задачу (USD), а не время и не стоимость разработки. Назвать явно |
| R3-17 | Выборка (в тексте не названа) | PDF, §4.1 Datasets; §3 | «the LITE split of SWE-BENCH, which consists of **300 tasks** … across **11 popular Python repositories**, none containing developer-provided context files, and our novel **CTXBENCH, consisting of 138 instances from 12 repositories**, all containing developer-provided context files». Агентов четыре: CLAUDE CODE/Sonnet-4.5, CODEX/GPT-5.2, CODEX/GPT-5.1 Mini, QWEN CODE/Qwen3-30B-Coder | **Verified this run** | **Знаменатель отсутствует в тексте** — добавить: 300 + 138 задач, 4 агента |
| R3-18 | «обзор репозитория не помогает» (следствие, которым мы пользуемся) | PDF, Abstract + §4.3 | Abstract: «while instructions in the context files are **well followed** by coding agents, **repository overviews**, although popular and recommended by model providers, **are not helpful**». §4.3: «We conclude that context files are not effective at providing a repository overview.» Метрика — среднее число шагов до первого обращения к файлу, который правил оригинальный PR | **Verified this run** | Это как раз наш тезис — но он про **секцию обзора**, а не про файл целиком |
| R3-19 | Трасса GAPS: «+7% у developer-written» | PDF, §1 | «developer-committed files **outperform LLM-generated ones** by a significant margin of 7% on average» — это DEV **против LLM**, не против «без файла». DEV против NONE: «improve agent performance by **2.4%** on average (**p = 21%**)» | **Wrong** (в трассе, не в статье) | В текст 7% не попало — хорошо. Если понадобится, брать с правильной базой |

**Вердикт по долгу 2: 2 claims must be fixed** — R3-11 («RCT», «две случайные группы») и R3-12
(«обзор репозитория в системном промпте»). Ядро утверждения — «успех не вырос, стоимость выросла
больше чем на 20%» — **подтверждено дословно**. Плюс один флаг знаменателя (R3-17).

### Готовая правка для `pieces/20260923_agent-config-ladder/ru.md`, стр. 31

Сейчас:

> Контролируемое исследование меряет эту надежду напрямую. RCT — рандомизированное контролируемое
> испытание, формат из медицины: две случайные группы, разница ровно в одном условии.
> [Gloaguen et al.](https://arxiv.org/abs/2602.11988) дали одной группе агентов автосгенерированный
> обзор репозитория в системном промпте, другой не дали ничего. Заметной разницы в успехе это не
> дало, зато стоимость выросла больше чем на 20%.

Предлагается (сохраняет вывод, чинит и механизм, и знаменатель):

> Контролируемое сравнение меряет эту надежду напрямую. [Gloaguen и соавторы,
> ETH Zurich](https://arxiv.org/abs/2602.11988) прогнали четырёх агентов по 438 задачам
> (300 из SWE-bench Lite, 138 из собственного CTXBench) в трёх условиях: файл инструкций
> автосгенерирован штатной командой самого агента, файл написан разработчиками репозитория, файла
> нет вовсе. Автосгенерированный файл успех не поднял — минус 0,5% и минус 2% в среднем,
> обе разницы статистически неразличимы, — зато стоимость инференса на задачу выросла на 20% и
> 23%. Агенты инструкции из файла честно выполняют; не работает именно «обзор репозитория» —
> секция, которую рекомендуют сами вендоры: до нужного файла агент с обзором добирается не быстрее.

Если нужен короткий вариант в одно-два предложения:

> [Gloaguen и соавторы, ETH Zurich](https://arxiv.org/abs/2602.11988) прогнали четырёх агентов по
> 438 задачам с автосгенерированным файлом инструкций и без него: успех не изменился (−0,5% и −2%,
> статистически неразличимо), стоимость инференса выросла на 20–23%. Инструкции агент выполняет —
> не работает именно секция «обзор репозитория».

**Чего писать нельзя:** «RCT», «две случайные группы», «в системном промпте», «+20%» без указания,
что это про **автосгенерированный** файл (у написанного разработчиками — «at most 19%», и успех
там всё же выше на 2,4%, p = 21%), и «стоимость» без слова «инференса».

---

VERDICT (раунд 3): **долг 1 — CLEAR** (одна правка формулировки, R3-4, плюс флаг подписи ссылки);
**долг 2 — 2 claims must be fixed**, и править нужно `pieces/20260923_agent-config-ladder/ru.md`,
а не эту статью. Оба `[UNVERIFIED]` из GAPS `seeding-recipes.md` сняты: первоисточники открыты и
прочитаны в этом прогоне.
