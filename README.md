# publishing

A harness for researching, writing, fact-checking and shipping **articles, notes and small
research** for the [tellian.io](https://tellian.io) blog, Telegram and LinkedIn.

This repo is not just a folder of drafts — it's an opinionated workflow plus a knowledge base
that compounds: every piece we ship makes the next one cheaper to research and harder to get wrong.

## What's here

```
CLAUDE.md            The harness — read this first. Lifecycle, roles, git, knowledge base.
AGENTS.md            Short brief for Codex/CLI agents working in this repo.
blueprint/           Conventions and accumulated lessons about how we work.
pieces/              One folder per piece: brief → outline → draft → fact-check → roast → ship.
templates/           Copy these to start a piece.
wiki/                Evergreen knowledge: topics, anti-patterns, catalog of shipped pieces.
ontology/            Lightweight graph linking pieces ↔ topics ↔ sources.
sources/             Curated reading list / source library.
notes/               Decision log and session reflections.
scripts/             Local RAG (semantic search over everything we've written).
.claude/             Agents (researcher, fact-checker, editor, librarian) and skills.
```

## The lifecycle

Every non-trivial piece moves through five stages, each leaving an artifact:

**BRIEF → DRAFT → FACT-CHECK → CRITIQUE → SHIP**

1. **BRIEF** — pre-register the angle, audience, channel and ship-bar (`brief.md`).
2. **DRAFT** — outline, then write (`outline.md` → `piece.md`).
3. **FACT-CHECK** — every load-bearing claim gets a resolvable source (`fact-check.md`).
4. **CRITIQUE** — an independent editorial roast, then improve (`roast.md`).
5. **SHIP** — user gates, publish, derive channel variants, close the loop.

## Starting a piece

```bash
slug=my-article-slug
mkdir -p pieces/$(date +%Y%m%d)_$slug
cp templates/{brief,outline,fact-check,roast,piece}.md pieces/$(date +%Y%m%d)_$slug/
git switch -c piece-$slug
```

Then fill `brief.md` first. See `pieces/README.md` for the full convention.

## Knowledge base

- **Search what we've written:** `python3 scripts/rag_search.py "your question"`
- **Topics & takes:** `wiki/topics/`
- **What we've debunked / clichés to avoid:** `wiki/topics/anti-patterns.md`
- **Shipped pieces:** `wiki/pieces/INDEX.md`

After anything ships, the `librarian` agent keeps these in sync (Close-the-Loop Protocol in `CLAUDE.md`).

## Conventions in one line

Feature branch + PR (never push to main) · persist work to disk as you go · every claim sourced ·
critique before ship · publish only after a user gate · keep the indexes current.
