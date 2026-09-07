<!-- Channel: LinkedIn (EN). Announce of Lecture 4 "AI Across the Software Development
     Lifecycle" — https://lessons.tellian.io/en/lectures/lec-04/
     Style canon: blueprint/channels/linkedin.md. Facts verified: research.md (this folder).
     This is the dev/SDLC post held back from the lessons.tellian.io course announce
     (that one deliberately used non-dev examples). Round 1: three hooks to choose from.
     L06 flag honored: NOT built on DORA-2024 throughput hit (reversed in DORA-2025). -->

# LinkedIn — лекция SDLC (lec-04). Три завлекалки, раунд 2 (цифры 2026)

Каждая: первая строка = хук-факт из проверенного исследования 2026 года (до сгиба) → второй
нетривиальный вывод → ссылка на лекцию → CTA без «if». Язык по канону — простой. Выбираем один.

> **L06:** раунд-1 хук на METR «19% медленнее» СГОРЕЛ — METR перезапустили в фев-2026 и получили
> обратное (~+18%, сами зовут «очень слабым доказательством»). Прошлогодний слоган больше не годится.
> Ниже — всё на данных 2026.

Мой голос: **A (Faros «Acceleration Whiplash»)** — самый крепкий: не опрос, а телеметрия по 22 000
разработчиков за 2 года; сам разворачивается в парадокс «выпускаем больше — ломаем больше».
**C (разворот METR)** — самый умный твист для профи. **B** — security-срез 2026.

---

## A — Faros 2026: «Acceleration Whiplash» (мой выбор)

Teams that went all-in on AI shipped 34% more code. Their review time went up 441%.

This is from Faros (2026), which tracked 22,000 developers over two years — real data from their tools, not a survey. More got shipped, but incidents per pull request rose 243%, and about a third of pull requests were merged with no review at all. The work didn't disappear. It moved — from writing code to reviewing and fixing it.

Where AI actually helps across the software lifecycle, and where it just moves the cost somewhere you're not looking — that's what my new lecture is about.

👉 https://lessons.tellian.io/en/lectures/lec-04/

When AI writes more of your code, what has to change in how you review it?

---

## B — Veracode 2026: умнее, но не безопаснее

A whole model generation later, AI still writes code with a security hole about 44% of the time.

Veracode ran the same test in 2025 and again in 2026. It barely moved — 45% then, 44% now. The newest, strongest model still ships a known vulnerability in roughly one task out of three. Better at writing code hasn't meant safer code.

When you can trust AI in your pipeline, and when a human has to stand behind it — that's what my new lecture works through, across the software lifecycle.

👉 https://lessons.tellian.io/en/lectures/lec-04/

What's the one thing you'd never merge from an AI without reading every line yourself?

---

## C — METR: два исследования, обратные ответы (умный твист)

Last year a study found experienced developers were 19% slower with AI. This year the same team re-ran it and got the opposite — an 18% speedup.

Both are from METR (2025 and 2026). And here's the honest part they wrote themselves: the new result is very weak evidence — the numbers barely hold. Two careful studies, opposite answers. If the people measuring this still can't say whether AI speeds developers up, then "it feels faster" tells you even less.

How to actually judge where AI helps across the software lifecycle — instead of trusting the feeling — is what my new lecture is about.

👉 https://lessons.tellian.io/en/lectures/lec-04/

How does your team tell whether AI actually helps — not just whether it feels faster?

---

## Факт-якоря 2026 (из research.md, секция «2026 refresh»)
- **Faros «Acceleration Whiplash» (апр-2026):** телеметрия, 22 000 devs / 4 000+ команд, 2 года.
  При высоком внедрении AI: throughput +34%, epics/dev +66%; но review time +441%, churn +861%,
  инциденты/PR +242.7%, 31.3% PR влиты без ревью. Vendor (Faros) — раскрыто именем в посте.
  https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways
- **Veracode 2026 (июль):** security pass 56% ⇒ ~44% задач c уязвимостью (2025: 55%/45% — почти флэт);
  лучшая модель (GPT-5.5) валит ~1 из 3. https://www.veracode.com/blog/2026-genai-code-security-report-ai-risk/
- **METR (фев-2026):** перезапуск → ~+18% (CI −38%…+9%), новички ~+4%; METR сами: «очень слабое
  доказательство». Разворот прошлогоднего −19%. https://metr.org/blog/2026-02-24-uplift-update/
- **JetBrains (авг-2026):** 90% профи используют AI-агентов еженедельно, 68% ежедневно (>15 000 devs).
  Якорь «AI — это дефолт». https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/
- ⚠️ Устарело (НЕ брать в хук): METR «19% медленнее» (перевёрнут); 2025 SO «66%» (рефреша нет);
  DORA-2024 throughput. 2026 DORA и 2026 SO survey ещё не вышли.
