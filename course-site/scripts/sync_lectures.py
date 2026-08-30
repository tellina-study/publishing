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
from PIL import Image

HERE = Path(__file__).resolve().parent
SITE = HERE.parent                       # course-site/
DOCS = SITE / "docs"

DEFAULT_LESSONS = Path(os.environ.get(
    "COURSE_LESSONS_DIR",
    "/home/harness/harness-projects/256/lessons-3bb49d40/library/lectures",
))
PROOF_LECTURES = ["lec-01", "lec-08", "lec-10", "lec-13"]  # по одному на диалект
ALL_LECTURES = [f"lec-{n:02d}" for n in range(1, 18) if n != 16]  # lec-01…17, нет lec-16
# published (publication-config: status=published) — чистые + двуязычные; 05..17 = draft (пауза)
PUBLISHED = ["lec-01", "lec-02", "lec-03", "lec-04"]
LANGS = ["ru", "en"]
DPI = 120
WEBP_QUALITY = 80  # WebP + lazy-load: ~−70% веса против PNG@132


# ─────────────────────────── speech.md парсинг ───────────────────────────

class GuardMismatch(Exception):
    """Число слайд-секций speech != числу страниц PDF — не мапим вслепую."""


HEADING = re.compile(r'^(#{1,6})\s+(.*\S)\s*$')

# Исключаемые секции (publication-config exclude_slides/exclude_inline): универ-специфика.
# Дропаем ЦЕЛИКОМ (и комментарий, и слайд): карта семестра, оценивание, посещаемость,
# рубежный контроль, домашки, семинары-мостики, чат курса в MAX. Telegram/email — оставляем.
EXCLUDE_SECTION_RE = re.compile(
    r'карт[аы]\s+семестр|semester\s+map|'
    r'оценк\w*\s+за\s+семестр|оцениван\w*|semester\s+grade|grading|'
    r'чат\s+курса|course\s+chat|\bв\s+max\b|'
    r'посещаемост\w*|attendance|'
    r'рубежн\w*\s+контрол\w*|\bрк\s*[123]\b|midterm|'
    r'домашн\w*\s+задани\w*|homework|'
    r'семинар\w*\s*(?:№|\d|мостик|bridge)|seminar\s*(?:\d|bridge)',
    re.I,
)

def is_excluded_section(title: str) -> bool:
    return bool(EXCLUDE_SECTION_RE.search(title))

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

def normalize_title(raw: str, num, lang: str = "ru") -> str:
    """Единый вид «Лекция N. Заголовок» / «Lecture N. Title»; чистка шума («речь лектора»)."""
    core = raw.strip()
    core = re.sub(r'^(Лекци[яю]|Lecture)\s*\d+\s*[.．:]\s*', '', core, flags=re.I)   # снять «Лекция N.»
    noise = r'(речь\s+лектора|lecturer.?s?\s+(?:speech|script|talk))'
    core = re.sub(r'\s*[—–-]\s*' + noise + r'\s*\.?\s*$', '', core, flags=re.I)      # хвост
    core = re.sub(r'^' + noise + r'\s*[.—–-]*\s*', '', core, flags=re.I)             # начало
    core = re.sub(noise + r'\s*\.?\s*', '', core, flags=re.I)                        # остатки
    core = core.strip(' .—–-:')
    prefix = "Лекция" if lang == "ru" else "Lecture"
    return f"{prefix} {num}. {core}" if num else core


def yaml_q(s: str) -> str:
    """Безопасно закавычить строку для YAML (двоеточия в заголовке ломали frontmatter)."""
    return '"' + str(s).replace('\\', '\\\\').replace('"', '\\"') + '"'


def strip_stage_directions(body: str) -> str:
    """Убрать сценические ремарки в [квадратных скобках] (для лектора, не для читателя):
    «[На слайде— …]», «[Backup-фраза …]», «[I turn on the laptop …]».
    Сохраняем: [N]-цитаты (только цифры) и markdown-ссылки [text](url)."""
    # скобки с буквой внутри, НЕ являющиеся началом markdown-ссылки (нет '(' сразу после)
    body = re.sub(r'\[[^\]]*[A-Za-zА-Яа-яЁё][^\]]*\](?!\()', '', body)
    body = re.sub(r'[ \t]+\n', '\n', body)          # хвостовые пробелы
    body = re.sub(r'\n{3,}', '\n\n', body)          # схлопнуть пустые абзацы
    return body.strip()


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
        if is_excluded_section(title):        # универ-специфика — дропаем целиком
            continue
        # конец тела: следующий заголовок с уровнем <= level
        body_end = len(lines)
        for (nline_i, nlevel, _) in heads[h + 1:]:
            if nlevel <= level:
                body_end = nline_i
                break
        body = strip_stage_directions("\n".join(lines[line_i + 1:body_end]))
        slides.append({"caption": slide_caption(title), "body": body})
    return slides, fm


