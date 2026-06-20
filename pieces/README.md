# pieces/

One folder per piece, named `YYYYMMDD_<slug>`. Each piece moves through the lifecycle, leaving
one artifact per stage. Persist as you go — never keep the work only in chat.

## Lifecycle: BRIEF → DRAFT → FACT-CHECK → CRITIQUE → SHIP

| Stage | File | Owner | Gate to next stage |
|-------|------|-------|--------------------|
| BRIEF | `brief.md` | orchestrator | Angle, audience, channel, ship-bar and DO-NOT list agreed |
| DRAFT | `outline.md` → `piece.md` | writer (+ `researcher`) | Outline approved, then draft written |
| FACT-CHECK | `fact-check.md` | `fact-checker` | Every load-bearing claim resolved or cut |
| CRITIQUE | `roast.md` | `editor` (independent) | Roast verdict SHIP, criticals fixed |
| SHIP | `piece.md` (final) + `notes.md` | orchestrator + user | **User gate**, then publish + close the loop |

## Start a piece

```bash
slug=my-slug
dir=pieces/$(date +%Y%m%d)_$slug
mkdir -p "$dir"
cp templates/{brief,outline,fact-check,roast,piece}.md "$dir"/
git switch -c piece-$slug
```

Fill `brief.md` **first**. The brief's DO-NOT list and ship-bar are what the `editor` checks the
draft against at the end.

## Conventions

- The canonical version is the longest-form target (usually the blog article). Channel variants
  (Telegram, LinkedIn) are derived from it and noted in `piece.md` frontmatter.
- Keep each file under 600 lines.
- After SHIP: run `/catalog-piece <slug> published` so the wiki, ontology and RAG pick it up.
- Folders here are the **source of truth**; `wiki/pieces/INDEX.md` is the regenerable catalog.
