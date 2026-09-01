# Итог — 20260901_transformers-vaswani

**Вердикт: SHIP.** Опубликовано в блог (лайв), деривативы готовы.

## Продукт (в репе)
- `pieces/20260901_transformers-vaswani/ru.md` — RU-канон
- `pieces/20260901_transformers-vaswani/en.md` — EN-дериватив (billingua, один пост с `#en`/`#ru`)
- `pieces/20260901_transformers-vaswani/telegram.md` — TG (запощен владельцем)
- `pieces/20260901_transformers-vaswani/linkedin.md` — LinkedIn (готов к постингу)
- Кухня стадий: `outline.md`, `roast.md`, `fact-check.md`

## Опубликованные ссылки
- **Блог (RU+EN):** https://tellian.io/2026/09/01/ai-day-transformers/ (WP post 309)
- **Telegram:** запощен владельцем
- **LinkedIn:** текст готов (`linkedin.md`), постинг за владельцем

## Что получилось
Угол: **приключение одной идеи** — attention изобрели в 2014 (Bahdanau) для перевода; 2017 (Vaswani)
убрал рекуррентность → параллелизм → scaling → ChatGPT. Рамка «День ИИ / 12 лет». Изначальный угол
(«недооценённая статья») развернули в позитив после ревью владельца.

## Качество
- Research ×5 (до/статья · наследие · Bahdanau-2014 · фронтир-2026).
- fact-check: **CLEAR** — дата 2014-09-01, обе ключевые цитаты, arXiv-id, механизм параллелизма — verified.
- Линзы: editor + mirror-editor + reader-fan (все REVISE→устранено), stylist-ru ×2 + stylist-en.
- 22 инлайн-правки владельца + предпубликационная вычистка калек/склонённых годов.

## Инфраструктура (побочно)
- Хук-защита: `wp_publish.py --status publish` требует явного аппрува (`.claude/hooks/guard-live-publish.sh`).
- `.env` с WP-доступом сохранён в корне (gitignored).

## Ссылки процесса
- GitHub issue: [#26](https://github.com/tellina-study/publishing/issues/26)
- Ветка: `piece-transformers-vaswani`
