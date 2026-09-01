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

L06 — A social hook must be CURRENT — never build on a limitation the tooling already fixed.
  Why: round-1 LinkedIn drafts hooked on "AI can't multiply / can't count letters in strawberry."
  Both are outdated — calculators/tools closed them long ago; presenting them as "today AI can't X"
  is simply wrong. Rule: before a fact-hook ships, ask "is this still true in <current year>?" Prefer
  recent (last ~12 mo) or fundamental-and-still-true. Anchor: pieces/20260901_lessons-linkedin-announce
  / notes/owner-taste.md «Факт и актуальность»

L07 — Simplify past the point that feels enough; plainest word wins over the stylist's clever/idiomatic one.
  Why: Max asked to simplify the LinkedIn post THREE times after it already read clean. Each pass we
  traded "correct-but-clever" for plain: trusted→let, corporate→company, delivers→brings, "price in the
  risks"→"risks and all", "putting together/publishing openly"→"starting/putting it online", "judge a
  use case before you bet on it"→"tell where it's worth using". stylist-en (Williams & Bizup) is the
  EN equivalent of Нора Галь for our English pieces — but its idiomatic pick isn't always the *simplest*;
  do one more plain-language plane after it. Anchor: pieces/20260901_lessons-linkedin-announce
  / blueprint/channels/linkedin.md

L08 — English social posts go through stylist-en, not stylist-ru — pick the tool by the TEXT's language.
  Why: "гони Нору Галь" on an English post means the English clarity pass (stylist-en / Williams &
  Bizup), not stylist-ru. Same principles (kill deadwood, verb over construction, clarity), right tool.
  Anchor: pieces/20260901_lessons-linkedin-announce

<!--
L01 — <rule>.
  Why: <what happened>.
  Anchor: pieces/<slug> / notes/reflections/<date>-<topic>.md
-->
