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

<!--
L01 — <rule>.
  Why: <what happened>.
  Anchor: pieces/<slug> / notes/reflections/<date>-<topic>.md
-->
