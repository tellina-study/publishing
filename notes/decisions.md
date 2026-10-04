# Decisions

Running log of strategic decisions — channel choices, conventions, directions. Append-only;
newest at top. One line each, dated. Strategy and "why", not mechanics (mechanics → conventions).

---

## 2026-09-25 — ai-delivery-gap: двуязычная публикация, обобщённый финал, девять правил изложения
Статья про разрыв между локальным ускорением разработки и доставкой (ai-delivery-gap, issue #37)
вышла живой: <https://tellian.io/2026/09/25/ai-delivery-gap/> (RU 7471 слово + EN 9354, один пост,
WP 326). Три решения владельца, все общего действия:
- **Публикуем двуязычно** — RU и EN одним постом с переключателем, как и прежние лонгриды;
  деривативы для Telegram/LinkedIn по этой статье не делаем (объём и плотность цифр под них не
  ложатся — это справочный текст, а не хук).
- **Финал — обобщение, а не чек-лист.** Блок «Понедельник» с пошаговым списком забракован прямо:
  «выглядит слопом, просто убери». Ship-bar «есть проверяемое действие на понедельник» закрывается
  формулировкой принципа (прошлые инциденты как готовый набор заведомых дефектов), а не инструкцией.
  Общее правило: проверяемое действие в финале даём мыслью, из которой действие следует.
- **Девять правил изложения** (цифра только с источником и в порядке «кто мерил → что получилось»;
  мысль не обрывается на половине; каждый буллет читается отдельно; термин объясняется там, где
  стоит; в TL;DR нет ничего, что требует пояснения; вывод называет лекарство; три уровня структуры;
  блок в рамке = тезис на входе + обобщение на выходе; если статья про ИИ — ИИ виден в каждом
  разделе). Полностью — в `notes/owner-taste.md` (2026-09-24), разбор — в
  `pieces/20260924_ai-delivery-gap/review-owner-round2.md`.
Почему это важно для процесса: ни три прожарки, ни три раунда фактчека не поймали ни одного из этих
пунктов — они проверяют честность и качество письма, но не «на чём текст стоит» и «кому он нужен».
Вопрос о базе и адресате задаём на брифе, до драфта.

---

## 2026-09-01 — Transformer piece: angle pivoted to the positive "AI Day / adventure of one idea" framing
The transformers piece (ai-day-transformers, issue #26) started as "an underappreciated paper" —
a corrective, slightly grievance-shaped angle. After owner review the frame flipped to the
**positive story of one idea growing up**: attention born 2014, freed of recurrence in 2017, scaling
into the LLM era — a **12-year "AI Day" anniversary**. Same honest boundaries kept (2014 attention
was a bolt-on to an RNN, not the parallelization win; the frontier still runs on attention; Mamba/SSM
only in niche hybrids). Why: the celebratory lineage lands better for a general reader than a
"they got it wrong" corrective, without softening the technical honesty. Shipped RU+EN (blog),
Telegram; LinkedIn draft ready.

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
