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

## Images

`en.md`/`ru.md` reference local chart/diagram files (`![alt](assets/foo.png)`). The publisher
**uploads each one to the WP media library** (idempotent — looks up an existing upload by
filename before re-uploading) and rewrites the markdown to the real `source_url` before
rendering, and sets the `<img>` tag's `width`/`height` from the actual local file's pixel size.
A relative path left as-is renders as a dead `src` on the live site — this isn't optional.

**Display size is capped at 840px regardless of the real file size or the column's CSS width.**
Jetpack Photon (the image CDN this site uses) resizes any inline content image to the theme's
`$content_width` (Twenty Sixteen hardcodes 840) — it reads that PHP global at render time, not
the tag's own width/height, and there's no REST-exposed setting for it (checked: no `content_width`
in `/wp/v2/settings`, no Photon-specific width override in `/jetpack/v4/settings` beyond the
on/off toggle). Fixing it for real means either a theme-level `$content_width` override (needs
file/code access this pipeline doesn't have) or disabling Photon site-wide (`jetpack/v4/settings`
→ `photon`) — a real site-wide tradeoff (loses Photon's CDN/optimization for every image on every
post), not something to flip without asking. As of 2026-11-08, left on; images render at ≤840px.

## Site layout (Twenty Sixteen) — widened article column, 2026-11-08

The theme's default single-post layout is narrower than it looks like it should be: `.entry-content`
only gets ~50% of the page (floated against `.entry-footer`'s byline column inside the same
`#primary`), on top of `.site-inner`'s own 1320px cap. Widened via Additional CSS (site-wide,
scoped to `body.single`): `.site-inner` to 1600px, `.content-area` to 80%, `.entry-content` to
100% of that (no longer float-paired with `.entry-footer`).

**The byline (avatar/date/categories/tags) now lives in the sidebar, not next to the article** —
moved there by a tiny `<script>` in a **Custom HTML widget** (`custom_html-2`, first in
`sidebar-1`, added via `POST /wp/v2/widgets` + reordered via `POST /wp/v2/sidebars/sidebar-1`),
which on `DOMContentLoaded` does `sidebar.insertBefore(entryFooter, sidebar.firstChild)` for
`body.single` pages. This was the fix that stuck, after two CSS-only attempts (`position:absolute`
with a fixed `top`/`padding-top` guess) both broke on real content — the absolute-positioned box
either overlapped the title or, once padded to align with the sidebar's own inset, wrapped the tag
list onto 6 lines and overflowed into the sidebar below it. Moving the real DOM node means it
inherits the sidebar's own widget spacing for free — no height guessing.
**If anyone ever rebuilds the sidebar widget list from scratch, re-add this widget first**, or the
byline reverts to its default spot next to the article.

## Gotchas

- A draft is created on the live site but isn't public — safe to preview, then delete if junk.
- If credentials rotate, just update `.env`.
- Fenced code **inside a blockquote** renders fine (engine handles it) — but it must be a real
  fenced block (```` ``` ````), not indented.
- No headless browser available in this environment to visually verify a layout change (Playwright
  is installed but its Chromium is missing system libs, no sudo to install them) — any CSS/layout
  change here is verified by the human in an actual browser, not by this pipeline.
