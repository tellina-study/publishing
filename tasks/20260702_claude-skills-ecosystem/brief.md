# Brief — Claude Code skills ecosystem review (inbound from sibling lab)

**Source:** GitHub issue #15. Draft produced by `workain/agent-lab-manager` (sibling AI-agent lab,
same operator), branch `docs-glebis-claude-skills-landscape`. Requested to go through our normal
CREATE→ROAST→SHIP pipeline before publishing on tellian.io.

**Angle:** An audit of the top "Claude Code skills" GitHub repos with one load-bearing, reproducible
finding — a 2.2k-star toolkit (`rohitg00/awesome-claude-code-toolkit`) ships MCP configs referencing
npm packages under the `@anthropic/` scope that do not exist (404) → namespace-squatting risk class.

**Audience:** technical-but-general readers wiring up Claude Code agents / MCP.
**Channels (owner-confirmed):** tellian.io blog (bilingual EN+RU, canonical) + Telegram + LinkedIn derivations.

**Ship-bar:** every load-bearing claim reproducible this run; honest framing (no over-claim); voice
matches tellian (first-person, warm, on равных, "делюсь интересным" — not gotcha/scold); the
`@anthropic`-scope finding is the single spine.

**Verified this run (orchestrator):**
- `@anthropic/mcp-ghidra`, `@anthropic/mcp-figma`, `@anthropic/mcp-server-figma` → 404. `kubectl-mcp-app`,
  `mcp-terraform` → 404. `defi-mcp` → 200. Core finding real.
- Live stars match draft within drift (superpowers 244,250 vs 243,958 in text; etc.).
- **Correction:** real Anthropic scope is `@anthropic-ai` (`@anthropic-ai/sdk`, `@anthropic-ai/claude-code` → 200);
  `@anthropic/*` → 404. So `@anthropic/` is NOT the official scope — only a plausible look-alike.

## DO NOT
- Do not repeat the draft's "live supply-chain hole" framing — it's a *latent, contingent* namespace risk.
- Do not claim `@anthropic/` "reads as official" without the correction (official = `@anthropic-ai`).
- Do not keep the victory-lap register (repeated lab-credential flexing, "you were too lazy to read it").
- Do not freeze precise star counts into an evergreen post without a dated "live API pull" anchor.
- Do not claim per-commit/file/line traceability in the body while showing zero links.
