---
slug: "lec3-agent-scaling"
title: "When an agent earns its cost (and when a workflow beats it)"
date: 2026-09-21
channels: [linkedin]
audience: "practicing engineers/PMs who ship or are pressured to ship agentic features; LinkedIn feed, ~5-second skim"
status: drafting
issue: "33"
---

# Brief: When an agent earns its cost

## Angle
More agents is not an upgrade by default — it's a quantifiable reliability and cost trade
that usually loses unless the task is genuinely unpredictable and widely parallel. A plain
predetermined workflow (or a single agent) beats a multi-agent "swarm" on most real tasks,
and the topology of the multi-agent system (coordinator vs swarm) changes the blast radius
of errors by ~4x for the same headcount.

## Why now / why us
Lecture 3 of the course just went from 55 to 67 slides (v6.4, EN parity merged today) —
§4.3/§4.10 added a quantified failure catalog and a reliability-compounding framework that
isn't in the typical "AI agents are the future" LinkedIn discourse. First pass at insight
candidates from this material was rejected by the owner as recycled press facts (Air Canada,
Stanford legal-AI study, BM25 mythbusting — all already everywhere). This angle survived a
second, stricter pass: quantified, source-cited, non-consensus, actionable tomorrow.

## Audience & altitude
LinkedIn feed — engineers/PMs deciding architecture, not researchers. No ML background
assumed beyond "what's an agent." Should leave with one number they didn't have before and
a one-line decision rule, not a taxonomy.

## Ship-bar
- [x] Hook is the insight itself, stated directly — not a concrete/dated case as an intro.
      **Supersedes the line below** (owner correction, 2026-09-21, on this same draft — see
      `blueprint/channels/linkedin.md` log): the channel canon's "concrete case > abstract
      stat" rule applies to announce-posts selling entry into other material; for an
      insight-post the hook IS the claim, a case (if used at all) comes after as illustration.
- [ ] Every number sourced, both flagged `[VFY-day-of]` in source material and independently
      re-checked before ship (PocketOS/Zenity/Euronews; Kim et al. arXiv:2512.08296)
- [ ] 150–500 words, cuts hard — one paragraph per beat, no second "why it matters" clause
- [ ] CTA has no "if you've…" framing; closes on an open question
- [ ] Confirms lessons.tellian.io actually reflects v6.4 before the post says "we just expanded this"

## DO NOT
- Don't reduce this to "AI agents bad" — the piece is about when escalation pays, not a
  blanket dismissal (course's own framing explicitly rejects both "AI solves everything" and
  "AI is overhyped")
- Don't list all five workflow patterns by name in the post — that's article-depth, not
  post-depth; name the idea (predetermined pipeline with a check), not the taxonomy
- Don't stack more than 2 numbers in one post — cut, don't cram (channel canon: "cut hard")
- Don't invent or guess a lecture-specific URL — link to lessons.tellian.io/en (verified
  precedent), not a guessed /lecture-3 path

## Narrative spine
1. Hook: PocketOS case (April 2026) — agent deletes prod DB + backups in 9 seconds via an
   over-privileged token it found on its own.
2. Generalize: reliability multiplies, not averages (p^n); "fixing" it with more agents
   often backfires — swarm vs coordinator topology, ~17x vs ~4x error amplification for the
   same headcount.
3. What actually works: most "we need an agent" asks are a predetermined sequence in
   disguise — a fixed pipeline with a check between steps.
4. CTA: this is the judgment call Lecture 3 just built a decision framework around — link.
5. Casual-reader carve-out + open closing question.

## Sources to start from
- `lessons` repo (folder 288, tellina-study/AI-usage-lessons), `library/lectures/lec-03/chapter-part3.md` §4.3 (workflow vs agent, multi-agent math)
- Same repo, `chapter-part4.md` §4.10 (PocketOS case, failure catalog) and Deep-dive box 4/5
- Kim et al. (2026), arXiv:2512.08296 — multi-agent topology error amplification
- Zenity / Euronews (2026-04-28) — PocketOS incident

## Channel plan
- LinkedIn only, standalone (no blog article behind it — this is source material from the
  course itself, not a piece we're also shipping to tellian.io).
