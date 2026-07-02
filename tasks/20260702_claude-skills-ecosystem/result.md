# Result — Claude skills collections field guide

**Verdict: SHIPPED (live).** Published to tellian.io on 2026-07-02.

- **Live URL:** https://tellian.io/2026/07/02/claude-skills-collections/ (verified HTTP 200, status `publish`, bilingual EN/RU switcher present)
- **WP post id:** 271 (idempotent — re-run `wp_publish.py` updates, never duplicates)
- **Issue:** tellina-study/publishing#15
- **Files:** `pieces/20260702_claude-skills-ecosystem/{en,ru}.md`

## What it is
Reader-service field guide for someone shopping for Claude Code skills: do skills work
(production + one arXiv benchmark, honest ceiling) → map of 7 collections with stars, freshness,
and one pick-reason each → which to trust (security pass as trust signal) → how to install → how to
use skills well. Every repo mention links to GitHub.

## Load-bearing finding (verified this run)
`rohitg00/awesome-claude-code-toolkit`'s MCP configs reference npm packages under the `@anthropic/`
scope that do not exist (`mcp-ghidra`, `mcp-figma`, `mcp-server-figma`, `kubectl-mcp-app`,
`mcp-terraform` → all 404; `defi-mcp` → 200). Real Anthropic scope is `@anthropic-ai` (`@anthropic-ai/sdk`,
`@anthropic-ai/claude-code` → 200). A plausible-but-unclaimed official-looking scope pointing at
missing packages = latent namespace-squatting risk.

## Process
Intake from sibling lab draft (issue #15) → fact-check (orchestrator, re-verified core + found the
@anthropic-ai scope correction) → 3-lens roast (editor/mirror/reader → REVISE) → **full reframe** on
owner override (v1 was inward-facing "our audit"; v2 serves the skill-seeker) → effectiveness research
(arXiv 2604.04323, honest "conditional lift") → install instructions verified against Claude Code docs
→ every repo linked → stylist-en + self RU polish (stylist-ru API-failed twice) → 2 cold readers
(both "install + share") → published live on owner gate.

## Owner calls captured (→ owner-taste.md)
- Article = service to the reader, not a report on our work; our audit is a trust signal, not the subject.
- Title must be reader-benefit, not self-congratulation.
- Add TL;DR up front (value without reading); maintenance/freshness signal; per-repo pick bullets; repo links; install steps.

## Open (deferred, non-blocking)
- Length ~top of range (EN 2350 / RU 2150 words). Reader-flagged the 7-repo bullets as skimmable;
  owner chose to ship. Option B (trim bullet/table duplication) left on the table for a future pass.
- Telegram + LinkedIn derivations not yet produced (owner said publish the blog; derivations pending his go).
