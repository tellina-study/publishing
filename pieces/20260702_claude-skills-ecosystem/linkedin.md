# LinkedIn — EN

There are dozens of "awesome Claude skills" repos. The biggest has more stars than most programming languages. And a star count tells you nothing about whether anyone actually checked what's inside.

So I went through the seven biggest. Here's the shortlist — plus one you should not copy blindly.

🟢 **anthropics/skills** — Anthropic's own, production-grade (the document skills literally power Claude's file-creation feature). Start here.
🟢 **obra/superpowers** (244k★) — not a bag of skills but a whole enforced workflow: brainstorm → plan → build test-first → review. Reach for it if you want a process.
🟢 **glebis/claude-skills** — a tidy ~90-skill personal set. The browsable middle.
🔵 **jqueryscript** / **travisvn** — link indexes, good for discovering what else is out there.
🟡 **ComposioHQ** — its "1000+ skills" headline is really 30–40.
🔴 **rohitg00/awesome-claude-code-toolkit** — its MCP configs tell your agent to install npm packages under the `@anthropic/` scope that don't exist (404). That scope isn't even Anthropic's (it's `@anthropic-ai`). An official-looking, unclaimed namespace is a slot waiting to be squatted. Don't paste those configs.

Two things I took away:
- Skills give a real but *conditional* lift — a few that reliably fit your task beat a hundred installed "just in case."
- Give any repo a 15-minute read before you trust it: `npm info` every package it names, and check what runs automatically. Popularity isn't a safety check.

(If you just chat with an assistant now and then, you don't need any of this — it's for people wiring up agents.)

Full breakdown, with how to install and vet each: https://tellian.io/2026/07/02/claude-skills-collections/

Which skills repo are you actually running — and did you read past the README?
