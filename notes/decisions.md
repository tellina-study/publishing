# Decisions

Running log of strategic decisions — channel choices, conventions, directions. Append-only;
newest at top. One line each, dated. Strategy and "why", not mechanics (mechanics → conventions).

---

## 2026-06-21 — Close-the-Loop tracks `main`, not the ship
The KB must mirror `main` (the source of truth), not wait for a SHIP verdict. Heavy doc-layer sync
is rekeyed: **merge to `main`** → `wiki/pieces/INDEX.md` (status bucket) + ontology + RAG (auto);
**publish (live URL)** → row to Published + URL, topic note, `/catalog-piece`. Drove a CLAUDE.md
rule change (PR #12) + a post-merge hook reminder. Why: merging a piece to preview/publish left the
indexes lagging `main` — a real inconsistency the owner flagged.

## 2026-06-21 — Bilingual blog longread stays one full reference; short version ships as derivatives
For the prompting piece (RU v13 + EN), editor + reader-fan flagged "two articles in one coat" —
a casual reader and a builder served by the same text. Owner's call: **do NOT split the blog
piece.** The canonical blog longread stays the FULL reference even when it serves two audiences;
the short, casual version is delivered as the **Telegram/LinkedIn derivatives**, not as a separate
blog article. We cut only genuine duplication (per-model contrast consolidated into one section;
TOON trimmed 3→2 bullets) — builder depth is kept intact. General rule for bilingual blog pieces:
one canonical reference per language, casual entry points live in the short channels.

## 2026-06-20 — Co-author harness adopted
Borrowed methodology from `starshineworld/world`: I work as a **full co-author with opinions**
(owner has the final word); maintain the **owner's mirror** (`notes/owner-taste.md` + mirror's
learning loop) reviewed by a new `mirror-editor` agent; added a `reader-fan` (cold-reader) lens.
New process rules: **clarity-first** (study KB → sequential clarifying questions before starting),
**ШАГ 0** (task-specific plan before work), **`tasks/` workspace** (kitchen: brief/plan/log/result
+ materials, separate from `pieces/` deliverables), **one branch + worktree per task**, union-merge
for append-only files, tooling-hygiene + living-body-artifact rules. My identity lives in
`notes/coauthor-vision.md` + `coauthor-journal.md`. Every non-trivial task is also mirrored by a
**GitHub issue** (Goal / checklist / progress / status), kept current in the same turn — the issue
is the shareable ledger, `tasks/` is the kitchen.

## 2026-06-20 — Repo created
Set up the `publishing` harness (tellina-study/publishing, public). Lifecycle BRIEF → DRAFT →
FACT-CHECK → CRITIQUE → SHIP; knowledge base = wiki + lightweight ontology + local RAG; agents =
researcher / fact-checker / editor / librarian. Patterns adapted from the tradebotint/research lab
harness and the AI-usage-lessons knowledge repo.

## 2026-09-20 — Семинары публикуются: у курса-сайта появился раздел «Семинары»
Владелец отменил решение 2026-08-30 «Семинары: СКРЫТЬ пока» — на lessons.tellian.io сделан
отдельный раздел, опубликованы семинары 1-3. Из паблика убрана только универ-админка
(чат курса в MAX, рубежный контроль) плюс три слайда, где «МГТУ им. Н.Э. Баумана» и метки
РК1-3 вшиты в КАРТИНКУ и текстовым фильтром не снимаются — перерендер вернёт их обратно.
Кросс-ссылки лекций на семинары больше не считаются «висячими».
Anchor: publishing#31 / PR publishing#32 / AI-usage-lessons PR #202

## 2026-09-20 — Источник комментариев на сайте: не только speech.md
Раньше `speech.md` была единственным индексом истины для страниц курса. Теперь генератор
берёт комментарии из `## Speaker notes` в `slides/*.md`, когда речь ОТСТАЛА от дека
(проверяется покрытием id) или её нет вовсе (семинары). Речь остаётся источником по
умолчанию: пока она покрывает дек, ничего не меняется. Повод — lec-03 v6.4: дек углубили
55→67 слайдов, речь не тронули, и публикация по речи дала бы 48 слайдов вместо 67.
Anchor: publishing PR #32 / course-site/scripts/sync_lectures.py

