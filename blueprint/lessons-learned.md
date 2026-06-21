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

<!--
L01 — <rule>.
  Why: <what happened>.
  Anchor: pieces/<slug> / notes/reflections/<date>-<topic>.md
-->
