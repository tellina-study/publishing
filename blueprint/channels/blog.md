# Канал: блог tellian.io

Канонический дом материала. Всё остальное деривируется отсюда.

## Техника
- **Форма / длина:** лонгрид 800–2500 слов. Полные ссылки/references.
- **Платформа:** WordPress.com Atomic (Business plan). **Не пере-выводить** — пайплайн построен.
- **Пайплайн публикации:**
  ```bash
  cp -r templates/piece-bilingual pieces/<slug>          # en.md + ru.md (YAML frontmatter)
  python3 scripts/wp_publish.py pieces/<slug>            # → draft (безопасный дефолт)
  python3 scripts/wp_publish.py pieces/<slug> --dry-run  # печать HTML, без API
  python3 scripts/wp_publish.py pieces/<slug> --status publish  # в прод (нужен гейт юзера)
  ```
- **Двуязычность:** `wp_publish.py` сливает `en.md` + `ru.md` в **один** пост с CSS `:target`
  переключателем языка (`#en`/`#ru`). Идемпотентно по `wp_post_id` (ре-ран обновляет, не дублит).
  Категории/теги резолвятся/создаются по имени.
- **Авторизация:** Application Password (HTTP Basic) из `.env` в корне репо — **не** OAuth.
  UI паролей: tellian.io/wp-admin/profile.php.
- **Полный how-to:** `templates/piece-bilingual/README.md`, `wiki/topics/publishing-to-tellian.md`.

## Стиль
- Полный голос owner-taste: просто о сложном (айсберг), показывать-не-называть, божественная деталь,
  мягкий онбординг, доводить рассуждение до посчитанного практического вывода.
- **Сканируемость:** ключевое — в карточки-выноски (💡/📌/🛠️), важнейшие узлы — подзаголовки с
  эмодзи, сводка — ярлык **TL;DR**. Но без текстовых ярлыков-анонсов («Коротко:»).
- **Заголовки/термины — по-русски**, англо-термин в скобки как пояснение.
- **Гейт обязателен:** `--status publish` только после явного одобрения Макса.

## Опубликованное (образцы)
- **2026-06-21 — Language, Format, Placement** (промптинг):
  tellian.io/2026/06/21/language-format-placement/

---
## Лог (capture buffer)
- 2026-09-01 — заведён файл канала; пайплайн зафиксирован из CLAUDE.md.
