---
name: reflect
description: Write a session reflection and fold durable lessons and decisions into the knowledge base. Run after a substantial writing or research session. If in doubt, reflect.
---

# /reflect

Capture what this session taught us so it isn't re-learned next time.

## Recipe

1. **Pick the topic and date.** `topic` = the session's focus (kebab-case). `date` = YYYYMMDD.

2. **Write `notes/reflections/<date>-<topic>.md`** from this skeleton:

   ```markdown
   # Reflection: <date> — <topic>

   ## What we did
   ## What we learned
   ## What surprised us
   ## What to do differently next time
   ## New ideas / pieces this generated
   ## Updates to make to the knowledge base
   ```

   Keep it honest and specific — concrete misses are worth more than tidy summaries.

3. **Fold durable lessons** into `blueprint/lessons-learned.md` — anything about *how we work*
   that should change future behavior gets a numbered `L<NN>` entry.

4. **Fold decisions** into `notes/decisions.md` — anything strategic (a channel choice, a
   convention change, a direction) gets a dated line.

5. **Run the `librarian`** if the session shipped a piece, established a take, debunked a claim,
   or found a source — the reflection is not a substitute for Close-the-Loop.

6. Stay under 600 lines. `mkdir -p notes/reflections` first if needed.
