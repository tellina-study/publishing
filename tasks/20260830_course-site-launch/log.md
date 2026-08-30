# Лог — course-site-launch

## 2026-08-30 — старт, разведка, blueprint
- Прочитал CLAUDE.md/README/owner-taste publishing-репо, сориентировался в конвенциях.
- Разведал исходный контент lessons (`/home/harness/harness-projects/256/lessons-3bb49d40/library/lectures/`):
  - 16 лекций (lec-01…lec-17, нет lec-16), контент только RU.
  - **`*-notes.pdf` не существует** → комментарии только из `speech.md`. «Открытый вопрос» снят реальностью.
  - `speech.md` чисто маппится на слайды: `## [sNN · X мин] — Title`, число совпадает со `slides_covered`.
  - `deck.yaml` — порядок слайдов + метаданные; join-ключ PDF-страница ↔ slide-id ↔ комментарий.
  - Slide-ID не последовательны (s01,s00a,s02a…) → маппинг только через порядок в deck.yaml.
  - **poppler (`pdftoppm`) не установлен** — риск для локали и билда.
  - `speech.md` status: draft — публикуем черновой контент, нужен гейт.
- Завёл ветку+worktree `kb-course-site-launch`, развернул tasks/20260830_course-site-launch.
- Написал brief.md, architecture.md (blueprint с развязкой фаз A/B/C), plan.md.
- Ключевые решения (реальностью, не вкусом): комментарии = speech.md; контент = COPY производных
  (PNG+md) в publishing-репо (CF Pages видит только его); развязка фаз (A не зависит от Vultr).
- Дальше: 4 issue → роаст плана → PR → гейт владельца.

## 2026-08-30 — issue + уточнения владельца
- Заведены issue: **#19 epic**, #20 дизайн, #21 генератор, #22 публикатор (все label `infra`).
- Уточнения владельца учтены до роаста: (1) референсы вынесены в `materials/references.md` + §8 blueprint;
  (2) **EN-перевод комментариев — наша работа** (субагенты при публикации), не внешняя задача;
  (3) навигация ДВА уровня — по лекциям и **внутри по слайдам** (якоря + TOC-сайдбар). Комменты в #20/#21.
