#!/usr/bin/env python3
"""sync_lectures.py — генерит страницы курса-сайта из репозитория `lessons`.

Ключевые решения (см. tasks/20260830_course-site-launch/):
- ИНДЕКС ИСТИНЫ — speech.md: его слайд-секции 1:1 соответствуют страницам PDF
  (перепроверено на всех 16 лекциях). deck.yaml НЕ индекс (неполон/отсутствует).
- Парсер знает 4 ДИАЛЕКТА разметки заголовков слайдов:
    A `## [sNN · X мин] — Title`   (H2)   — lec-01,02,03,04,05,06,14,15,17
    B `### [sNN · X мин]`          (H3)   — lec-07,08,12
    C `### [Слайд N — Title] · dur`(H3)   — lec-09,10,11   (без sNN-id)
    D `## sNN — Title · dur`       (H2)   — lec-13         (без скобок)
- WHITELIST: берём ТОЛЬКО слайд-секции. Инструкторские вставки
  («Подготовка…», «Если пойдёт не так», «## Раздел N») НЕ попадают в паблик.
- GUARD: #слайд-секций == #страниц PDF, иначе падаем громко с именем лекции.
- Рендер PDF→PNG через PyMuPDF (без системного poppler).
- language-aware: пишет docs/lectures/lec-NN.<lang>.md (suffix-структура i18n).

Usage:
    python3 scripts/sync_lectures.py [lec-01 lec-08 ...]   # по умолчанию — 4 proof-лекции
    COURSE_LESSONS_DIR=/path/to/lessons/library/lectures python3 scripts/sync_lectures.py
"""
from __future__ import annotations
import os
import re
import sys
import argparse
from pathlib import Path

import yaml
import pymupdf

HERE = Path(__file__).resolve().parent
SITE = HERE.parent                       # course-site/
DOCS = SITE / "docs"

DEFAULT_LESSONS = Path(os.environ.get(
    "COURSE_LESSONS_DIR",
    "/home/harness/harness-projects/256/lessons-3bb49d40/library/lectures",
))
PROOF_LECTURES = ["lec-01", "lec-08", "lec-10", "lec-13"]  # по одному на диалект
DPI = 132


# ─────────────────────────── speech.md парсинг ───────────────────────────

HEADING = re.compile(r'^(#{1,6})\s+(.*\S)\s*$')

def is_slide_heading(title: str) -> bool:
    """4 диалекта. Инструкторские секции («Раздел N», «Подготовка…») → False."""
    t = title.strip()
    if re.match(r'^\[s\d', t):          # A / B: [sNN …]
        return True
    if re.match(r'^\[Слайд\s+\d', t):   # C: [Слайд N …]
        return True
    if re.match(r'^s\d+\b', t):         # D: sNN — …
        return True
    return False

def slide_caption(title: str) -> str:
    """Человеческая подпись слайда для подзаголовка/навигации."""
    t = title.strip()
    # C: [Слайд 1 — Title] · dur  → Title
    m = re.match(r'^\[Слайд\s+\d+\s*[—–-]\s*(.*?)\]', t)
    if m:
        return m.group(1).strip()
    # A/B: [sNN · dur] — Title      → Title
    m = re.match(r'^\[s\d[^\]]*\]\s*[—–-]\s*(.*)$', t)
    if m:
        return m.group(1).strip()
    # A/B без тире после скобки: [sNN · dur]  → снять скобки
    m = re.match(r'^\[s\d[^\]]*\]\s*(.*)$', t)
    if m and m.group(1).strip():
        return m.group(1).strip()
    # D: sNN — Title · dur          → Title (без хвоста · dur)
    m = re.match(r'^s\d+\s*[—–-]\s*(.*)$', t)
    if m:
        return re.sub(r'\s*·.*$', '', m.group(1)).strip()
    return re.sub(r'^\[|\]$', '', t)

def parse_frontmatter(text: str) -> dict:
    if text.startswith('---'):
        end = text.find('\n---', 3)
        if end != -1:
            try:
                return yaml.safe_load(text[3:end]) or {}
            except yaml.YAMLError:
                return {}
    return {}

