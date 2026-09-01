---
title: "AI Day: how translating a long sentence grew into ChatGPT"
slug: ai-day-transformers
status: draft
categories:
- AI
- Deep Learning
tags:
- Transformers
- Attention
- LLM
- History of AI
- Neural Networks
---

> Twelve years ago a paper came out about machine translation. Step by step, ChatGPT grew out of it.

September 1 — the day the school year traditionally starts, Knowledge Day in Russia and much of the post-Soviet world. It also makes a fine birthday for artificial intelligence.

ChatGPT — late 2022. Transformers, the architecture it stands on — 2017. And the idea that transformers and everything else sprouted from? Dig to the very root and you land on September 1, 2014, in a paper from Montreal. Twelve years ago to the day, right on Knowledge Day.

You couldn't ask for a better excuse to wish AI a happy birthday. The date does the work for you.

That paper was about a narrow, practical thing: teach a program to "look" at the right words while it translates a long sentence. Twelve years later, that grew into systems that write code and hold a conversation. The idea got a name — **attention** — and everything started there.

## What attention is — and why nothing works without it

Picture translating a long sentence out of a language you barely know. You can't hold the whole thing in your head at once. You look at the first chunk, translate it, move your eyes to the next, keep the link to the beginning in mind — which noun is the subject, what that pronoun points back to — and so on to the period. At every moment you're looking at the word that matters right now, not at the whole sentence at once. And when you reach the verb at the end of the German sentence, you still remember who, back at its start, was doing the thing.

That's **attention** — a program's ability, at each step, to look at exactly the source words it needs right now, instead of trying to take everything in at one gulp.

Early machine translators worked differently. The program read the whole sentence start to finish and tried to cram its meaning into one cramped cell — a short list of numbers of a fixed size, an extremely compressed summary. Then, working from that one distillation and no longer looking at the original, it assembled the translation.

For a short phrase the trick held: everything fit in the summary. On a long one the cell overflowed. A whole sentence's meaning won't fit in a handful of numbers — something has to be dropped, and what gets dropped is exactly what didn't fit. "The cat sat on the mat" you can still translate this way. A half-page paragraph, no.

Attention broke that squeeze open. No need to compress everything into one box and hope it all survives — you can glance back at any word of the original at any moment and take it directly. This is the mechanism that later ended up on the famous sign. But it was invented earlier.

## 2014, Montreal: fixing the translation of long sentences

A team in Yoshua Bengio's lab (Dzmitry Bahdanau, Kyunghyun Cho; MILA, University of Montreal) was wrestling with machine translation. The model translated short phrases decently — and fell apart on long ones. The longer the sentence, the worse the translation. Not a minor rough edge — a wall the whole approach ran into.