# ─────────────────────────── рендер PDF → PNG ───────────────────────────

def render_pdf(pdf: Path, out_dir: Path, dpi: int = DPI, force: bool = False) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(pdf)
    n = doc.page_count
    # пропуск: если webp уже отрисованы в нужном количестве — не перерисовываем
    existing = sorted(out_dir.glob("page-*.webp"))
    if not force and len(existing) == n and not list(out_dir.glob("page-*.png")):
        doc.close()
        return n
    for f in list(out_dir.glob("page-*.png")) + list(out_dir.glob("page-*.webp")):
        f.unlink()
    for k in range(n):
        pix = doc.load_page(k).get_pixmap(dpi=dpi)
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        img.save(out_dir / f"page-{k + 1:02d}.webp", "WEBP",
                 quality=WEBP_QUALITY, method=6)
    doc.close()
    return n


# ────────────── content-based маппинг: страница PDF ↔ секция speech ──────────────
# Порядок страниц PDF не всегда == порядку секций speech (вставленные/переставленные
# слайды — напр. бауманские в lec-01). Сопоставляем по СОДЕРЖИМОМУ: заголовок секции
# ищем в тексте страницы. Глобальное жадное 1:1 + позиционная подсказка. Страницы без
# пары (лишние слайды) отбрасываются, секции без пары — без картинки (флагуем).

_STOP = set("и в на что как не с по за из от до или а но the of a an to in on for and or is are".split())

def _norm_txt(s: str) -> str:
    return re.sub(r'[^0-9a-zа-яё]+', ' ', str(s).lower()).strip()

def _title_tokens(title: str) -> list[str]:
    return [w for w in _norm_txt(title).split() if len(w) >= 3 and w not in _STOP]

def _score(title_toks: list[str], page_text: str) -> float:
    if not title_toks:
        return 0.0
    return sum(1 for w in title_toks if w in page_text) / len(title_toks)

def build_page_map(doc, slides: list[dict], gap: float = -0.12) -> list:
    """section_idx → pdf_page_idx (или None) через УПОРЯДОЧЕННОЕ выравнивание (DP, как diff).
    Обе последовательности (секции speech и реальные слайды PDF) идут в порядке лекции;
    вставленные лишние страницы (бауманские) пропускаются как 'insertions', пропущенные
    слайды — как 'deletions'. Диагональ (позиционная) выигрывает на чистых лекциях —
    обложки/Q&A/дивайдеры с малым текстом остаются на месте."""
    S = len(slides)
    P = doc.page_count
    page_texts = [_norm_txt(doc.load_page(k).get_text()) for k in range(P)]
    toks = [_title_tokens(s["caption"]) for s in slides]

    dp = [[0.0] * (P + 1) for _ in range(S + 1)]
    bt = [[""] * (P + 1) for _ in range(S + 1)]
    for j in range(1, P + 1):
        dp[0][j] = dp[0][j - 1] + gap; bt[0][j] = "P"     # пропуск страницы
    for i in range(1, S + 1):
        dp[i][0] = dp[i - 1][0] + gap; bt[i][0] = "S"     # пропуск секции
    for i in range(1, S + 1):
        for j in range(1, P + 1):
            m = dp[i - 1][j - 1] + _score(toks[i - 1], page_texts[j - 1])
            sp = dp[i][j - 1] + gap
            ss = dp[i - 1][j] + gap
            best = max(m, sp, ss)
            dp[i][j] = best
            bt[i][j] = "M" if best == m else ("P" if best == sp else "S")

    sec2page = [None] * S
    i, j = S, P
    while i > 0 or j > 0:
        move = bt[i][j] if (i and j) else ("S" if i > 0 else "P")
        if move == "M":
            sec2page[i - 1] = j - 1; i -= 1; j -= 1
        elif move == "P":
            j -= 1
        else:
            i -= 1

    # RESCUE: локальные перестановки слайдов в PDF монотонный DP роняет. Досопоставляем
    # секции-без-пары пропущенным страницам по содержимому. Бауманские страницы (совпадают
    # с exclude-паттерном) в кандидаты НЕ берём — их дропаем намеренно.
    used = {p for p in sec2page if p is not None}
    free = [k for k in range(P) if k not in used and not EXCLUDE_SECTION_RE.search(page_texts[k])]
    for i in range(S):
        if sec2page[i] is not None:
            continue
        best, best_sc = None, 0.34
        for k in free:
            sc = _score(toks[i], page_texts[k])
            if sc > best_sc:
                best_sc, best = sc, k
        if best is not None:
            sec2page[i] = best
            free.remove(best)
    return sec2page

