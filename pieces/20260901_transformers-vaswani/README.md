# Bilingual piece → tellian.io

A piece is a folder with two files: `en.md` and `ru.md`. The publisher merges them
into **one** WordPress post with the CSS `:target` language switcher (`#en` / `#ru`),
exactly like existing tellian.io posts.

## New piece

```bash
cp -r templates/piece-bilingual pieces/<slug>
# edit pieces/<slug>/en.md  (title, slug, categories, tags, body)
# edit pieces/<slug>/ru.md  (title, body)
```

## Frontmatter

- **`en.md`** is canonical for post-level metadata:
  `title` (English — becomes the WP post title *and* the in-block `<h1>`),
  `slug`, `status` (`draft`/`publish`), `categories` (by name), `tags` (by name).
  `wp_post_id` is written back automatically after the first publish.
- **`ru.md`** carries only its own `title` (Russian, becomes the RU block `<h1>`).
- Categories/tags are matched by name on tellian.io and **created if missing** —
  watch for typos, a misspelling makes a new term.
- Do **not** put the title as `# H1` in the body; the publisher injects it.

## Publish

```bash
python3 scripts/wp_publish.py pieces/<slug>                 # creates a DRAFT (safe default)
python3 scripts/wp_publish.py pieces/<slug> --dry-run       # print HTML, no API calls
python3 scripts/wp_publish.py pieces/<slug> --status publish  # go live (explicit gate)
```

Re-running **updates** the same post (idempotent via `wp_post_id`), never duplicates.
First run prints the edit + preview links — open the preview to eyeball the switcher.

## Auth

Reads `.env` at the repo root (gitignored):

```
WP_API_BASE=https://tellian.io/wp-json/wp/v2
WP_USER=<wp login or email>
WP_APP_PASSWORD=<Application Password from tellian.io/wp-admin/profile.php>
```

The show/hide CSS for `.lang-block` already lives once in the site's Additional CSS
(Appearance → Customize), so the publisher only emits the per-post HTML.
