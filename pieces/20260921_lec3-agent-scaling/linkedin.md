<!-- Channel: LinkedIn (EN). Standalone post (no blog article behind it) — sourced from
     Lecture 3 v6.4 expansion (lessons.tellian.io course, tellina-study/AI-usage-lessons,
     library/lectures/lec-03/chapter-part3.md §4.3, chapter-part4.md §4.10).
     Style canon: blueprint/channels/linkedin.md. Brief: brief.md. Issue: #33.
     Fact-check: fact-check.md. Roast: roast.md. Mirror: mirror-verdict.md.
     STATUS: FINAL — fact-checked, roasted, mirror-checked, and the one open blocker (EN
     site deploy) is cleared. Verified this run (2026-09-22): lessons.tellian.io/en/lectures/
     lec-03/ shows "Lecture 3 · ~105 min · 67 slides". Ready for Max to post. -->

# LinkedIn — final

AI agents get things done — chain a few together without a plan and the system quietly
gets worse at its job, not better.

Ten steps at 99% reliability each don't add up to 99% overall — they multiply to around
90%. Reliability multiplies, it doesn't average. Teams often try to fix this by adding
more agents, and that can backfire: one recent study found an independent swarm of peer
agents amplifies errors about 17.2x compared to a single agent working alone — a
coordinator running the same agents holds it to about 4.4x (Kim et al., 2026). Same
headcount; the only thing that changed is who's allowed to act alone.

It shows up in cost too. A single agent burns roughly 4x the tokens of one chat call on
the same task; a multi-agent setup runs closer to 15x, by Anthropic's own numbers. And
it's not just theory: on a benchmark of realistic agent tasks called τ-bench, one model
solved 61% of tasks on a single try, but success on eight tries in a row — same task,
repeated — dropped under 25%. That gap is what "reliability" actually costs.

Three things that actually help:

🛑 Give every agent a hard stop — max steps, a cost ceiling, a repeat detector. Without
one, "keep trying until it works" is exactly what it does, on your budget, forever.

🧭 If you need more than one agent, put a coordinator in charge instead of running them as
equal peers. The topology matters more than the headcount.

🔍 Validate between steps, not only at the end. Catching an error at step 2 stops it from
compounding through steps 3 to 10 — this matters more than making any single step smarter.

Most of what gets called "we need an agent" also turns out to be a predictable sequence in
disguise — a fixed pipeline with a check between steps, not a model improvising its own
path. That version is usually cheaper, more reliable, and does the job about as well.

We just updated Lecture 3 of our course to go deep on exactly this — when an agent earns
its cost, and how to build one that doesn't run away from you. Free and open:
👉 lessons.tellian.io/en

If you just chat with an assistant day to day, none of this changes anything for you. If
you're the one deciding whether your product needs another agent, it might.

Where do you draw the line — what would make you trust a longer agent chain with something
you can't undo?

#AI #SoftwareEngineering #AIAgents #MachineLearning

---

**Word count (body, excl. hashtags):** ~305 — inside the 150–500 channel range.

**Provenance (for the record):**
- Content: Lecture 3 v6.4 (lessons.tellian.io course), §4.3 + §4.10 + Deep-dive box 4/5.
- Fact-checked against primary sources (`fact-check.md`): Kim et al. arXiv:2512.08296
  (Table 5, exact 17.2x/4.4x); Anthropic "How we built our multi-agent research system"
  (exact 4x/15x); τ-bench arXiv:2406.12045 (61.2% exact, pass^8 "<25%" — stated as "under
  25%" here, not an exact figure); arithmetic (0.99^10 ≈ 90.4%) verified.
- Roasted (`roast.md`, editor) and mirror-checked (`mirror-verdict.md`, owner-taste) — both
  REVISE-then-fixed; see those files for the full findings-to-fix mapping.
- CTA blocker cleared 2026-09-22: EN page confirmed live on v6.4/67 slides (parity closed
  per sibling-session report, cross-checked here via direct fetch — see status line above).

**History:** v1 (anecdote hook, rejected) → v2 (hook rewritten as direct insight, per owner
correction) → v3 (+2 tips, explicit CTA) → v4 (+2 dimensions, +1 tip, ~350w target) → v5
(fact-check + roast + mirror fixes applied, CTA held pending EN deploy) → **final** (CTA-A
confirmed true, blocker cleared).
