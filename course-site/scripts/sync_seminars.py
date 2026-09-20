#!/usr/bin/env python3
"""sync_seminars.py — генерит страницы семинаров курса-сайта из репозитория `lessons`.

Отличия от лекций (см. sync_lectures.py), из-за которых это отдельный скрипт:
- У семинаров НЕТ `speech.md`. Индекс истины — `deck.yaml` (в отличие от лекций он полон:
  у каждого слайда есть `id` + `file`), комментарий — «## Speaker notes» в `slides/*.md`.
- Только RU. EN-перевода семинаров нет; i18n (`fallback_to_default: true`) отдаст RU-страницу
  на английской версии сайта, поэтому битых ссылок это не создаёт.
- `facilitator-guide.md` в паблик НЕ идёт: он про то, как вести занятие (тайминги, бюджет
  обсуждения, fallback-cuts), а не про содержание.

Всё тяжёлое (парсинг слайдов, content-based маппинг комментарий↔страница PDF, рендер webp,
срез футеров) переиспользуется из sync_lectures.py — здесь только семинар-специфика.

Usage:
    python3 scripts/sync_seminars.py [sem-01 sem-03 …]
    COURSE_LESSONS_DIR=/path/to/lessons/library/lectures python3 scripts/sync_seminars.py

Порядок в деплое: сначала этот скрипт (он пишет манифест), потом sync_lectures.py —
лендинг собирает sync_lectures.py и подхватывает манифест семинаров, если он есть.
"""
from __future__ import annotations
import argparse
import json
import os
import re
from pathlib import Path

import pymupdf
import yaml

import sync_lectures as L

SEMINARS = ["sem-01", "sem-02", "sem-03"]
LANG = "ru"
SEM_MANIFEST = L.DOCS / ".seminars-manifest.json"


def seminars_dir(lessons_lectures_dir: Path) -> Path:
    """COURSE_LESSONS_DIR указывает на library/lectures — семинары лежат рядом."""
    return lessons_lectures_dir.parent / "seminars"


# ── ЧТО НЕ ИДЁТ В ПАБЛИК ──────────────────────────────────────────────────────
# publish/publication-config.yaml: убираем универ-специфику (МГТУ/ИУ6/Бауманка, чат курса
# в MAX, рубежный контроль, посещаемость, оценивание). НО общий EXCLUDE_SECTION_RE лекций
# сюда не годится: он дропает всё, что похоже на «семинар N» — то есть обложку каждого
# семинара — и «домашнее задание», под которое у семинаров попадает содержательный разбор.
SEM_EXCLUDE_RE = re.compile(
    r'чат\s+курса|course\s+chat|'
    r'посещаемост\w*|attendance|'
    r'рубежн\w*\s+контрол\w*|\bрк\s*[123]\b|midterm|'
    r'оценк\w*\s+за\s+семестр|semester\s+grade|grading|'
    r'карт[аы]\s+семестр|semester\s+map',
    re.I,
)

# Точечные исключения по id — там, где универ-специфика вшита в КАРТИНКУ и текстом её не снять.
EXCLUDE_BY_ID = {
    "sem-01": {
        "s01": "обложка с «МГТУ им. Н.Э. Баумана» на самом слайде",
        "s03": "карта курса с метками РК1/РК2/РК3 (рубежный контроль)",
    },
    "sem-03": {
        "s01": "обложка с «МГТУ им. Н.Э. Баумана» на самом слайде",
    },
}


def deck_meta(sem_dir: Path) -> dict:
    for p in L.deck_files(sem_dir, LANG):
        try:
            data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError:
            continue
        if data.get("deck"):
            return data["deck"]
    return {}


def seminar_title(meta: dict, num, sem: str) -> str:
    """Единый вид «Семинар N. Заголовок» (в deck.title номер бывает вписан по-разному)."""
    raw = str(meta.get("title") or f"Семинар {num or sem}").strip()
    core = re.sub(r'^Семинар\s*\d+\s*[.．:—–-]*\s*', '', raw, flags=re.I).strip(' .—–-:')
    return f"Семинар {num}. {core}" if num else (core or raw)


