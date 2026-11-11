#!/usr/bin/env python3
"""Publish a bilingual (EN/RU) piece to the tellian.io WordPress.com blog.

Reads two markdown files — en.md and ru.md — from a piece folder, converts each
to HTML, wraps them in the site's CSS `:target` language-switcher template
(switcher line + <div id="en" …default> + <div id="ru" …>), and creates or
updates a single WordPress post via the REST API.

The show/hide CSS for `.lang-block` lives once in the site's Additional CSS, so
this script only emits the per-post HTML structure.

Metadata comes from YAML frontmatter:
  en.md  (canonical post-level meta):
    title:       English title  (also the WP post title + in-block <h1>)
    slug:        post slug
    status:      draft | publish        (CLI --status overrides)
    categories:  [Name, ...]            (resolved/created by name)
    tags:        [Name, ...]            (resolved/created by name)
    wp_post_id:  <filled in after first publish — enables idempotent updates>
  ru.md:
    title:       Russian title  (in-block <h1>)

Images: any `![alt](assets/<file>)` in either body is uploaded to the WP media
library and the reference is rewritten to the returned URL. Uploads are idempotent
via assets/.wp_media.json, which maps filename -> {id, url, sha256}: a file whose
bytes are unchanged is never re-uploaded. WordPress has no REST route to replace a
media item's binary, so an edited image uploads as a NEW item and the map is
re-pointed — the old attachment stays in the library until you delete it there.

Auth: WordPress Application Password via HTTP Basic, from .env at repo root:
    WP_API_BASE=https://tellian.io/wp-json/wp/v2
    WP_USER=...
    WP_APP_PASSWORD=...

Usage:
    python3 scripts/wp_publish.py pieces/<slug>           # status from frontmatter (default draft)
    python3 scripts/wp_publish.py pieces/<slug> --status publish
    python3 scripts/wp_publish.py pieces/<slug> --dry-run # print HTML, no API calls
"""
from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import re
import sys
from pathlib import Path

import requests
import yaml
from markdown_it import MarkdownIt

REPO_ROOT = Path(__file__).resolve().parent.parent
SEPARATOR = '<hr class="wp-block-separator" />'
ASSET_RE = re.compile(r"!\[([^\]]*)\]\((assets/[^)\s]+)\)")
MEDIA_MAP = ".wp_media.json"

# CommonMark engine + GFM tables/strikethrough. CommonMark-compliant, so it renders
# fenced code blocks nested inside blockquotes correctly (python-markdown does not).
# html=False escapes any stray `<tag>` in prose; typography is left to WP's wptexturize.
MD = MarkdownIt("commonmark", {"html": False}).enable(["table", "strikethrough"])


def load_env() -> dict[str, str]:
    """Minimal .env parser — no external dependency."""
    env_path = REPO_ROOT / ".env"
    if not env_path.exists():
        sys.exit(f"ERROR: {env_path} not found. Create it with WP_API_BASE/WP_USER/WP_APP_PASSWORD.")
    env: dict[str, str] = {}
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        env[key.strip()] = val.strip()
    for required in ("WP_API_BASE", "WP_USER", "WP_APP_PASSWORD"):
        if not env.get(required):
            sys.exit(f"ERROR: {required} missing from .env")
    return env


