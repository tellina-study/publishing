# Ontology (lightweight)

A small, structural graph linking what we produce. **Deliberately minimal** — it stores
references and links, never article text (that's what RAG and the pieces themselves are for).

We keep it as a plain Markdown table (`store.md`) rather than RDF/SPARQL: at this scale a table
is queryable by eye, by grep, and by RAG, with none of the triple-store overhead. If the graph
ever outgrows a table, promote it to `store.ttl` + a query script — but not before.

## Model

Four node types, three link types.

| Node | Is | Identified by |
|------|-----|---------------|
| **Piece** | An article / note / research write-up | its slug |
| **Topic** | An evergreen subject | `wiki/topics/<topic>.md` |
| **Source** | A citable external source | row in `sources/INDEX.md` |
| **Status** | draft / review / shipped / hold | enum |

| Link | Meaning |
|------|---------|
| **covers** | Piece → Topic |
| **cites** | Piece → Source |
| **hasStatus** | Piece → Status |

## Maintenance
- The `librarian` appends rows to `store.md` on every SHIP (Close-the-Loop trigger).
- One row per (Piece, link, target). Orphan rule: every shipped Piece **covers** ≥1 Topic and
  **cites** ≥1 Source.
- Never duplicate prose into the graph — links only.
