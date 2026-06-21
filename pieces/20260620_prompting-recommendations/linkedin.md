<!-- Channel: LinkedIn (EN). Shape: 150–500 words, takeaway-led, light formatting.
     Derivative of en.md. Drop the blog URL in at ship ({{BLOG_URL}}). -->

**Most prompt advice is folklore. I checked the popular tricks against the research and my own daily use — here's what actually moves the needle.**

Two things every prompt spends: a **token budget** (money + context window) and an **attention budget** (the model reads the edges of the window well and the middle poorly). Almost every good practice just spends those two wisely.

What holds up:

🌐 **Write instructions in English.** Another language doesn't compress your prompt — it inflates it. A non-English language runs multiples more tokens (Russian ≈ ×2). And "write in Chinese to save tokens" is a myth on the popular models: the tokenizer fragments the ideographs and any density gain disappears.

📍 **Placement beats compression.** Attention is U-shaped — put the key facts and the real question at the edges, not the middle. And the *reliable* context length is far shorter than the spec sheet claims.

🧱 **Simple Markdown wins.** It's what models saw most in training; keep heavy formats (JSON/XML) for data, not for the instructions. Forcing rigid JSON output can even choke the model's reasoning.

✂️ **Brevity helps less than the hype.** Cutting filler saves a real ~15–20% on instructions, not the viral "−75%" — and it pays off in agents, not in one-off chats. Never squeeze a reasoning model's chain of thought.

The order that matters: **sort out placement and format first, then language, and compress last** — compression saves the least and breaks meaning the easiest.

Full write-up — worked examples, a per-task stack (chat / production prompt / agent / data), and 40+ sources — here: {{BLOG_URL}}
