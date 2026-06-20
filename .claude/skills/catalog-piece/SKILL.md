---
name: catalog-piece
description: Register a finished piece into the knowledge base — add it to the pieces index, link its topics, record sources, and re-index RAG. Delegates the sync to the librarian.
argument-hint: [piece-slug] [status: draft|review|published]
---

# /catalog-piece <slug> <status>

Pull a finished (or shipped) piece into the knowledge base so it's findable and counted.

## Recipe

1. **Locate the piece** — `pieces/<date>_<slug>/piece.md`. Read its frontmatter (title, channels,
   targets, status, sources).

2. **Delegate to the `librarian`** with this brief:
   - Add/refresh a row in `wiki/pieces/INDEX.md`: title · slug · channel(s) · status · date ·
     published URL(s) · link to the piece folder.
   - For each topic the piece covers, create or extend `wiki/topics/<topic>.md` and link it from
     `wiki/index.md`.
   - Record Piece ↔ Topic ↔ Source ↔ Status rows in `ontology/store.md`.
   - Add any new reusable sources to `sources/INDEX.md`.
   - If the piece debunked a claim or named a cliché, add it to `wiki/topics/anti-patterns.md`.

3. **Re-ingest RAG** — `python3 scripts/rag_ingest.py`.

4. **Verify** — the piece now appears in `wiki/pieces/INDEX.md` and in
   `python3 scripts/rag_search.py "<a distinctive phrase from the piece>"`. Every file stays
   under 600 lines and internal links resolve.
