---
name: compile-wiki
description: Regenerate the wiki indexes from the pieces folder — refresh the pieces catalog, the topic links, and re-ingest RAG. Run when indexes have drifted from what's actually in pieces/.
---

# /compile-wiki

Rebuild the navigable layer from the source of truth (`pieces/`), so nothing is stale.

## Recipe

1. **Scan `pieces/`** — for each `pieces/<date>_<slug>/piece.md`, read its frontmatter
   (title, channels/targets, status, published URLs) and the SHIP verdict in `notes.md` if present.

2. **Regenerate `wiki/pieces/INDEX.md`** — one row per piece:
   `| date | title | slug | channels | status | published | folder |`. Group by status
   (published / in-review / draft). This file is a catalog — it may carry these columns.

3. **Refresh topic links** — ensure every topic referenced by a piece has a page under
   `wiki/topics/` and is linked from `wiki/index.md`. Do not invent metric tables in `index.md` —
   it stays navigation-only (pointers + currency notes).

4. **Refresh `wiki/topics/anti-patterns.md`** — make sure debunked claims from shipped pieces
   are captured.

5. **Verify constraints:** every wiki file < 600 lines, every internal link resolves, no orphan
   pages (a topic page nothing links to). Report violations; don't silently leave them.

6. **Re-ingest RAG** — `python3 scripts/rag_ingest.py`.

Delegate the mechanical sync to the `librarian` agent; this skill is the trigger and the
verification checklist.
