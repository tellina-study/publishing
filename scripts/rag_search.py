#!/usr/bin/env python3
"""Semantic search over everything we've written and gathered.

Usage:
    python3 scripts/rag_search.py "what have we said about agent memory"
    python3 scripts/rag_search.py "telegram hook openings" --top 8
    python3 scripts/rag_search.py "X" --category pieces --full

Index lives at $PUBLISHING_RAG_DB (default ~/.cache/publishing-rag_db). Build it first with
scripts/rag_ingest.py. Local-only: sentence-transformers (all-MiniLM-L6-v2) + LanceDB. No keys.
"""
import argparse
import os
import sys

DB_PATH = os.environ.get(
    "PUBLISHING_RAG_DB", os.path.expanduser("~/.cache/publishing-rag_db")
)
TABLE = "publishing_docs"
MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def validate_query(q: str) -> str:
    """Reject obvious mistakes early (unsubstituted placeholders, shell noise, empties)."""
    q = (q or "").strip()
    if not q:
        sys.exit("error: empty query")
    if len(q) < 3:
        sys.exit(f"error: query too short ({q!r}) — give a real phrase")
    bad = ["<query>", "<concept>", "<", ">", "&&", "||"]
    if any(tok in q for tok in bad):
        sys.exit(f"error: query looks like an unsubstituted placeholder: {q!r}")
    return q


def main() -> None:
    ap = argparse.ArgumentParser(description="Semantic search over the publishing corpus.")
    ap.add_argument("query", help="natural-language question")
    ap.add_argument("--top", type=int, default=5, help="number of results (default 5)")
    ap.add_argument("--category", help="filter: pieces | wiki | notes | sources | blueprint")
    ap.add_argument("--full", action="store_true", help="print full chunk, not a preview")
    args = ap.parse_args()

    query = validate_query(args.query)

    try:
        import lancedb
        from sentence_transformers import SentenceTransformer
    except ImportError:
        sys.exit(
            "error: missing deps. Install with:\n"
            "    pip install -r scripts/requirements.txt"
        )

    if not os.path.exists(DB_PATH):
        sys.exit(f"error: no index at {DB_PATH}. Build it: python3 scripts/rag_ingest.py")

    db = lancedb.connect(DB_PATH)
    if TABLE not in db.table_names():
        sys.exit(f"error: table {TABLE!r} not found. Run scripts/rag_ingest.py")
    tbl = db.open_table(TABLE)

    model = SentenceTransformer(MODEL)
    vec = model.encode(query, normalize_embeddings=True).tolist()

    rs = tbl.search(vec).metric("cosine").limit(max(args.top * 4, 20))
    if args.category:
        rs = rs.where(f"category = '{args.category}'")
    rows = rs.to_list()

    # Dedup by source, keep the best-scoring chunk per file.
    best = {}
    for r in rows:
        src = r["source"]
        if src not in best or r["_distance"] < best[src]["_distance"]:
            best[src] = r
    results = sorted(best.values(), key=lambda r: r["_distance"])[: args.top]

    if not results:
        print("(no matches — try rephrasing, or the corpus may not cover this yet)")
        return

    for i, r in enumerate(results, 1):
        score = 1 - r["_distance"]  # cosine similarity
        print(f"\n[{i}] {score:.3f}  [{r['category']}]  {r['source']}")
        if r.get("title"):
            print(f"    {r['title']}")
        text = r["text"].strip()
        print("    " + (text if args.full else text[:280].replace("\n", " ") + "…"))


if __name__ == "__main__":
    main()