def build_seminar(sem: str, sems_dir: Path) -> dict:
    sem_dir = sems_dir / sem
    pdf = sem_dir / "rendered" / f"{sem}.pdf"
    if not pdf.exists():
        raise FileNotFoundError(f"{sem}: нет {pdf}")

    slides = L.parse_deck_slides(sem_dir, LANG, exclude_re=SEM_EXCLUDE_RE)
    # точечные исключения по id — снимаем ПОСЛЕ парсинга, сверяя по assertion/заголовку
    by_id = EXCLUDE_BY_ID.get(sem, {})
    if by_id:
        drop_caps = set()
        for e in L.load_deck_entries(sem_dir, LANG):
            if e["id"] in by_id:
                f = sem_dir / e["file"]
                text = f.read_text(encoding="utf-8") if e["file"] and f.exists() else ""
                drop_caps.add(e["assertion"] or L.slide_title(text) or e["id"])
        before = len(slides)
        slides = [s for s in slides if s["caption"] not in drop_caps]
        for sid, why in by_id.items():
            print(f"    · {sem}: {sid} не публикуется — {why}")
        assert before - len(slides) == len(by_id), \
            f"{sem}: по id ожидалось снять {len(by_id)}, снято {before - len(slides)}"

    assets = L.DOCS / "assets" / LANG / sem
    doc = pymupdf.open(pdf)
    footers = L.strip_footer_pagenums(doc)
    if footers:
        print(f"    · {sem}: срезано футеров-пагинации: {footers}")
    page_map = L.build_page_map(doc, slides)
    moved = L.collapse_progressive_builds(doc, page_map)   # квиз-билд sem-01 → полный разбор
    if moved:
        print(f"    · {sem}: прогрессивных шагов свёрнуто к последнему кадру: {moved}")
    L.render_mapped(doc, page_map, assets)
    doc.close()

    dropped = [slides[i]["caption"] for i, p in enumerate(page_map) if p is None]
    if dropped:
        print(f"    ⚠ {sem}: без сопоставленного слайда (не публикуются): {dropped}")
    n = sum(1 for p in page_map if p is not None)

    meta = deck_meta(sem_dir)
    num = meta.get("seminar_number") or re.sub(r'\D', '', sem).lstrip("0")
    title = seminar_title(meta, num, sem)
    dur = meta.get("duration_min") or ""

    out = ["---", f"title: {L.yaml_q(title)}", "---", "", f"# {title}", ""]
    bits = [f"Семинар {num}"] if num else []
    if dur:
        bits.append(f"~{dur} мин")
    bits.append(f"{n} {L.plural_slides(n)}")
    out += ["*" + " · ".join(str(b) for b in bits) + "*", ""]

    disp = 0
    for orig_i, sl in enumerate(slides):
        if page_map[orig_i] is None:
            continue
        disp += 1
        cap = sl["caption"] or f"Слайд {disp}"
        out.append(f"### {disp:02d} · {cap} {{#s-{disp:02d}}}")
        out.append("")
        alt = cap.replace("]", " ").replace("[", " ")
        img = f"../assets/{LANG}/{sem}/page-{orig_i + 1:02d}.webp"
        out.append(f"[![Слайд {disp}. {alt}]({img}){{loading=lazy .slide-img}}]({img}){{.slide-link}}")
        out.append("")
        if sl["body"]:
            out += [sl["body"], ""]

    dest_dir = L.DOCS / "seminars"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{sem}.{LANG}.md"
    dest.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(f"  ✓ {sem}: {n} слайдов → {dest.relative_to(L.SITE)}")
    return {"id": sem, "title": title, "num": num, "slides": n}


def build_all(sems: list[str], lessons_dir: Path) -> list[dict]:
    sems_dir = seminars_dir(lessons_dir)
    if not sems_dir.exists():
        raise SystemExit(f"Нет каталога семинаров: {sems_dir}")
    manifest = [build_seminar(s, sems_dir) for s in sems]
    SEM_MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest


def main() -> None:
    ap = argparse.ArgumentParser(description="Собрать страницы семинаров из lessons.")
    ap.add_argument("seminars", nargs="*", default=None, help="sem-01 sem-03 … (по умолчанию 01-03)")
    ap.add_argument("--lessons", default=os.environ.get("COURSE_LESSONS_DIR", str(L.DEFAULT_LESSONS)),
                    help="путь к library/lectures в репо lessons (семинары ищутся рядом)")
    args = ap.parse_args()
    manifest = build_all(args.seminars or SEMINARS, Path(args.lessons))
    print(f"\nГотово: {len(manifest)} семинар(ов) → docs/seminars/, манифест "
          f"{SEM_MANIFEST.relative_to(L.SITE)}")
    print("\n# nav-сниппет для mkdocs.yml:")
    print("  - Семинары:")
    for m in manifest:
        print(f"      - seminars/{m['id']}.md")


if __name__ == "__main__":
    main()
