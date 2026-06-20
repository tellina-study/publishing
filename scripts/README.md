# scripts/

Local semantic search over everything we've written and gathered. No API keys — it runs
sentence-transformers (`all-MiniLM-L6-v2`) + LanceDB entirely on your machine.

## Setup (once)
```bash
pip install -r scripts/requirements.txt   # first run also downloads the ~90MB model
python3 scripts/rag_ingest.py             # build the index
```

## Use
```bash
python3 scripts/rag_search.py "what have we written about agent memory"
python3 scripts/rag_search.py "telegram hook openings" --top 8 --category pieces
```

## Rebuild
Re-run `rag_ingest.py` after anything ships or the wiki/notes change (the `librarian` does this as
part of Close-the-Loop). The index lives at `$PUBLISHING_RAG_DB` (default
`~/.cache/publishing-rag_db`) and is gitignored — it's regenerable.

## What's indexed
The `GLOBS` list in `rag_ingest.py` is the contract: `pieces/`, `wiki/`, `notes/`, `sources/`,
`blueprint/`, `ontology/`. Add a directory there when you add a new content area.