def render_mapped(doc, page_map: list, out_dir: Path, dpi: int = DPI) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for f in list(out_dir.glob("page-*.png")) + list(out_dir.glob("page-*.webp")):
        f.unlink()
    for i, k in enumerate(page_map, 1):
        if k is None:
            continue
        pix = doc.load_page(k).get_pixmap(dpi=dpi)
        Image.frombytes("RGB", (pix.width, pix.height), pix.samples).save(
            out_dir / f"page-{i:02d}.webp", "WEBP", quality=WEBP_QUALITY, method=6)


# ─────────────────────────── сборка страницы ───────────────────────────

# подписи интерфейса генератора по языкам
L10N = {
    "ru": {"lecture": "Лекция", "slides": lambda n: plural_slides(n), "slide": "Слайд", "min": "мин"},
    "en": {"lecture": "Lecture", "slides": lambda n: "slides", "slide": "Slide", "min": "min"},
}

def lecture_files(lec_dir: Path, lec: str, lang: str):
    """RU→EN маппинг файлов (publication-config naming). Footer-less pub-дек RU — если есть."""
    if lang == "en":
        speech = lec_dir / "speech.en.md"
        pdf = lec_dir / "rendered" / f"{lec}-en.pdf"
    else:
        speech = lec_dir / "speech.md"
        pub = lec_dir / "rendered" / f"{lec}-pub.pdf"   # footer-less RU pub, если появится
        pdf = pub if pub.exists() else lec_dir / "rendered" / f"{lec}.pdf"
    return speech, pdf


def build_lecture(lec: str, lessons_dir: Path, lang: str = "ru") -> None:
    lec_dir = lessons_dir / lec
    speech, pdf = lecture_files(lec_dir, lec, lang)
    if not pdf.exists():
        raise FileNotFoundError(f"{lec}/{lang}: нет {pdf}")
    if not speech.exists():
        raise FileNotFoundError(f"{lec}/{lang}: нет {speech}")
    loc = L10N.get(lang, L10N["ru"])

    slides, fm = parse_speech(speech)
    assets = DOCS / "assets" / lang / lec

    # CONTENT-MAPPING: сопоставляем каждую секцию speech её странице PDF по СОДЕРЖИМОМУ
    # (порядок страниц PDF ≠ порядку секций из-за вставленных/переставленных слайдов).
    doc = pymupdf.open(pdf)
    page_map = build_page_map(doc, slides)      # section_idx → pdf_page_idx | None
    render_mapped(doc, page_map, assets)        # webp только для сопоставленных, по исходному индексу
    doc.close()
    dropped = [slides[i]["caption"] for i, p in enumerate(page_map) if p is None]
    if dropped:
        print(f"    ⚠ {lec}/{lang}: без сопоставленного слайда (не публикуются): {dropped}")
    n_pages = sum(1 for p in page_map if p is not None)

    # frontmatter-схемы разнятся по лекциям: title|lecture_title, lecture|lecture_number
    num = fm.get("lecture") or fm.get("lecture_number") or ""
    raw = str(fm.get("title") or fm.get("lecture_title") or f"{loc['lecture']} {lec}")
    title = normalize_title(raw, num, lang)
    dur = fm.get("length_min") or fm.get("duration_min") or ""

    out = ["---", f"title: {yaml_q(title)}", "---", "", f"# {title}", ""]
    meta = []
    if num:
        meta.append(f"{loc['lecture']} {num}")
    if dur:
        meta.append(f"~{dur} {loc['min']}")
    meta.append(f"{n_pages} {loc['slides'](n_pages)}")
    if meta:
        out.append("*" + " · ".join(str(m) for m in meta) + "*")
        out.append("")

    disp = 0
    for orig_i, sl in enumerate(slides):
        if page_map[orig_i] is None:
            continue                        # нет слайда → секцию не публикуем (нет висячих комментов)
        disp += 1
        anchor = f"s-{disp:02d}"
        cap = sl["caption"] or f"{loc['slide']} {disp}"
        # последовательный номер в подзаголовке → правый TOC как нумерованный список
        out.append(f"### {disp:02d} · {cap} {{#{anchor}}}")
        out.append("")
        # webp назван по ИСХОДНОМУ индексу секции (как в render_mapped)
        alt = cap.replace("]", " ").replace("[", " ")
        img = f"../assets/{lang}/{lec}/page-{orig_i + 1:02d}.webp"
        out.append(f"[![{loc['slide']} {disp}. {alt}]({img}){{loading=lazy .slide-img}}]({img}){{.slide-link}}")
        out.append("")
        if sl["body"]:
            out.append(sl["body"])
            out.append("")

    lectures_dir = DOCS / "lectures"
    lectures_dir.mkdir(parents=True, exist_ok=True)
    dest = lectures_dir / f"{lec}.{lang}.md"
    dest.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(f"  ✓ {lec}: {n_pages} слайдов → {dest.relative_to(SITE)}")
    return {"id": lec, "title": str(title), "num": num, "slides": n_pages, "lang": lang}