def parse_frontmatter(path: Path) -> tuple[dict, str]:
    """Split a markdown file into (frontmatter dict, body)."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    meta = yaml.safe_load(parts[1]) or {}
    return meta, parts[2].lstrip("\n")


def md_to_html(body: str) -> str:
    return MD.render(body)


def build_content(en_title: str, en_html: str, ru_title: str, ru_html: str) -> str:
    """Assemble the language-switcher HTML exactly like existing tellian.io posts."""
    return "\n".join([
        '<p><a href="#en">English</a> | <a href="#ru">Русский</a></p>',
        SEPARATOR,
        '<div id="en" class="wp-block-group lang-block default">',
        f"<h1>{en_title}</h1>",
        en_html,
        "</div>",
        SEPARATOR,
        '<div id="ru" class="wp-block-group lang-block">',
        f"<h1>{ru_title}</h1>",
        ru_html,
        "</div>",
    ])


class WP:
    def __init__(self, env: dict[str, str]):
        self.base = env["WP_API_BASE"].rstrip("/")
        self.session = requests.Session()
        self.session.auth = (env["WP_USER"], env["WP_APP_PASSWORD"])
        self.session.headers["User-Agent"] = "tellian-publisher/1.0"

    def _term_id(self, taxonomy: str, name: str) -> int:
        """Resolve a category/tag name to an ID, creating the term if missing."""
        r = self.session.get(f"{self.base}/{taxonomy}", params={"search": name, "per_page": 100})
        r.raise_for_status()
        for term in r.json():
            if term["name"].strip().lower() == name.strip().lower():
                return term["id"]
        r = self.session.post(f"{self.base}/{taxonomy}", json={"name": name})
        r.raise_for_status()
        return r.json()["id"]

    def resolve_terms(self, taxonomy: str, names: list[str]) -> list[int]:
        return [self._term_id(taxonomy, n) for n in names]

    def upload_media(self, path: Path, alt: str = "") -> dict:
        """Upload one file to the media library; return its WP media object."""
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        r = self.session.post(
            f"{self.base}/media",
            data=path.read_bytes(),
            headers={"Content-Type": mime,
                     "Content-Disposition": f'attachment; filename="{path.name}"'},
        )
        r.raise_for_status()
        media = r.json()
        if alt:
            self.session.post(f"{self.base}/media/{media['id']}", json={"alt_text": alt})
        return media

    def upsert_post(self, payload: dict, post_id: int | None) -> dict:
        if post_id:
            r = self.session.post(f"{self.base}/posts/{post_id}", json=payload)
        else:
            r = self.session.post(f"{self.base}/posts", json=payload)
        r.raise_for_status()
        return r.json()


def collect_assets(bodies: list[str]) -> dict[str, str]:
    """Every assets/ image referenced by the bodies -> its first alt text."""
    found: dict[str, str] = {}
    for body in bodies:
        for alt, rel in ASSET_RE.findall(body):
            found.setdefault(rel, alt)
    return found


def sync_media(wp: "WP", piece: Path, assets: dict[str, str]) -> dict[str, str]:
    """Upload any new or changed asset; return {relative path -> media URL}.

    Idempotent via assets/.wp_media.json keyed on the file's sha256, so re-running
    the publisher re-uploads nothing. A changed file becomes a new attachment —
    the REST API cannot replace a media item's bytes in place.
    """
    map_path = piece / "assets" / MEDIA_MAP
    known = json.loads(map_path.read_text(encoding="utf-8")) if map_path.exists() else {}
    urls: dict[str, str] = {}

    for rel, alt in sorted(assets.items()):
        local = piece / rel
        if not local.exists():
            sys.exit(f"ERROR: {local} is referenced but missing")
        digest = hashlib.sha256(local.read_bytes()).hexdigest()
        entry = known.get(rel)
        if entry and entry.get("sha256") == digest:
            urls[rel] = entry["url"]
            print(f"  media unchanged: {rel} -> {entry['url']}")
            continue
        media = wp.upload_media(local, alt)
        known[rel] = {"id": media["id"], "url": media["source_url"], "sha256": digest}
        urls[rel] = media["source_url"]
        print(f"  media uploaded:  {rel} -> {media['source_url']}")

    if known:
        map_path.parent.mkdir(parents=True, exist_ok=True)
        map_path.write_text(json.dumps(known, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return urls


def rewrite_assets(body: str, urls: dict[str, str]) -> str:
    """Point every assets/ image reference at its uploaded media URL."""
    return ASSET_RE.sub(lambda m: f"![{m.group(1)}]({urls.get(m.group(2), m.group(2))})", body)


def write_back_post_id(en_path: Path, meta: dict, post_id: int) -> None:
    """Persist wp_post_id into en.md frontmatter so re-runs update instead of duplicate."""
    meta = dict(meta)
    meta["wp_post_id"] = post_id
    _, body = parse_frontmatter(en_path)
    fm = yaml.safe_dump(meta, allow_unicode=True, sort_keys=False).strip()
    en_path.write_text(f"---\n{fm}\n---\n\n{body}", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description="Publish a bilingual piece to tellian.io")
    ap.add_argument("piece_dir", help="folder containing en.md and ru.md")
    ap.add_argument("--status", choices=["draft", "publish"], help="override frontmatter status")
    ap.add_argument("--dry-run", action="store_true", help="print assembled HTML, make no API calls")
    args = ap.parse_args()

    piece = Path(args.piece_dir)
    en_path, ru_path = piece / "en.md", piece / "ru.md"
    for p in (en_path, ru_path):
        if not p.exists():
            sys.exit(f"ERROR: {p} not found")

    en_meta, en_body = parse_frontmatter(en_path)
    ru_meta, ru_body = parse_frontmatter(ru_path)

    en_title = en_meta.get("title") or sys.exit("ERROR: en.md frontmatter needs `title`")
    ru_title = ru_meta.get("title") or en_title
    slug = en_meta.get("slug") or piece.name
    status = args.status or en_meta.get("status", "draft")

    assets = collect_assets([en_body, ru_body])

    if args.dry_run:
        print(f"# title:  {en_title}\n# slug:   {slug}\n# status: {status}")
        print(f"# categories: {en_meta.get('categories', [])}\n# tags: {en_meta.get('tags', [])}")
        print(f"# assets ({len(assets)}, not uploaded on a dry run): {sorted(assets)}")
        print("# ---- content ----")
        print(build_content(en_title, md_to_html(en_body), ru_title, md_to_html(ru_body)))
        return

    env = load_env()
    wp = WP(env)

    if assets:
        print(f"Syncing {len(assets)} asset(s):")
        urls = sync_media(wp, piece, assets)
        en_body, ru_body = rewrite_assets(en_body, urls), rewrite_assets(ru_body, urls)

    content = build_content(en_title, md_to_html(en_body), ru_title, md_to_html(ru_body))

    payload = {"title": en_title, "slug": slug, "status": status, "content": content}
    if en_meta.get("categories"):
        payload["categories"] = wp.resolve_terms("categories", en_meta["categories"])
    if en_meta.get("tags"):
        payload["tags"] = wp.resolve_terms("tags", en_meta["tags"])

    post_id = en_meta.get("wp_post_id")
    result = wp.upsert_post(payload, post_id)

    if not post_id:
        write_back_post_id(en_path, en_meta, result["id"])

    action = "Updated" if post_id else "Created"
    print(f"{action} post {result['id']} [{result['status']}]")
    print(f"  view:  {result.get('link')}")
    print(f"  edit:  https://tellian.io/wp-admin/post.php?post={result['id']}&action=edit")


if __name__ == "__main__":
    main()
