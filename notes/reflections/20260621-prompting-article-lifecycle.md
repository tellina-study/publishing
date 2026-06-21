# Reflection: 20260621 — prompting article, full lifecycle to SHIP

## What we did
Took the near-final prompting WIP («Язык, форма и место») all the way to published across blog
(RU+EN), LinkedIn and Telegram. In one session: applied 19 owner formatting edits (cards, TL;DR,
emoji subheads, finale reorder, de-Russian-centering); ran a 4-way roast (editor / mirror /
reader-fan / stylist) and folded it; deduped the per-model section + trimmed TOON; wrote the EN
adaptation + stylist-en; produced Telegram (RU) and LinkedIn (EN) derivatives; aligned the files
to the WordPress publisher (`en.md`/`ru.md` + YAML frontmatter); changed the Close-the-Loop rule
to track `main`; and ran the full ship close-the-loop. Three PRs (#7, #12, #13).

## What we learned
- **The biggest quality lever was applying the owner's edits faithfully + generalizing them**, not
  more agents. The roast agents earned their keep mostly by catching *seams my own edits introduced*
  (triple "середина проваливается", the 🎯 emoji collision, the TOON-merge dup) — i.e. verification
  of my work, not original critique.
- **Derivatives drift from the canon.** The old Telegram draft still said "русский ×3" after the
  canon was fact-corrected to ×2, and carried a проговор-leak the body had already purged. A
  derivative is a fork of the facts, not just the prose.
- **The publisher is a hard contract:** `en.md`/`ru.md` filenames, YAML frontmatter, title injected
  as `<h1>` (never repeated in the body). `--dry-run` is the cheap proof it parses.
- **`main` is the source of truth, so the KB must track `main`** — not wait for SHIP. RAG already
  did (post-merge hook); the doc-layer (INDEX, ontology) was the gap, which read as inconsistency
  the moment we merged-to-preview.

## What surprised us
- The owner merged the article to `main` mid-process *to preview/publish in a parallel session* —
  which exposed the RAG-vs-doc-layer asymmetry. A workflow detail (parallel publishing) drove a
  harness rule change.
- The owner's LinkedIn edit pushed *further* in the direction I'd taken: he replaced the personal
  "I dug into…" hook with a bare provocative headline, cut each bullet to one line, and removed the
  China-myth from the teaser (kept it for the article). Punchier than I'd dared.
- The new hook reminder fired on the very next merge ("pieces/ changed → sync doc-layer") —
  the rule self-demonstrated within the session.

## What to do differently next time
- **When deriving channel variants, diff the derivative's claims against the FINAL canon**, number
  by number — don't trust an earlier draft's facts.
- **Run `--dry-run` before declaring a piece publish-ready**, and confirm categories/tags against the
  site's real taxonomy *before* any real run (terms are created by name).
- **Capture the owner's edit in the same turn** (mirror + memory) — his edits are the highest-signal
  taste data we get.
- Consider a tiny **"canon → derivatives" fact-parity check** as a standing step before shipping
  derivatives.

## New ideas / pieces this generated
- A short meta-piece could come out of the harness itself: "running a bilingual AI publishing lab
  as a repo" — the public repo is already a showcase (owner is sharing it).
- Standing **fact-parity linter** for derivatives (numbers in telegram/linkedin must appear in the
  canon).

## Updates to make to the knowledge base
- Lessons → `blueprint/lessons-learned.md`: derivative fact-drift; publisher file contract +
  dry-run; KB-tracks-main; owner-edits-are-signal. (Done this session: L02–L05.)
- Decision → `notes/decisions.md`: Close-the-Loop rekeyed from SHIP to merge-to-main. (Done.)
- Ship close-the-loop for the piece itself: already done (INDEX→Published, topic `prompt-packaging`,
  anti-patterns, sources, ontology).