HERO = {
    "ru": """---
title: Использование ИИ в различных индустриях
---

# Использование ИИ в различных индустриях

Открытый курс о том, как **ИИ работает в реальных отраслях** — где помогает, где нет, и как это
понять. Каждая лекция — это слайды и разбор к ним: смотришь слайд, читаешь, что за ним стоит.

## Лекции

<div class="grid cards" markdown>
""",
    "en": """---
title: AI Across Industries
---

# AI Across Industries

An open course on how **AI works in real-world industries** — where it helps, where it doesn't, and
how to tell. Each lecture is slides plus commentary: look at a slide, read what's behind it.

## Lectures

<div class="grid cards" markdown>
""",
}

def write_landing(manifest: list[dict], lang: str = "ru") -> None:
    """Генерит лендинг-витрину из манифеста лекций (по языку)."""
    loc = L10N.get(lang, L10N["ru"])
    open_label = "Открыть →" if lang == "ru" else "Open →"
    cards = []
    for m in sorted(manifest, key=lambda x: x["id"]):
        t = str(m["title"])
        body = re.sub(r'^(Лекци[яю]|Lecture)\s*\d+[.\s—-]*', '', t, flags=re.I).strip() or t
        num_prefix = f"{loc['lecture']} {m['num']}. " if m["num"] else ""
        cards.append(
            f"-   **{num_prefix}{esc(body)}**\n\n"
            f"    ---\n\n"
            f"    {m['slides']} {loc['slides'](m['slides'])}\n\n"
            f"    [{open_label}](lectures/{m['id']}.md)\n"
        )
    text = HERO.get(lang, HERO["ru"]) + "\n".join(cards) + "\n</div>\n"
    (DOCS / f"index.{lang}.md").write_text(text, encoding="utf-8")
    print(f"  ✓ лендинг ({lang}): {len(manifest)} карточек → docs/index.{lang}.md")

def html_num(num) -> str:
    return f"Лекция {num}. " if num else ""

def plural_slides(n: int) -> str:
    n = int(n)
    if 11 <= n % 100 <= 14:
        return "слайдов"
    d = n % 10
    return "слайд" if d == 1 else ("слайда" if 2 <= d <= 4 else "слайдов")

def esc(s: str) -> str:
    return s.replace("[", "").replace("]", "")

def print_nav(manifest: list[dict]) -> None:
    print("\n# nav-сниппет для mkdocs.yml:")
    print("  - Лекции:")
    for m in sorted(manifest, key=lambda x: x["id"]):
        print(f"      - lectures/{m['id']}.md")


def main() -> None:
    ap = argparse.ArgumentParser(description="Собрать страницы курса из lessons.")
    ap.add_argument("lectures", nargs="*", default=None,
                    help="lec-01 lec-08 … (по умолчанию — все 16 лекций)")
    ap.add_argument("--proof", action="store_true",
                    help="только 4 proof-лекции (по одному диалекту)")
    ap.add_argument("--all", action="store_true",
                    help="все 16 лекций (иначе — только published 01-04)")
    ap.add_argument("--no-landing", action="store_true",
                    help="не перегенерировать лендинг")
    ap.add_argument("--lessons", default=str(DEFAULT_LESSONS),
                    help="путь к library/lectures в репо lessons")
    args = ap.parse_args()

    lessons_dir = Path(args.lessons)
    if not lessons_dir.exists():
        raise SystemExit(f"Нет каталога lessons: {lessons_dir}")
    if args.lectures:
        lectures = args.lectures
    elif args.proof:
        lectures = PROOF_LECTURES
    elif args.all:
        lectures = ALL_LECTURES
    else:
        lectures = PUBLISHED

    print(f"lessons: {lessons_dir}")
    manifests = {lang: [] for lang in LANGS}
    skipped = []
    for lec in lectures:
        for lang in LANGS:
            # язык собираем только если есть язык-специфичные исходники
            speech, pdf = lecture_files(lessons_dir / lec, lec, lang)
            if not speech.exists() or not pdf.exists():
                if lang == "en":
                    continue  # нет EN — тихо пропускаем (RU-first)
            try:
                manifests[lang].append(build_lecture(lec, lessons_dir, lang))
            except GuardMismatch as e:
                print(f"  ✗ ПРОПУСК {lec}/{lang}: {e}")
                skipped.append(str(e))
    ru_manifest = manifests["ru"]
    if not args.no_landing:
        for lang in LANGS:
            if manifests[lang]:
                write_landing(manifests[lang], lang)
    print(f"\nГотово: {len(ru_manifest)} лекц. (RU) + EN где есть, {len(skipped)} пропущено.")
    for s in skipped:
        print(f"  ✗ {s}")
    print_nav(ru_manifest)


if __name__ == "__main__":
    main()