def parse_speech(path: Path) -> tuple[list[dict], dict]:
    """Возвращает (слайды по порядку, frontmatter). Каждый слайд:
    {caption, body_md}. Тело — до следующего заголовка уровня <= текущего."""
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    lines = text.splitlines()

    # все заголовки: (idx_строки, уровень, заголовок)
    heads = []
    for i, line in enumerate(lines):
        m = HEADING.match(line)
        if m:
            heads.append((i, len(m.group(1)), m.group(2)))

    slides = []
    for h, (line_i, level, title) in enumerate(heads):
        if not is_slide_heading(title):
            continue
        # конец тела: следующий заголовок с уровнем <= level
        body_end = len(lines)
        for (nline_i, nlevel, _) in heads[h + 1:]:
            if nlevel <= level:
                body_end = nline_i
                break
        body = "\n".join(lines[line_i + 1:body_end]).strip()
        slides.append({"caption": slide_caption(title), "body": body})
    return slides, fm


# ─────────────────────────── рендер PDF → PNG ───────────────────────────

def render_pdf(pdf: Path, out_dir: Path, dpi: int = DPI) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    for f in out_dir.glob("page-*.png"):
        f.unlink()
    doc = pymupdf.open(pdf)
    n = doc.page_count
    for k in range(n):
        pix = doc.load_page(k).get_pixmap(dpi=dpi)
        pix.save(out_dir / f"page-{k + 1:02d}.png")
    doc.close()
    return n


# ─────────────────────────── сборка страницы ───────────────────────────

def build_lecture(lec: str, lessons_dir: Path, lang: str = "ru") -> None:
    lec_dir = lessons_dir / lec
    pdf = lec_dir / "rendered" / f"{lec}.pdf"
    speech = lec_dir / "speech.md"
    if not pdf.exists():
        raise FileNotFoundError(f"{lec}: нет {pdf}")
    if not speech.exists():
        raise FileNotFoundError(f"{lec}: нет {speech}")

    slides, fm = parse_speech(speech)
    assets = DOCS / "assets" / lang / lec
    n_pages = render_pdf(pdf, assets)

    # GUARD: индекс истины — speech; должен совпасть со страницами PDF
    if len(slides) != n_pages:
        raise SystemExit(
            f"[GUARD] {lec}: слайд-секций speech={len(slides)} != страниц PDF={n_pages}. "
            f"Разметка speech.md не покрывает все страницы — проверь диалект/пропуски."
        )

    title = fm.get("title", f"Лекция {lec}")
    num = fm.get("lecture", "")
    dur = fm.get("length_min", "")
    lang = fm.get("language", lang)

    out = [f"---", f"title: {title}", "---", "", f"# {title}", ""]
    meta = []
    if num:
        meta.append(f"Лекция {num}")
    if dur:
        meta.append(f"~{dur} мин")
    meta.append(f"{n_pages} слайдов")
    if meta:
        out.append("*" + " · ".join(str(m) for m in meta) + "*")
        out.append("")

    for i, sl in enumerate(slides, 1):
        anchor = f"s-{i:02d}"
        cap = sl["caption"] or f"Слайд {i}"
        out.append(f"### {cap} {{#{anchor}}}")
        out.append("")
        out.append(f"![Слайд {i}](../assets/{lang}/{lec}/page-{i:02d}.png)")
        out.append("")
        if sl["body"]:
            out.append(sl["body"])
            out.append("")

    lectures_dir = DOCS / "lectures"
    lectures_dir.mkdir(parents=True, exist_ok=True)
    dest = lectures_dir / f"{lec}.{lang}.md"
    dest.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(f"  ✓ {lec}: {n_pages} слайдов → {dest.relative_to(SITE)}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Собрать страницы курса из lessons.")
    ap.add_argument("lectures", nargs="*", default=None,
                    help="lec-01 lec-08 … (по умолчанию — 4 proof-лекции)")
    ap.add_argument("--lessons", default=str(DEFAULT_LESSONS),
                    help="путь к library/lectures в репо lessons")
    args = ap.parse_args()

    lessons_dir = Path(args.lessons)
    if not lessons_dir.exists():
        raise SystemExit(f"Нет каталога lessons: {lessons_dir}")
    lectures = args.lectures or PROOF_LECTURES

    print(f"lessons: {lessons_dir}")
    for lec in lectures:
        build_lecture(lec, lessons_dir)
    print(f"Готово: {len(lectures)} лекц.")


if __name__ == "__main__":
    main()