The [paper](https://arxiv.org/abs/1409.0473) names the diagnosis without hedging: *"the use of a fixed-length vector is a bottleneck."* A long sentence simply won't fit — and everything that doesn't fit is lost. Half the work in science is naming the disease correctly. Here they named it, and it became clear where to strike.

And they struck like this. While assembling the translation, let the model, at each word, **look** at all the words of the original and take exactly what matters right now — with different weights, stronger here, weaker there. Not a compressed retelling of the whole sentence, but a live gaze sliding across the source. That's how attention was born.

The model itself had a dry name — RNNsearch; the word "attention," which would later carry an entire era, was added, by Bahdanau's own account, by Bengio — on one of the final passes, almost in passing. The reasoning was simple: a human really does keep one or two words in mind at a time, not the whole sentence at once. The word turned out to be apt — but it was set down without fanfare.

## Why "real AI" still didn't arrive after 2014

The idea was excellent — and it hit the old design of the models themselves.

- **Recurrence.** A model of those years read text in strict order, word by word, holding in mind a short "summary" of everything it had read so far. Each next word went on top of that summary. Like reading a book through a slit: one word visible, the next only when you slide further.
- **And here's the drag.** Training ran in that same strict order: each step waited on the one before, and there was no way to split the work across many hands at once. So training the model on enormous volumes of text was agonizingly slow — and no amount of "add more power" really helped, because the next step still ran into the previous one. Computing became too slow and too expensive to grow at any serious scale.

Attention back then cured one disease — the overflowing cell. But the second, the slowness of reading in sequence, it never touched: it stayed a bolt-on over the old design, which still read word by word. Training on big data got no faster. No revolution in models came after 2014 — not because the idea was weak, but because it had nowhere to stretch: attention could look in the right place, but it was bolted to an engine you couldn't rev. For the idea to fire, someone had to swap the engine itself. That took three years.

## 2017: strip out everything else, keep attention alone

Three years later a different team took it on — Ashish Vaswani and seven colleagues. And they didn't build their model out of thin air. Behind them was a whole arsenal of other people's findings:

- the [encoder-decoder scheme from Cho](https://arxiv.org/abs/1406.1078);
- the line of work on attention — first Bahdanau, then [Luong](https://arxiv.org/abs/1508.04025) refined it;
- residual connections from image recognition ([ResNet](https://arxiv.org/abs/1512.03385));
- layer normalization ([layer norm](https://arxiv.org/abs/1607.06450));
- techniques against overfitting (dropout);
- the [Adam](https://arxiv.org/abs/1412.6980) optimizer.

Every brick was borrowed and already proven — a precise assembly of what lay within reach of the whole field, not a bolt from the blue.

One single move was radical. Rip out the slow machinery entirely — both recurrence (reading word by word) and convolutions. Convolutions are another way to process sequences, slow in their own right; they came from image recognition, and they'd been tried for text too. Rip out both at once — and keep attention alone. The [paper](https://arxiv.org/abs/1706.03762) declares it outright, in its very first sentence: the model is built *"dispensing with recurrence and convolutions entirely."* The daring was exactly this — throw out what everything had rested on for years, and test whether attention could hold the whole structure by itself.

The paper was called "Attention Is All You Need." And it turned out exactly right: beyond attention, nothing else is needed. They threw out recurrence, threw out convolutions, kept attention alone — and it carried the whole load. The title sounded like a cocky slogan, but it was a precise description.

## What opened the road: two findings that only worked as a pair

Two things opened the road together, and it matters not to confuse them. One was invented in 2014, the other in 2017, and they only started working as a pair.

- **Attention (2014).** The model learned to see the link between every word and every other word directly — no retelling through a cramped cell, no loss of meaning on a long sentence.
- **Dropping recurrence (2017).** While the model read text word by word, each step waited on the one before — the work ran in single file. Drop recurrence, and the queue vanishes: every word of the sentence can now be computed at once. And that's exactly what the graphics cards models are trained on do best: not one hard operation fast, but thousands of identical ones in parallel.

Attention gave the model sharp sight; dropping the queue gave it speed.

And then everything went wide. Once training splits into parallel work, you can **feed it ever more computation**: more graphics cards, more text, in the same time. And then a fact of almost indecent simplicity turned up: this predictably turns into quality. More scale — a smarter model, and not by luck but along a fairly smooth curve (later measured and written up in the "scaling laws" — the work of [Kaplan](https://arxiv.org/abs/2001.08361), then [Chinchilla](https://arxiv.org/abs/2203.15556)).

> Before, making a model smarter took a new bright idea. Now, much of the time, it was enough to add computation and data — and wait.

Down this very path came [BERT](https://arxiv.org/abs/1810.04805), then [GPT](https://arxiv.org/abs/2005.14165), and at the end — ChatGPT, which by now everyone has talked to.

And the numbers confirmed it right away, still on translation. The base transformer beat all the previous champions — including heavy composite systems, where several models' answers are averaged for an extra sliver of quality — at a small fraction of their cost. Training fit into 3.5 days on eight graphics cards; the previous champions cost several times, sometimes tens of times, more for the same quality. Best in class — and markedly cheaper. And that, not the high quality number alone, was the main signal: if the same result comes cheaper, then for the same money you can reach for something far bigger than translation.

> **For the curious: how it works under the hood.** The 2014 attention mechanism is "soft alignment": the context for the next word is assembled as a weighted sum over all the encoder's states. The transformer generalizes the same trick. For each word, three vectors are computed — Query, Key, and Value; the closeness of the query to the keys gives the weights, by which the values are averaged. The dot products are divided by √d (the square root of the dimension) — otherwise softmax drifts to where the gradients are nearly zero and training stalls. Attention is computed not with one "head" but with several in parallel (multi-head) — each looking at its own slice of connections. The price of every word's direct access to every other is quadratic complexity O(n²) in length: twice as long an input, four times the work. It's exactly this square that people would later find every way to get around.

## Twelve years later

The best proof of how big the shift was: its skeleton still holds the frontier, nine years on. In a field where everything goes stale in a couple of years and yesterday's breakthrough looks naive by tomorrow, that's rare.

What survived into our flagships out of each of the two papers:

- **from 2014** — the idea of attention itself. It's at the heart of every large model today, without a single exception. When ChatGPT "understands" what that "it" refers to in your long question, the same mechanism is at work — the one invented to translate German sentences.
- **from 2017** — Vaswani's specific design at the very core: every word's attention to every other, several parallel "heads" of attention at once, residual connections with normalization, the alternation of "attention → processing" blocks, and the very thought that word order has to be told to the model separately (since there's no queue anymore, it won't arise on its own).

Meanwhile the 2017 blueprint has been quietly rewritten in many places over these years:

- normalization was moved so training would go smoother — pre-norm ([Xiong, 2020](https://arxiv.org/abs/2002.04745));
- the way of telling the model position was swapped for a more flexible one — RoPE ([Su, 2021](https://arxiv.org/abs/2104.09864)), ALiBi ([Press, 2021](https://arxiv.org/abs/2108.12409));
- from the encoder-decoder pair, large language models moved to a single decoder (the GPT line);
- the O(n²) square was taught to be computed more cleverly, without materializing the whole matrix in memory — FlashAttention ([Dao, 2022](https://arxiv.org/abs/2205.14135));
- attention was thinned out for cheapness — GQA ([Ainslie, 2023](https://arxiv.org/abs/2305.13245));
- dense processing was replaced by a "mixture of experts," where only part of the model switches on for each word — MoE/Switch ([Fedus, 2021](https://arxiv.org/abs/2101.03961)).

The skeleton is 2017's; the flesh grown onto it is largely new.

The frontier today is still that same transformer with attention at its core. Every flagship (models on the level of GPT-5, Claude, Gemini, Llama 4, DeepSeek, Qwen) is a transformer refined around the edges; the upgrades run around the core, and the core holds. One caveat: the makers of the closed models never disclosed their architecture — so for GPT-5, Claude, and Gemini this is a strong inference from indirect signs, not a confirmed fact.

There was a serious challenge too. Architectures without attention — above all [**Mamba**](https://arxiv.org/abs/2312.00752) — have already gone into use, but only as hybrids in niches of long context (Jamba, [Nemotron-H](https://arxiv.org/abs/2504.03624), Granite 4.0): some of their layers still carry attention. Without it a model computes fast but "retrieves" poorly from a long text — it can't precisely copy a fact named ten pages back. Which is exactly what attention was invented for in 2014. So the throne, twelve years later, still belongs to that idea from Montreal.

## Happy AI Day

Out of a narrow task — translate a long sentence without losing the beginning — grew, over twelve years, systems that write code and hold a conversation.

And along the way a lesson about how technology moves shows through. We're used to looking for the big shift wherever something was loudly **added and given a ringing name**. But it's often the opposite — in someone deciding to **strip out what's extra and let the idea finally stretch**. Attention was invented in 2014; it fired only three years later, when the slow old engine was yanked out from under it. And spotting where the real turn was doesn't come at once — it comes years later, when a whole world has grown out of a small find, and you can see what it grew from.

So September 1 is a good day to wish artificial intelligence a happy birthday. It's twelve. Happy AI Day.
