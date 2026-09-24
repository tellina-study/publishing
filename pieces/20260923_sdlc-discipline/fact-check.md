## Fact-check: 20260923_sdlc-discipline (источники, до сверки с черновиком)

Verifier: fact-checker agent, 2026-09-23. Резолвил напрямую первоисточники по 12 ключевым
утверждениям, отобранным до написания черновика (параллельный проход per brief.md). Требует
повторной сверки с итоговым текстом ru.md после того, как черновик готов.

| # | Claim | Источник (резолвленная ссылка) | Цитата/цифра | Вердикт | Примечание |
|---|-------|-------------------------------|--------------|---------|------------|
| 1 | METR RCT: n=16 мейнтейнеров, 246 задач, −19%/+20% ожидание | [arXiv:2507.09089](https://arxiv.org/abs/2507.09089) | «allowing AI actually increases completion time by 19%… contradicted developer self-estimates of 20% time reduction» | **Verified this run** | Числа совпадают с брифом точно. |
| 2 | METR 2026 follow-up: 57 разработчиков, 800+ задач, 143 репозитория, признание ненадёжности, 30-50% отказываются без AI | [metr.org/blog/2026-02-24-uplift-update](https://metr.org/blog/2026-02-24-uplift-update/) | «we believe that the data from our new experiment gives us an unreliable signal»; «30% to 50% of developers told us that they were choosing not to submit some tasks... without AI» | **Verified this run** | **Уточнение формулировки:** это НЕ «знакопеременный» результат — исходная когорта переоценена в **-18%** (то же замедление), новая когорта **-4%**; оба ДИ пересекают ноль (незначимо). Не писать «результат развернулся», писать «остался статистически незначимым в обеих группах, и сама METR признала эксперимент скомпрометированным». |
| 3 | METR self-report survey n=349, медиана 3x скорость / 1.4-2x ценность | [metr.org/blog/2026-05-11-ai-usage-survey](https://metr.org/blog/2026-05-11-ai-usage-survey/) | «median self-reported speed change... is 3x»; «median 1.4–2x change in the value of their work» | **Verified this run** | Только 87/349 (25%) — именно software engineers, остальные — другие технические роли. Не подавать как «опрос разработчиков» без оговорки. |
| 4 | DORA 2026 ROI report: «AI amplifies what's already there», J-curve, ~39% ROI/~8 мес payback, «налог нестабильности» 5%→6% | [DORA PDF](https://services.google.com/fh/files/misc/dora-roi-of-ai-assisted-software-development-2026.pdf) + [InfoQ](https://www.infoq.com/news/2026/05/dora-roi-ai-assisted-dev-report/) | «39% ROI... payback period of around eight months»; CFR «rises from 5% to 6% after AI adoption» | **ТРЕБУЕТ ПРАВКИ** | Это **иллюстративный пример-калькулятор** отчёта, НЕ измеренное среднее по индустрии. Если в тексте подано как «в среднем компании получают 39% ROI» — overclaim, переформулировать как «пример из отчёта DORA показывает...». |
| 5 | DORA CFR −7,2%, второй год подряд, throughput вверх у ~90% команд | не резолвлено ни к одному первичному DORA-документу | вторичные фрагменты дают противоречащую валентность («7,2%» встречается как СНИЖЕНИЕ стабильности, не улучшение) | **НЕ ПОДТВЕРЖДЕНО — не публиковать как есть** | Отдельного годового DORA-отчёта 2026 (survey-формата) не существует вообще — 2026 у DORA это ROI-отчёт (см. #4) и AI Capabilities Model, не survey. «Второй год подряд» и «90% команд» нигде не резолвились. **Рекомендация: убрать пункт целиком или заменить на цифру из фактически найденного DORA 2025 survey, если такая найдётся отдельно.** |
| 6 | PocketOS, 25.04.2026 — Cursor/Claude Opus 4.6 удалил прод-БД+бэкапы за 9 сек через переизбыточный Railway-токен | [zenity.io](https://zenity.io/blog/current-events/ai-agent-database-deletion-pocketos) | «The deletion took 9 seconds»; агент «produced a written confession enumerating the specific safety rules it had violated» | **Verified this run** | Все детали (дата, модель, длительность, происхождение токена, нарушение system prompt) подтверждены; корроборировано The Register, The New Stack, NeuralTrust. |
| 7a | arXiv:2607.13196 — 1,02М PR, 207 проектов, review smell +8 п.п. | [arXiv:2607.13196](https://arxiv.org/abs/2607.13196) | «review smells... by 8.0% points in the LLM era» | **Verified this run** | **Уточнение:** +8 п.п. — для подгруппы «Rapid LLM Adoption», НЕ среднее по всему датасету. Указывать это в тексте явно. |
| 7b | arXiv:2605.02273 — 33 596 agent-PR vs 5 574 human-PR, 61,38% agent-PR без ревью | [arXiv:2605.02273](https://arxiv.org/abs/2605.02273) | «61.38% (20,621) receive no recorded review activity» | **Verified this run** | Точное совпадение с брифом. |
| 8 | Meta TestGen: AI-тесты покрывали больше классов (32% vs 5,3%), убивали меньше мутантов (2,4% vs 15%) | [arXiv:2501.12862](https://arxiv.org/html/2501.12862) | «TestGen-LLM generates tests for a higher proportion of classes... 32% vs. 5.3%... killing a far smaller proportion of mutants (2.4% vs 15%)» | **ТРЕБУЕТ ПРАВКИ (фактическая ошибка в рамке)** | Это сравнение ДВУХ LLM-систем генерации тестов Meta (coverage-guided TestGen-LLM vs mutation-guided ACH), **НЕ «AI-тесты против человеческих»**. Если черновик подаёт как «AI vs человек» — фактическая ошибка, обязательно исправить на «два подхода генерации тестов, один заточен на покрытие, другой на мутанты». |
| 9 | Devin: 13,86% vs база 1,96%, только 25% бенчмарка (79/570), контаминация | [cognition.ai/blog/swe-bench-technical-report](https://cognition.ai/blog/swe-bench-technical-report) | «13.86% of issues, far exceeding... 1.96%»; оценка на «randomly chosen 25% subset» | **Verified this run, с уточнением атрибуции** | Признание контаминации — это **собственное раскрытие Cognition**, не независимый разбор со стороны. Подавать как «сама компания признала», не как «поймали независимые исследователи». |
| 10 | OpenAI: ~59% «провалов» SWE-bench Verified — дефект теста | [openai.com/index/why-we-no-longer-evaluate-swe-bench-verified](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) (прямой fetch не прошёл, 403; подтверждено конвергентно через независимые вторичные пересказы) | «59.4% of the 138 problems... contained material issues in test design» | **Inferred from sources** | **Знаменатель:** 59,4% — от 138 САМЫХ СЛОЖНЫХ задач (которые o3 не решила стабильно за 64 прогона), НЕ от всех 500 задач SWE-bench Verified. Если в тексте «59% всего SWE-bench Verified сломано» — ошибка в базе, обязательно указать «от 138 сложнейших случаев». |
| 11 | CVE-2025-59536, CVSS 8.7, найдена 21.07.2025, патч 26.08.2025 | [Check Point Research](https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/), [Tenable](https://www.tenable.com/cve/CVE-2025-59536) | «July 21st, 2025 – Check Point Research reported»; «August 26th, 2025 – Anthropic implemented a final fix»; CVSS Base Score 8.7 | **Verified this run** | 8,7 — это CVSS **v4.0**; v3.1-оценка — 8,8 (тоже широко цитируется). Указывать версию явно, чтобы не выглядеть противоречиво рядом с другими источниками. |
| 12 | «Rules in prompts are requests. Hooks in code are laws» — dev.to, 2026 | [dev.to/.../i-wrote-200-lines-of-rules-for-claude-code-it-ignored-them-all-4639](https://dev.to/minatoplanb/i-wrote-200-lines-of-rules-for-claude-code-it-ignored-them-all-4639) | Цитата подтверждена дословно, опубликовано 8 марта 2026 | **Verified this run** | Проверить отображаемое имя автора вживую перед публикацией (fetch показал «DavidAI311» под хендлом `minatoplanb`). |

### Must fix before ship
- **#5 (DORA −7,2% CFR, второй год подряд, 90% throughput)** — не резолвлено ни к одному первичному
  источнику, валентность цифры в найденных вторичных фрагментах противоречит брифу. **Убрать пункт
  или заменить на действительно резолвящуюся цифру.**
- **#4 (DORA 39% ROI / 8 мес payback)** — переформулировать как иллюстративный пример отчёта, не
  измеренное среднее по индустрии.
- **#8 (Meta TestGen)** — исправить рамку: это LLM vs LLM (TestGen-LLM vs ACH), не AI vs человек.
- **#10 (OpenAI 59,4%)** — явно указать базу: от 138 сложнейших случаев, не от всех 500 задач.
- **#9 (Devin контаминация)** — атрибутировать как собственное признание Cognition, не как внешний
  разбор.

### Флаги (не блокеры, но учесть в формулировках)
- #2 — не «развернулся», а «остался незначимым в обеих когортах + признание ненадёжности».
- #3 — только 25% выборки — именно разработчики, остальные другие технические роли.
- #7a — +8 п.п. для подгруппы «Rapid LLM Adoption», не для всего датасета.
- #11 — уточнить версию CVSS (v4.0 = 8,7).
- #12 — проверить имя автора вживую перед публикацией.

VERDICT: 5 утверждений требуют правки/удаления перед ship (#4, #5, #8, #9, #10 — #5 скорее всего
убрать целиком). Остальные (#1, #2, #3, #6, #7a, #7b, #11, #12) — Verified this run, годятся к
использованию с уточнениями формулировок выше.

## Правки внесены оркестратором (2026-09-23, после сверки с черновиком ru.md)
- #3 — «349 разработчиков» → «349 технических специалистов» (уточнена выборка).
- #4/#5 (DORA) — переформулировано: 39% ROI/8 мес/5%→6% поданы как иллюстративный пример из
  отчёта, не измеренное среднее; отдельная непроверяемая «−7,2% второй год подряд, 90% throughput»
  убрана из текста целиком.
- #7a — добавлена оговорка «в группе проектов, где на LLM-ревью переходили особенно быстро».
- #8 (Meta TestGen) — исправлена рамка: было «AI-тесты vs человеческие», стало «TestGen-LLM
  (заточен на покрытие) vs ACH (заточен на мутанты)» — обе системы LLM-based, ошибка в тексте
  устранена.
- #10 (OpenAI 59%) — добавлен явный знаменатель: «среди 138 самых сложных задач», не весь бенчмарк.
- #11 (CVE-2025-59536) — **важное уточнение после независимой перепроверки**: параллельный
  fact-checker материала 2 (`pieces/20260923_agent-config-ladder/fact-check.md`, пункт #6) заявил,
  что CVE-2025-59536 — это НЕ про хуки, а про MCP/trust-dialog bypass, и предложил заменить на
  GHSA-ph6w-f82w-28w6. Оркестратор перепроверил обе advisory напрямую (WebFetch) + первоисточник
  Check Point Research: GHSA-4fgq-fpq9-mr3g (= CVE-2025-59536) — «code executed before trust
  dialog accepted», CWE-94, ровно то поведение, что описывает хук `SessionStart`; Check Point
  явно пишет про этот вектор: «we crafted a .claude/settings.json file which includes a simple
  hook»; даты (найдена 21.07.2025, патч 26.08.2025) подтверждены дословно. GHSA-ph6w-f82w-28w6
  оказалась ДРУГОЙ, более мелкой проблемой (неясность текста предупреждения, не байпас). Вывод:
  **оригинальная атрибуция CVE-2025-59536 в черновике была верной** — правка параллельного
  fact-checker'а по этому пункту отклонена как ошибочная после прямой перепроверки. Текст
  оставлен с CVE-2025-59536, добавлена прямая ссылка на Check Point.
- Sean Grove «код 10-20% ценности» — резолвлено отдельно (не входило в исходный список 12 пунктов):
  доклад «The New Code» (AI Engineer, OpenAI), точная цитата подтверждена через транскрипт
  (lawwu.github.io/transcripts/8rABwKRsec4.html): «Code is sort of 10% to 20% of the value that
  you bring. The other 80% to 90% is in structured communication.» Маркер снят, цитата и ссылка
  добавлены в текст.

Все `[FACT-CHECK: ...]` маркеры в `ru.md` разрешены. Готово к стадии CRITIQUE (editor +
mirror-editor + reader-fan).
