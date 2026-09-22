# Lessons Learned

Numbered, durable lessons about **how we work** (not topic knowledge — that goes in `wiki/topics/`).
Read before starting; append on discovery. Each lesson: what happened, the rule it produces.

> Format: `L<NN> — <one-line rule>` then a short why + anchor (the piece/session that taught it).

---

L01 — To publish on tellian.io, run the built pipeline; don't re-derive access.
  Why: the blog is WordPress.com **Atomic** (Business), which supports **Application Passwords**
  directly on `tellian.io/wp-json` (HTTP Basic) — no OAuth. The app-password UI is hidden by the
  WordPress.com profile screen (find it at `wp-admin/profile.php`). Pipeline: `scripts/wp_publish.py`
  + `templates/piece-bilingual/`; how-to in `wiki/topics/publishing-to-tellian.md`.
  Anchor: tasks/20260621_wp-publish/

L02 — A derivative is a fork of the FACTS, not just the prose — diff every number against the final canon.
  Why: the Telegram draft still said "русский ×3" after the canon was fact-corrected to ×2, and
  carried a проговор-leak the body had already purged. Re-verify each load-bearing number/claim in
  telegram/linkedin against the *final* `ru.md`/`en.md` before shipping the derivative.
  Anchor: pieces/20260620_prompting-recommendations / notes/reflections/20260621-prompting-article-lifecycle.md

L03 — The WP publisher is a hard file contract; prove it with `--dry-run` before any real run.
  Why: it reads `pieces/<slug>/en.md` + `ru.md` with YAML frontmatter and injects `title` as `<h1>`
  (never repeat the title in the body). `--dry-run` prints the assembled HTML with no API call.
  categories/tags are resolved/created **by name** — confirm against the site's taxonomy first, a
  typo spawns a stray term. Anchor: pieces/20260620_prompting-recommendations

L04 — The KB tracks `main`, not the ship — sync the doc-layer on every merge, with status accuracy.
  Why: merging a piece to `main` to preview/publish exposed a RAG-vs-doc-layer asymmetry (RAG
  auto-reindexes via the post-merge hook; `wiki/pieces/INDEX.md` + ontology lagged until SHIP, so
  `main` and the indexes diverged). Close-the-Loop now keys INDEX (status bucket) + ontology to
  *merge*, and URL/topic/catalog to *publish*. The post-merge hook reminds when `pieces/` changed.
  Anchor: CLAUDE.md Close-the-Loop / notes/reflections/20260621-prompting-article-lifecycle.md

L05 — Every owner edit of a draft is taste signal — capture it (mirror + memory) the same turn.
  Why: the owner's own LinkedIn edit taught the calibration (provocative headline over personal
  narrative; one line per point; keep myth-busting for the article, not the teaser). His edits are
  the highest-signal taste data we get; folding them keeps the mirror honest.
  Anchor: notes/owner-taste.md / memory linkedin-style

L06 — «Последняя версия» ищется по ВЕТКАМ И ВОРКТРИ, а не по origin: ветка, которую никто не
  запушил, невидима для любой проверки через remote.
  Why: лекция 3 v6.4 (14 коммитов, дек 55→67 слайдов) месяц лежала только в локальном воркри
  умершей сессии. `git ls-remote` показывал, что свежее v6.3 ничего нет, и это было враньём.
  Anchor: AI-usage-lessons PR #200 / tasks/20260830_course-site-launch/log.md

L07 — Перед публикацией сверяй ПОКРЫТИЕ артефактов друг другом, а не их наличие: версия,
  поднятая в одном артефакте, не поднята в остальных.
  Why: v6.4 углубила дек и главу, не тронув speech.md — 55 секций против 67 слайдов, 7 из них
  про удалённые слайды. Артефакты были на месте и «свежие», а публикация по речи дала бы 48
  слайдов — регресс против уже живых 55. Ловится одной проверкой: id дека ⊆ id речи.
  Anchor: publishing PR #32 / course-site/scripts/sync_lectures.py:deck_covers_speech

L08 — Способ деплоя обязан жить в репозитории, а не в транскрипте сессии: иначе он исчезает
  вместе с сессией, и следующий исполнитель честно рапортует «доступа нет».
  Why: ключ к RU VPS лежал в scratchpad сессии e777caf5; после её смерти `deploy/README.md`
  требовал «SSH-доступ от владельца», а реальный приём (root-пароль → paramiko ставит ключ в
  authorized_keys → rsync) был записан только в чужом транскрипте. Владелец знал, что я «уже
  деплоил», — и был прав. Проверять соседей стоит ДО того, как объявлять блокер.
  Anchor: tasks/20260830_course-site-launch/log.md 2026-09-20 / course-site/deploy/README.md

L09 — «Последней версии» может не быть ни в одном коммите: проверяй `git status` по ВСЕМ
  воркри, а не только `git diff` по веткам.
  Why: кейс-версия Семинара 3 (43 слайда, полный пивот формата) лежала незакоммиченной в воркри
  умершей сессии. Сравнение веток по коммитам дало «везде идентично», и на сайт ушла старая
  версия — владелец заметил раньше меня. Дополняет [[L06]]: там ветка была непушнутой, здесь
  работа вообще не закоммичена.
  Anchor: AI-usage-lessons PR #203 / tasks/20260830_course-site-launch/log.md 2026-09-20

L10 — Перед тем как объявлять «нет SSH-доступа», проверь ключ по фиксированному абсолютному
  пути, а не только `~/.ssh`: разные сессии на этом воркспейсе резолвят `$HOME` по-разному, и
  ключ, заведённый одной из них, физически лежит вне текущего `~` и переживает её смерть — доступ
  ведь живёт на сервере (`authorized_keys`), не в сессии.
  Why: две подряд сессии («Публикация 3», «Публикация 3-2») заявили блокер «нет ключа», честно
  проверив пустой `~/.ssh`, и одна из них прождала владельца несколько часов. Ключ всё это время
  был рабочим — просто лежал по `/home/harness/.ssh_course_deploy_key`, а не в `~` конкретной
  сессии. Проверка — одна SSH-команда с `BatchMode=yes`, ничего не портит, занимает секунды.
  Углубляет [[L08]]: там был найден сам рецепт заведения ключа, здесь — что рецепт вообще не
  нужен, если ключ уже стоит на сервере где-то за пределами твоего `~`.
  Anchor: course-site/deploy/README.md (Шаг 0) / publishing sess-f6e07105f5b248049de0a93f53f38641 2026-09-22

<!--
L01 — <rule>.
  Why: <what happened>.
  Anchor: pieces/<slug> / notes/reflections/<date>-<topic>.md
-->
