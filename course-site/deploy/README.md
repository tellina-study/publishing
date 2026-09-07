# Деплой курса-сайта (self-host на Vultr, без Cloudflare)

Статический MkDocs-сайт живёт на том же Vultr VM, что Umami и Remark42 — одна инфра,
same-origin (проще CORS/куки для метрики и комментариев).

## Что нужно один раз
1. **DNS:** `A`/`AAAA` запись поддомена (напр. `course.tellian.io`) → IP этого VM.
2. **Caddy** на VM (авто-TLS): положи `Caddyfile` (замени `COURSE_DOMAIN`), запусти.
3. **Каталог** `/var/www/course-site` на VM, права на запись для деплой-пользователя.

## Каждый деплой (фаза A)
```bash
export COURSE_LESSONS_DIR=/path/to/lessons/library/lectures
export COURSE_SSH=deploy@<vm-ip>
export COURSE_REMOTE_DIR=/var/www/course-site
bash deploy/deploy.sh
```
Скрипт: генерит страницы из lessons → `mkdocs build --strict` → `rsync` собранного `site/` на VM.
PNG слайдов **не хранятся в git** — они пересобираются локально и уезжают в `site/` (rsync).

## Фаза B (Umami + Remark42) — когда контейнеры подняты на VM
- Раскомментируй reverse-proxy в `Caddyfile` (`/stats/*` → Umami, `/comments/*` → Remark42).
- Пропиши в шаблон темы (`docs/overrides/`) снепет Umami + кастомный scroll-глубина JS
  (25/50/75/100 %) и embed Remark42. Нужны: Umami `website-id`, Remark42 `SITE_ID` + URL.

## Что нужно от владельца, чтобы задеплоить
- SSH-доступ к VM (user@host + ключ) ИЛИ владелец сам гоняет `deploy.sh`.
- Выбранный поддомен.
- (Для фазы B) URL и ID работающих Umami/Remark42.
