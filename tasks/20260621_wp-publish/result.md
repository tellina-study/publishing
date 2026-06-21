# Итог — wp-publish (публикатор на tellian.io)

## Вердикт
**SHIP (infra).** Двуязычный EN/RU markdown → один пост на WordPress.com со свитчером
языков (CSS `:target`) через REST API. Конвейер проверен end-to-end.

## Что сделано
- `scripts/wp_publish.py` — читает `pieces/<slug>/{en.md,ru.md}`, конвертит в HTML,
  заворачивает в шаблон свитчера, создаёт/обновляет один пост (идемпотентно через
  `wp_post_id`), разрешает/создаёт категории и теги по имени. Дефолт статус = `draft`.
- `templates/piece-bilingual/` — скелеты `en.md` + `ru.md` + `README.md`.
- `.env` (gitignored) — `WP_API_BASE` / `WP_USER` / `WP_APP_PASSWORD`.

## Ключевые находки (verified this run)
- Сайт — **WordPress.com Atomic** (Business), ID 244070662. Поддерживает
  **Application Passwords** прямо на `tellian.io/wp-json` — OAuth не нужен.
- Авторизация: HTTP Basic (email + app password). Права `publish_posts`,
  `edit_posts`, `manage_categories` = true.
- Свитчер — **чистый CSS `:target`** (не JS). Правила show/hide лежат один раз в
  Additional CSS сайта; пост несёт только строку-свитчер + `#en`/`#ru` `lang-block` div.
- Теги/категории — нативная таксономия WP (term ID), резолв по имени, создаются если нет.

## Проверено вживую
Создан черновик 255 → сверены контент/термы на сервере → повторный запуск обновил
(без дубля) → черновик 255 и тестовый тег удалены. Мусора на сайте не осталось.

## Артефакты
- В репе: `scripts/wp_publish.py`, `templates/piece-bilingual/`
- Опубликовано: не публиковалось (только тестовый черновик, удалён)

## Решения
- Без worktree (нет параллельных задач; `.env` живёт в корне основного чекаута).
- Дефолт `--status draft`; выход в публикацию требует явного `--status publish` (ship-gate).

## Что забрать на будущее (урок)
- WordPress.com Business = Atomic → Application Passwords работают напрямую, искать их
  надо на `tellian.io/wp-admin/profile.php` (UI wordpress.com их прячет), а не в OAuth.
