#!/usr/bin/env bash
# deploy.sh — собрать курс-сайт и залить на Vultr VM (self-host, без Cloudflare).
#
# Требует переменные окружения (или заполни ниже):
#   COURSE_LESSONS_DIR  путь к library/lectures в клоне репо lessons
#   COURSE_SSH          user@host VM (напр. deploy@203.0.113.10)
#   COURSE_REMOTE_DIR   каталог на VM (напр. /var/www/course-site)
#
# Идемпотентно: пересобирает страницы из lessons, строит mkdocs, rsync только изменённое.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"   # course-site/
cd "$HERE"

: "${COURSE_LESSONS_DIR:?укажи путь к lessons/library/lectures}"
: "${COURSE_SSH:?укажи user@host VM}"
: "${COURSE_REMOTE_DIR:=/var/www/course-site}"

echo "==> 1/3 генерация страниц из lessons ($COURSE_LESSONS_DIR)"
python3 scripts/sync_lectures.py --lessons "$COURSE_LESSONS_DIR"

echo "==> 2/3 сборка сайта (mkdocs build --strict)"
python3 -m mkdocs build --strict

echo "==> 3/3 rsync → $COURSE_SSH:$COURSE_REMOTE_DIR"
rsync -avz --delete --checksum site/ "$COURSE_SSH:$COURSE_REMOTE_DIR/"

echo "Готово. Проверь https://<домен>/ (Caddy отдаёт $COURSE_REMOTE_DIR)."
