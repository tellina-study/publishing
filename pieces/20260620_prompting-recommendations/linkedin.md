<!-- Channel: LinkedIn (EN). Style: insight-as-hook → article, short, non-categorical,
     casual-user caveat at the end, engaging close. See memory: linkedin-style / owner-taste. -->

**I dug into a question that sounds trivial: when you write a prompt, how much does the *packaging* — the language, the format, where you put things — actually change the answer? I went through the research and my own daily use, and a few results genuinely surprised me.**

Three that stuck with me:

🌐 Language looks more like a cost lever than a compression one. Instructions in English tend to be a bit cheaper and more accurate — a non-English prompt can run ~2× the tokens (Russian does). And "write in Chinese to save tokens" mostly doesn't hold on the popular models.

📍 Placement seems to matter more than trimming words. Attention leans toward the start and end of the context window, so your key facts — and the actual question — tend to land better at the edges than buried in the middle.

🧱 Simple Markdown usually does better than heavier formats (JSON/XML) for the instruction itself — those are worth keeping for data.

I wrote up the full picture — worked examples, a per-task breakdown, and the sources — here:
https://tellian.io/2026/06/21/language-format-placement/

And honestly — if you just chat with an assistant now and then, the first two are about all you need. The rest is really for people wiring prompts into a product.

Curious how this lands for others: does format and placement move the needle in your experience?
