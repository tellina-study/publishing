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

## Доступ к RU VPS (88.218.62.36) — если ключа в сессии нет

**Ключ не хранится в репозитории и не переживает сессию.** Каждая новая сессия начинает с пустым
`~/.ssh`, и это НЕ означает «доступа нет». Заводится он так (проверено 2026-08-30 и 2026-09-20):

1. Сгенерировать свой ed25519: `ssh-keygen -t ed25519 -N '' -f ~/.ssh_course_deploy_key`.
2. Поставить публичную часть в `authorized_keys` root@88.218.62.36 **по root-паролю** (пароль у
   владельца; в сессию он передаётся разово и в логи не пишется):
   ```python
   import os, paramiko                      # pip install --user paramiko
   c = paramiko.SSHClient(); c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   c.connect("88.218.62.36", username="root", password=os.environ["RU_PW"],
             look_for_keys=False, allow_agent=False, timeout=25)
   pub = open(os.path.expanduser("~/.ssh_course_deploy_key.pub")).read().strip()
   c.exec_command("mkdir -p ~/.ssh && chmod 700 ~/.ssh && touch ~/.ssh/authorized_keys && "
                  "chmod 600 ~/.ssh/authorized_keys && "
                  f"grep -qF '{pub}' ~/.ssh/authorized_keys || echo '{pub}' >> ~/.ssh/authorized_keys")
   ```
3. Дальше всё по ключу: `COURSE_SSH=root@88.218.62.36 bash deploy/deploy.sh`, либо вручную
   `rsync -az --delete --checksum -e "ssh -i ~/.ssh_course_deploy_key -o StrictHostKeyChecking=no" \
   site/ root@88.218.62.36:/var/www/course-site/`.

Отдаёт сайт Caddy с этого же VPS (`systemctl is-active caddy`), корень — `/var/www/course-site`.

## Что нужно от владельца, чтобы задеплоить
- Root-пароль VPS (разово, для шага 2 выше) — либо владелец сам гоняет `deploy.sh`.
- Выбранный поддомен.
- (Для фазы B) URL и ID работающих Umami/Remark42.