- Дальше: коммит ветки + PR (линк #19), независимый роаст плана, гейт.

## 2026-08-30 — роаст (HOLD) + исправления + разворот по переводу
- Независимый роаст плана → **HOLD**: ложная предпосылка «speech чисто маппится, индекс=deck».
- Перепроверил сам на всех 16 лекциях: **speech-секций == страниц PDF везде**; deck.yaml ненадёжен
  (03/04/05 неполны, 09 без slides). **Индекс = speech.md.** Разметка в **4 диалектах** (H2 `## [s`,
  H3 `### [s`, `### [Слайд N]`, `## sNN`) — наивный парсер ломал 7/16 молча. Инструкторские секции
  вкраплены между слайдами → whitelist. Добавлен PII/лицензия-скраб (High). Milestone → по представителю
  каждого диалекта (lec-01+08+10+13). Umami scroll = кастом-JS, не «за час».
- Всё внесено: roast.md, architecture.md (§3 переписан, §5, риски R6-R10), plan.md milestone, issue #19/#21/#22.
- **Разворот по переводу (владелец):** перевод комментариев И слайдов — НЕ наш scope, а upstream в
  `lessons` (владелец ставит задачу). publishing = language-aware рендер готовых языков. MVP RU-only.
  Убрал EN-перевод из нашего scope (было ошибочно вписано ранее).
- Дальше: гейт владельца (открытые вопросы: домен/DNS, Vultr, CF, PII).

## 2026-08-30 — proof-of-format собран и проверен (post-gate milestone)
- Владелец дал ход пруву на гейте («да, строй прув»).
- Стек: mkdocs 1.6.1 + material + static-i18n + rss + PyMuPDF (в user-site, --break-system-packages;
  venv недоступен — нет ensurepip). **PyMuPDF вместо poppler** → риск R1 закрыт (нет системной зависимости).
- `course-site/`: mkdocs.yml (i18n suffix, attr_list, toc), requirements.txt, scripts/sync_lectures.py, лендинг.
- **Генератор отработал на всех 4 диалектах** (lec-01 H2 `## [s`, lec-08 H3 `### [s`, lec-10 `### [Слайд N]`,
  lec-13 `## sNN`): 36/39/43/41 слайдов, guard «секций==страниц» прошёл. **0 утечек** инструкторских секций.
- `mkdocs build --strict` — ок; построились ru + en (EN = fallback на RU, НЕ 404 → R8 закрыт).
  Якоря слайдов `id="s-01"` + TOC-пермалинки → внутрилекционная слайд-навигация работает. Переключатель RU/EN,
  sitemap.xml — на месте.
- **Git-бლоат измерен:** 48 МБ / 4 лекции (~12 МБ/лекц) → ~190 МБ на 16 (R4 подтверждён замером, не догадка).
  Генерируемый вывод (PNG+md) убран в .gitignore — решение git-vs-LFS на гейт. Коммитим только код+конфиг.
- Дальше: артефакт-образец владельцу «пощупать»; затем гейт по формату + вопросы деплоя (домен/CF/Vultr/git-LFS).

## 2026-08-30 — масштаб на 16 + «без Cloudflare»
- Гейт #2 (формат): владелец одобрил на реальном контенте («да, масштабируй на 16»); PNG — «обычный git»;
  доступы — Vultr VM поднят + DNS tellian.io. Артефакт-образец показан (lec-08, 7 слайдов).
- **Владелец: «без Cloudflare»** — override зафиксированного стека. CF Pages убран. Хостинг переигран:
  self-host на Vultr (rsync + Caddy, same-origin с Umami/Remark42, PNG не нужны в git) ИЛИ GitHub Pages.
  → вопрос хостинга владельцу.
- Генератор масштабирован: ALL_LECTURES default, авто-лендинг из манифеста, терпимый frontmatter
  (title|lecture_title), устойчивый GuardMismatch (пропуск+отчёт, не слепой маппинг).
- **15/16 собрано чисто** (mkdocs --strict, 604 PNG, 146 МБ). **lec-04 пропущена**: 36 speech-секций vs
  41 страница PDF (Δ=5 build-шагов) — дефект исходника lessons, нужен переэкспорт/ручная сверка.
- Связка «PNG в git»↔хостинг: при self-host PNG в git не нужны (rsync) → решение отложено к хостингу,
  вывод в .gitignore. Закоммичен только код (генератор/конфиг/nav).
- Дальше: выбор хостинга владельцем → фаза A деплой; lec-04 к владельцу (фикс в lessons).

## 2026-08-30 — хостинг: self-host Vultr (выбор владельца)
- Владелец выбрал **self-host на Vultr**. Следствия: PNG в git НЕ нужны (rsync собранного site/),
  same-origin с Umami/Remark42. Вопрос «PNG в git» закрыт (moot при self-host) — вывод в .gitignore.
- Подготовлен деплой-скаффолдинг (фаза A, без доступа к VM): course-site/deploy/{Caddyfile,deploy.sh,README.md}.
  Caddy авто-TLS + file_server + кэш ассетов; deploy.sh: sync_lectures → mkdocs build → rsync.
  Reverse-proxy /stats,/comments под фазу B — закомментирован (ждёт URL/ID Umami/Remark42).
- Нужно от владельца для реального деплоя: SSH к VM (или сам гоняет deploy.sh), поддомен, и для фазы B —
  URL+ID работающих Umami/Remark42. lec-04 — переэкспорт PDF в lessons.

## 2026-08-30 — ФАЗА A ЗАДЕПЛОЕНА (live на Vultr)
- VM: Ubuntu 26.04, 1 vCPU, 1.6 ГБ RAM, 40 ГБ free, host `lessons`, IP 136.244.103.245.
- Доступ: залил свой ed25519-ключ (scratchpad), дальше по ключу; пароль root не печатал. **Рекомендация владельцу:
  сменить розданный в чате пароль + оставить только key-auth.**
- Caddy v2.11.4 (apt), webroot /var/www/course-site, Caddyfile :80 (IP, без TLS пока нет домена).
- Деплой: mkdocs build → rsync site/ (155 МБ, 15 лекций). **ufw был policy DROP** → открыл 22/80/443.
- **Live http://136.244.103.245/**: landing/lecture/slide-png/EN-fallback/sitemap — все HTTP 200.
- ⚠️ Перф: слайд-PNG ~данные ниже — тяжёлые страницы. Флаг на оптимизацию (WebP/ниже DPI/lazy-load) до широкого шаринга.
- Дальше: домен (поддомен tellian.io → A-запись на IP) → Caddy auto-TLS (HTTPS); затем перф-оптимизация; фаза B.

## 2026-08-30 — домен+HTTPS, оптимизация, фаза B (всё live)
- **Домен lessons.tellian.io** (владелец дал; A-запись уже указывала на IP). Caddy → auto-TLS Let's Encrypt,
  HTTP→HTTPS 308. **https://lessons.tellian.io/** живой.
- **Оптимизация:** слайды PNG→**WebP** (q80, DPI 120) + **lazy-load** (raw `<img loading=lazy>`).
  Страница лекции **~2.8 МБ вместо 12.8 МБ (−78%)**, ~75 КБ/слайд.
- **Баг заголовков (lec-3 «Lec 03»):** мой генератор писал YAML `title:` без кавычек — двоеточие в
  заголовке ломало frontmatter. Фикс: `yaml_q()` + нормализация заголовков (снятие «речь лектора»,
  единый «Лекция N. …»). Правок в исходниках не нужно.
- **Переключатель языков:** был мёртвый EN (fallback показывал русский) → EN `build:false` до появления
  перевода upstream. Свитчер убран (не вводит в заблуждение). Вернётся при появлении `*.en.md`.
- **Фаза B (Umami + Remark42) на том же VM, same-origin через Caddy:**
  - Docker + compose (deploy/phase-b/): Umami+Postgres+Remark42, слушают 127.0.0.1, проксируются
    Caddy `/stats` и `/comments`. Swap 5.4 ГБ уже был; RAM used ~560/1637 МБ.
  - Umami website-id `35d3e86c-…`; трекер + **scroll-глубина (25/50/75/100%)** и Remark42-embed вшиты
    в `overrides/main.html` (комментарии — только на страницах лекций).
  - **Сменил дефолтный admin/umami** (pgcrypto bcrypt): новый пароль в `/opt/course-phase-b/CREDENTIALS.txt`
    (root-600 на VM). Проверено: new login 200, old 401. Дашборд https://lessons.tellian.io/stats/ = 200.
  - End-to-end: pageview event 200, embed.js 200.
- Осталось: сменить root-пароль VM (владелец); дизайн/брендинг (#20); lec-04 фикс в lessons; соц-логины
  Remark42 (опц.); RSS.
