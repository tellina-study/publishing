# Ontology store

Structural links between pieces, topics and sources. Appended by the `librarian` on each SHIP.
See `README.md` for the model. One row per link.

| Piece (slug) | Link | Target | Notes |
|--------------|------|--------|-------|
| language-format-placement | covers | prompt-engineering | |
| language-format-placement | covers | prompt-packaging | data format / structure of the prompt |
| language-format-placement | covers | tokenization | tokenizer tax across languages |
| language-format-placement | covers | context-engineering | placement / lost-in-the-middle |
| language-format-placement | cites | sources/INDEX.md#lost-in-the-middle | Lost in the Middle (Liu et al.) — position effect |
| language-format-placement | cites | sources/INDEX.md#tokenizer-tax | Tokenizer Tax (Petrov et al.) — 25 European languages |
| language-format-placement | cites | sources/INDEX.md#toon-benchmark | TOON format vs JSON token/accuracy benchmark |
| language-format-placement | hasStatus | published | SHIP; live 2026-06-21 (issue #3). Blog https://tellian.io/2026/06/21/language-format-placement/ (RU+EN); LinkedIn https://www.linkedin.com/posts/maximlevko_activity-7474523958642479106-gp3l; Telegram posted (URL n/a) |
| claude-skills-collections | covers | claude-code-skills | field guide to the 7 biggest Claude Code skills collections |
| claude-skills-collections | covers | vetting-a-skills-repo | how to trust/vet a skills repo before use |
| claude-skills-collections | covers | supply-chain-security | hallucinated npm packages under a look-alike scope |
| claude-skills-collections | cites | sources/INDEX.md#skills-in-the-wild | Skills in the Wild — Terminal-Bench lift 57.7%→65.5% |
| claude-skills-collections | cites | sources/INDEX.md#anthropics-skills | anthropics/skills — first-party vetted skills |
| claude-skills-collections | cites | sources/INDEX.md#obra-superpowers | obra/superpowers — skills + enforced workflow |
| claude-skills-collections | cites | sources/INDEX.md#rohitg00-toolkit | rohitg00 toolkit — the namespace-squatting risk case |
| claude-skills-collections | cites | sources/INDEX.md#claude-code-docs | Claude Code docs — skills/plugins/MCP install |
| claude-skills-collections | hasStatus | published | SHIP; live 2026-07-02 (issue #15, wp_post_id 271). Blog https://tellian.io/2026/07/02/claude-skills-collections/ (EN+RU); Telegram + LinkedIn derivations pending |
