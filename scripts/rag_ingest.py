#!/usr/bin/env python3
"""(Re)build the local semantic index over the publishing corpus.

Usage:
    python3 scripts/rag_ingest.py          # rebuild the index
    python3 scripts/rag_ingest.py --dry    # list what would be ingested, don't build

Run after anything ships (Close-the-Loop) or after editing the wiki/notes. The GLOBS list below
is the contract for what is searchable — edit it when you add a new content directory.

Local-only: sentence-transformers (all-MiniLM-L6-v2) + LanceDB. No API keys.
"""
import argparse
import glob
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.environ.get(
    "PUBLISHING_RAG_DB", os.path.expanduser("~/.cache/publishing-rag_db")
)
TABLE = "publishing_docs"
MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# (glob, category) — what gets indexed.
GLOBS = [
    ("pieces/**/*.md", "pieces"),
    ("wiki/**/*.md", "wiki"),
    ("notes/**/*.md", "notes"),
    ("sources/**/*.md", "sources"),
    ("blueprint/**/*.md", "blueprint"),
    ("ontology/**/*.md", "ontology"),
]
SKIP_NAMES = {"README.md"}  # scaffolding noise; real content gets indexed

CHUNK_CHARS = 1800
OVERLAP = 200


def chunk(text: str):
    text = text.strip()
    if len(text) <= CHUNK_CHARS:
        return [text] if text else []
    out, i = [], 0
    while i < len(text):
        out.append(text[i : i + CHUNK_CHARS])
        i += CHUNK_CHARS - OVERLAP
    return out


def first_heading(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def collect():
    docs = []
    for pattern, category in GLOBS:
        for path in glob.glob(os.path.join(REPO, pattern), recursive=True):
            if os.path.basename(path) in SKIP_NAMES:
                continue
            try:
                with open(path, encoding="utf-8") as f:
                    text = f.read()
            except (OSError, UnicodeDecodeError):
                continue
            if not text.strip():
                continue
            rel = os.path.relpath(path, REPO)
            title = first_heading(text)
            for idx, ch in enumerate(chunk(text)):
                docs.append(
                    {"source": rel, "category": category, "title": title,
                     "chunk_idx": idx, "text": ch}
                )
    return docs


def main() -> None:
    ap = argparse.ArgumentParser(description="Rebuild the publishing RAG index.")
    ap.add_argument("--dry", action="store_true", help="list docs, don't build")
    args = ap.parse_args()

    docs = collect()
    files = sorted({d["source"] for d in docs})
    print(f"{len(files)} files → {len(docs)} chunks")
    if args.dry:
        for f in files:
            print(f"  {f}")
        return
    if not docs:
        print("nothing to ingest yet — write some pieces first")
        return

    try:
        import lancedb
        from sentence_transformers import SentenceTransformer
    except ImportError:
        sys.exit(
            "error: missing deps. Install with:\n    pip install -r scripts/requirements.txt"
        )

    model = SentenceTransformer(MODEL)
    vectors = model.encode(
        [d["text"] for d in docs], normalize_embeddings=True, show_progress_bar=True
    )
    for d, v in zip(docs, vectors):
        d["vector"] = v.tolist()

    db = lancedb.connect(DB_PATH)
    if TABLE in db.table_names():
        db.drop_table(TABLE)
    db.create_table(TABLE, data=docs)
    print(f"indexed {len(docs)} chunks → {DB_PATH} (table {TABLE})")


if __name__ == "__main__":
    main()
