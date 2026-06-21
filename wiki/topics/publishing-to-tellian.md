# Publishing to tellian.io

How we ship a finished piece to the **tellian.io** blog. Built and verified 2026-06-21 — don't
re-derive it; run the pipeline.

## TL;DR

```bash
cp -r templates/piece-bilingual pieces/<slug>     # en.md + ru.md
# fill frontmatter + bodies
python3 scripts/wp_publish.py pieces/<slug>                 # → DRAFT (default)
python3 scripts/wp_publish.py pieces/<slug> --status publish  # → live (user gate first)
```

## How the site is set up

- **WordPress.com Atomic** (Business plan), site ID 244070662.
- Bilingual layout = **one** post, **pure CSS `:target`** switcher (not JS). The switcher line
  `English | Русский` links to `#en` / `#ru`; each language is a `div.lang-block`, English carries
  `default`. The show/hide rules live **once** in the site's Additional CSS (Appearance →
  Customize) — a post only carries the switcher line + the two `lang-block` divs.
- Tags/categories = native WP taxonomy. The publisher resolves them **by name** and **creates**
  any that don't exist — typos spawn stray terms, so watch spelling.

## Access

- Auth = **Application Password** over HTTP Basic — *not* OAuth (OAuth is only needed for
  `public-api.wordpress.com`; the Atomic site's own `tellian.io/wp-json` accepts app passwords).
- The app-password UI is hidden by the WordPress.com profile screen; create one at
  `tellian.io/wp-admin/profile.php` → Application Passwords, or
  `tellian.io/wp-admin/authorize-application.php?app_name=<name>`.
- Credentials live in `.env` at repo root (gitignored): `WP_API_BASE`, `WP_USER`, `WP_APP_PASSWORD`.
  `WP_USER` can be the account email.

## The publisher (`scripts/wp_publish.py`)

- Input: `pieces/<slug>/en.md` (+ post-level frontmatter: `title`, `slug`, `status`, `categories`,
  `tags`) and `ru.md` (just its `title`). Title is injected as the in-block `<h1>` — don't repeat it
  in the body.
- **Idempotent**: first publish writes `wp_post_id` back into `en.md`; re-runs **update** that post
  instead of creating a duplicate.
- **Default status = `draft`** (the ship gate). Going live requires explicit `--status publish` +
  the user's approval. `--dry-run` prints the assembled HTML without any API call.

## Markdown engine

Conversion uses **markdown-it-py** (CommonMark + GFM tables/strikethrough), not
python-markdown. Reason: python-markdown does **not** render a fenced code block nested
inside a blockquote (`> ` + ```` ``` ````) — it leaks the code as text and lets raw `<tag>`
escape into the HTML. markdown-it-py renders it as a proper `<pre><code>` with the contents
escaped. `html=False`, so any stray `<tag>` in prose is escaped; typography (curly quotes,
dashes) is left to WordPress's `wptexturize` on display.

## Gotchas

- A draft is created on the live site but isn't public — safe to preview, then delete if junk.
- If credentials rotate, just update `.env`.
- Fenced code **inside a blockquote** renders fine (engine handles it) — but it must be a real
  fenced block (```` ``` ````), not indented.
