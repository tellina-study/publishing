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
    # sem-03 — с v2 (кейс-формат) исключений нет: скан всех 43 страниц по
    # «МГТУ / Бауман / ИУ6 / рубежный / посещаемость / чат курса» даёт ноль.
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


# Подписи-заглушки: в deck.yaml у структурных слайдов в assertion стоит их kind.
KIND_CAPTIONS = {"closing": "Что унести", "cover": "Обложка", "map": "Карта занятия"}


def compose_closing(entry: dict) -> str:
    """Финальный слайд кейс-формата: notes нет, содержание — takeaways + bridge."""
    parts = []
    tk = entry.get("takeaways")
    if isinstance(tk, (list, tuple)):
        parts += [f"- {t}" for t in tk]
    elif tk:
        parts.append(str(tk))
    if entry.get("bridge"):
        parts += ["", str(entry["bridge"])]
    return "\n".join(parts).strip()


def seminar_pdf(sem_dir: Path, sem: str) -> Path:
    """Канонический рендер — rendered/sem-NN.pdf. Кейс-формат (sem-03 v2) выкладывает
    только rendered/sem-NN-preview.pdf: канонический там удалён самой контент-сессией."""
    for name in (f"{sem}.pdf", f"{sem}-preview.pdf"):
        p = sem_dir / "rendered" / name
        if p.exists():
            return p
    raise FileNotFoundError(f"{sem}: нет ни rendered/{sem}.pdf, ни rendered/{sem}-preview.pdf")


def attach_spec_notes(sem_dir: Path, sem: str, slides: list[dict]) -> int:
    """Кейс-формат (doc-first, sem-03 v2): slides/*.md — стабы, а текст и speaker notes
    живут в tools/seminar-render/spec_<sem>.py (список S, порядок 1:1 с deck.yaml).
    Дописываем заметки тем слайдам, у которых их нет. No-op для sem-01/02 (заметки в md)
    и вообще везде, где спека нет."""
    spec_file = sem_dir.parents[2] / "tools" / "seminar-render" / f"spec_{sem.replace('-', '')}.py"
    if not spec_file.exists() or all(s["body"] for s in slides):
        return 0
    import importlib.util
    spec = importlib.util.spec_from_file_location(f"spec_{sem}", spec_file)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as e:                       # спека — чужой код, падать из-за неё не хотим
        print(f"    ⚠ {sem}: не смог прочитать {spec_file.name}: {e}")
        return 0
    entries = [e for e in (getattr(mod, "S", None) or []) if isinstance(e, dict)]
    deck = L.load_deck_entries(sem_dir, LANG)
    if len(entries) != len(deck):
        print(f"    ⚠ {sem}: в {spec_file.name} {len(entries)} слайдов, в deck.yaml {len(deck)} "
              f"— заметки не привязываю (порядок не гарантирован)")
        return 0
    # Порядок спека 1:1 с deck.yaml, поэтому ключ — подпись слайда из дека, а не title
    # спека: у слайдов «Кейс N.N · Разбор» они расходятся. `slides` уже отфильтрованы
    # по exclude, так что по индексу их сопоставлять нельзя — только по подписи.
    by_caption = {}
    for e, d in zip(entries, deck):
        cap = (d["assertion"] or str(e.get("title") or "")).strip()
        if cap and e.get("notes"):
            by_caption.setdefault(cap, str(e["notes"]).strip())
    # У финального слайда notes нет — его содержание лежит в takeaways/bridge.
    by_caption.update({
        (d["assertion"] or "").strip(): compose_closing(e)
        for e, d in zip(entries, deck)
        if not e.get("notes") and compose_closing(e)
    })
    n = 0
    for sl in slides:
        cap = sl["caption"].strip()                 # ключ by_caption — подпись ИЗ ДЕКА
        if not sl["body"] and by_caption.get(cap):
            sl["body"] = L.strip_stage_directions(by_caption[cap])
            n += 1
        # подпись вида «closing»/«cover» — это kind из дека, а не название слайда;
        # переименовываем ПОСЛЕ поиска заметки, иначе ключ перестанет совпадать
        if cap.lower() in KIND_CAPTIONS:
            sl["caption"] = KIND_CAPTIONS[cap.lower()]
    if n:
        print(f"    · {sem}: заметок взято из {spec_file.name}: {n}")
    return n


def build_seminar(sem: str, sems_dir: Path) -> dict:
    sem_dir = sems_dir / sem
    pdf = seminar_pdf(sem_dir, sem)

    slides = L.parse_deck_slides(sem_dir, LANG, exclude_re=SEM_EXCLUDE_RE)
    attach_spec_notes(sem_dir, sem, slides)
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
