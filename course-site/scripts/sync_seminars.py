#!/usr/bin/env python3
"""sync_seminars.py — генерит страницы семинаров курса-сайта из репозитория `lessons`.

Отличия от лекций (см. sync_lectures.py), из-за которых это отдельный скрипт:
- У семинаров НЕТ `speech.md`. Индекс истины — `deck.yaml` (в отличие от лекций он полон:
  у каждого слайда есть `id` + `file`), комментарий — «## Speaker notes» в `slides/*.md`.
- RU+EN (с AI-usage-lessons#205/#206): каждый семинар собирается на обоих языках, если
  для него есть `deck.en.yaml` — EN пропускается тихо (RU-first), как у лекций. EN-рендер
  PDF/PPTX именуется `sem-NN-en(.pdf|-preview.pdf)`, не `sem-NN.en.pdf` — не суффикс лекций.
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

SEMINARS = ["sem-01", "sem-02", "sem-03", "sem-04"]
LANGS = ["ru", "en"]
SEM_MANIFEST = L.DOCS / ".seminars-manifest.json"


def seminars_dir(lessons_lectures_dir: Path) -> Path:
    """COURSE_LESSONS_DIR указывает на library/lectures — семинары лежат рядом."""
    return lessons_lectures_dir.parent / "seminars"


# ── ЧТО НЕ ИДЁТ В ПАБЛИК ──────────────────────────────────────────────────────
# publish/publication-config.yaml: убираем универ-специфику (МГТУ/ИУ6/Бауманка, чат курса
# в MAX, рубежный контроль, посещаемость, оценивание). НО общий EXCLUDE_SECTION_RE лекций
# сюда не годится: он дропает всё, что похоже на «семинар N» — то есть обложку каждого
# семинара — и «домашнее задание», под которое у семинаров попадает содержательный разбор.
# Уже билингвальный (RU+EN термины) — работает без изменений для обоих языков.
SEM_EXCLUDE_RE = re.compile(
    r'чат\s+курса|course\s+chat|'
    r'посещаемост\w*|attendance|'
    r'рубежн\w*\s+контрол\w*|\bрк\s*[123]\b|midterm|'
    r'оценк\w*\s+за\s+семестр|semester\s+grade|grading|'
    r'карт[аы]\s+семестр|semester\s+map',
    re.I,
)

# Точечные исключения по id — там, где универ-специфика вшита в КАРТИНКУ и текстом её не снять.
# Ключ — id слайда, общий для RU/EN (одна и та же структура деков в обоих языках).
EXCLUDE_BY_ID = {
    "sem-01": {
        "s01": "обложка с «МГТУ им. Н.Э. Баумана» на самом слайде",
        "s03": "карта курса с метками РК1/РК2/РК3 (рубежный контроль)",
    },
    # sem-03 — с v2 (кейс-формат) исключений нет: скан всех 43 страниц по
    # «МГТУ / Бауман / ИУ6 / рубежный / посещаемость / чат курса» даёт ноль.
}

SEM_TITLE_PREFIX_RE = re.compile(r'^(Семинар|Seminar)\s*\d+\s*[.．:—–-]*\s*', re.I)


def deck_meta(sem_dir: Path, lang: str) -> dict:
    for p in L.deck_files(sem_dir, lang):
        try:
            data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError:
            continue
        if data.get("deck"):
            return data["deck"]
    return {}


def seminar_title(meta: dict, num, sem: str, lang: str) -> str:
    """Единый вид «Семинар N. Заголовок»/«Seminar N. Title» (в deck.title номер и разделитель
    бывают вписаны по-разному — em-dash, точка, «:»)."""
    loc = L.L10N.get(lang, L.L10N["ru"])
    word = loc["seminar"]
    raw = str(meta.get("title") or f"{word} {num or sem}").strip()
    core = SEM_TITLE_PREFIX_RE.sub('', raw).strip(' .—–-:')
    return f"{word} {num}. {core}" if num else (core or raw)


# Подписи-заглушки: в deck.yaml у структурных слайдов в assertion стоит их kind (id
# литерала — "closing"/"cover"/"map" — общий для RU/EN, стабы не переводятся; переводится
# только отображаемая подпись).
KIND_CAPTIONS = {
    "ru": {"closing": "Что унести", "cover": "Обложка", "map": "Карта занятия"},
    "en": {"closing": "Key takeaways", "cover": "Cover", "map": "Session map"},
}


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


def seminar_pdf(sem_dir: Path, sem: str, lang: str) -> Path:
    """Канонический рендер. RU: rendered/sem-NN(.pdf|-preview.pdf). EN: rendered/sem-NN-en
    (.pdf|-preview.pdf) — `-en` перед расширением, не суффикс `.en.` как у лекций (так
    заведено PR AI-usage-lessons#205). Кейс-формат (sem-03 v2) выкладывает только
    *-preview.pdf: канонический там удалён самой контент-сессией."""
    names = ((f"{sem}.pdf", f"{sem}-preview.pdf") if lang == "ru"
             else (f"{sem}-en.pdf", f"{sem}-en-preview.pdf"))
    for name in names:
        p = sem_dir / "rendered" / name
        if p.exists():
            return p
    raise FileNotFoundError(f"{sem}/{lang}: нет ни rendered/{names[0]}, ни rendered/{names[1]}")


def spec_file_for(sem_dir: Path, sem: str, lang: str) -> Path:
    """Doc-first кейс-формат (sem-03 v2): RU-спека и EN-спека — отдельные файлы
    (`spec_sem03.py` / `spec_sem03_en.py`), не языковой параметр внутри одной — так решил
    AI-usage-lessons#204 (RU остаётся source of truth, общая спека дала бы риск частичного
    применения правок при переводе)."""
    base = sem.replace('-', '')
    name = f"spec_{base}.py" if lang == "ru" else f"spec_{base}_en.py"
    return sem_dir.parents[2] / "tools" / "seminar-render" / name


def attach_spec_notes(sem_dir: Path, sem: str, slides: list[dict], lang: str) -> int:
    """Кейс-формат (doc-first, sem-03 v2): slides(-en)/*.md — стабы, а текст и speaker notes
    живут в tools/seminar-render/spec_<sem>[_en].py (список S, порядок 1:1 с deck.yaml).
    Дописываем заметки тем слайдам, у которых их нет. No-op для sem-01/02 (заметки в md)
    и вообще везде, где спеки нет."""
    spec_file = spec_file_for(sem_dir, sem, lang)
    if not spec_file.exists() or all(s["body"] for s in slides):
        return 0
    import importlib.util
    spec = importlib.util.spec_from_file_location(f"spec_{sem}_{lang}", spec_file)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as e:                       # спека — чужой код, падать из-за неё не хотим
        print(f"    ⚠ {sem}/{lang}: не смог прочитать {spec_file.name}: {e}")
        return 0
    entries = [e for e in (getattr(mod, "S", None) or []) if isinstance(e, dict)]
    deck = L.load_deck_entries(sem_dir, lang)
    if len(entries) != len(deck):
        print(f"    ⚠ {sem}/{lang}: в {spec_file.name} {len(entries)} слайдов, в deck {len(deck)} "
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
    caps = KIND_CAPTIONS.get(lang, KIND_CAPTIONS["ru"])
    n = 0
    for sl in slides:
        cap = sl["caption"].strip()                 # ключ by_caption — подпись ИЗ ДЕКА
        if not sl["body"] and by_caption.get(cap):
            sl["body"] = L.strip_stage_directions(by_caption[cap])
            n += 1
        # подпись вида «closing»/«cover»/«map» — это kind из дека (литерал, не переводится
        # в стабе), а не название слайда; переименовываем ПОСЛЕ поиска заметки, иначе ключ
        # перестанет совпадать
        if cap.lower() in caps:
            sl["caption"] = caps[cap.lower()]
    if n:
        print(f"    · {sem}/{lang}: заметок взято из {spec_file.name}: {n}")
    return n


def build_seminar(sem: str, sems_dir: Path, lang: str) -> dict | None:
    sem_dir = sems_dir / sem
    if lang != "ru" and not L.deck_files(sem_dir, lang):
        return None   # нет EN-исходников для этого семинара — тихо пропускаем (RU-first)

    pdf = seminar_pdf(sem_dir, sem, lang)

    slides = L.parse_deck_slides(sem_dir, lang, exclude_re=SEM_EXCLUDE_RE)
    attach_spec_notes(sem_dir, sem, slides, lang)
    # точечные исключения по id — снимаем ПОСЛЕ парсинга, сверяя по assertion/заголовку
    by_id = EXCLUDE_BY_ID.get(sem, {})
    if by_id:
        drop_caps = set()
        for e in L.load_deck_entries(sem_dir, lang):
            if e["id"] in by_id:
                f = sem_dir / e["file"]
                text = f.read_text(encoding="utf-8") if e["file"] and f.exists() else ""
                drop_caps.add(e["assertion"] or L.slide_title(text) or e["id"])
        before = len(slides)
        slides = [s for s in slides if s["caption"] not in drop_caps]
        for sid, why in by_id.items():
            print(f"    · {sem}/{lang}: {sid} не публикуется — {why}")
        assert before - len(slides) == len(by_id), \
            f"{sem}/{lang}: по id ожидалось снять {len(by_id)}, снято {before - len(slides)}"

    assets = L.DOCS / "assets" / lang / sem
    doc = pymupdf.open(pdf)
    footers = L.strip_footer_pagenums(doc)
    if footers:
        print(f"    · {sem}/{lang}: срезано футеров-пагинации: {footers}")
    page_map = L.build_page_map(doc, slides)
    moved = L.collapse_progressive_builds(doc, page_map)   # квиз-билд sem-01 → полный разбор
    if moved:
        print(f"    · {sem}/{lang}: прогрессивных шагов свёрнуто к последнему кадру: {moved}")
    L.render_mapped(doc, page_map, assets)
    doc.close()

    dropped = [slides[i]["caption"] for i, p in enumerate(page_map) if p is None]
    if dropped:
        print(f"    ⚠ {sem}/{lang}: без сопоставленного слайда (не публикуются): {dropped}")
    n = sum(1 for p in page_map if p is not None)

    meta = deck_meta(sem_dir, lang)
    num = meta.get("seminar_number") or re.sub(r'\D', '', sem).lstrip("0")
    title = seminar_title(meta, num, sem, lang)
    dur = meta.get("duration_min") or ""
    loc = L.L10N.get(lang, L.L10N["ru"])

    out = ["---", f"title: {L.yaml_q(title)}", "---", "", f"# {title}", ""]
    bits = [f"{loc['seminar']} {num}"] if num else []
    if dur:
        bits.append(f"~{dur} {loc['min']}")
    bits.append(f"{n} {loc['slides'](n)}")
    out += ["*" + " · ".join(str(b) for b in bits) + "*", ""]

    disp = 0
    for orig_i, sl in enumerate(slides):
        if page_map[orig_i] is None:
            continue
        disp += 1
        cap = sl["caption"] or f"{loc['slide']} {disp}"
        out.append(f"### {disp:02d} · {cap} {{#s-{disp:02d}}}")
        out.append("")
        alt = cap.replace("]", " ").replace("[", " ")
        img = f"../assets/{lang}/{sem}/page-{orig_i + 1:02d}.webp"
        out.append(f"[![{loc['slide']} {disp}. {alt}]({img}){{loading=lazy .slide-img}}]({img}){{.slide-link}}")
        out.append("")
        if sl["body"]:
            out += [sl["body"], ""]

    dest_dir = L.DOCS / "seminars"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{sem}.{lang}.md"
    dest.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
    print(f"  ✓ {sem}/{lang}: {n} слайдов → {dest.relative_to(L.SITE)}")
    return {"id": sem, "title": title, "num": num, "slides": n}


def build_all(sems: list[str], lessons_dir: Path) -> dict[str, list[dict]]:
    sems_dir = seminars_dir(lessons_dir)
    if not sems_dir.exists():
        raise SystemExit(f"Нет каталога семинаров: {sems_dir}")
    manifests: dict[str, list[dict]] = {lang: [] for lang in LANGS}
    for s in sems:
        for lang in LANGS:
            m = build_seminar(s, sems_dir, lang)
            if m:
                manifests[lang].append(m)
            elif lang != "ru":
                print(f"    · {s}: нет EN-исходников — EN пропущен (RU-first)")
    SEM_MANIFEST.write_text(json.dumps(manifests, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifests


def main() -> None:
    ap = argparse.ArgumentParser(description="Собрать страницы семинаров из lessons.")
    ap.add_argument("seminars", nargs="*", default=None, help="sem-01 sem-03 … (по умолчанию 01-04)")
    ap.add_argument("--lessons", default=os.environ.get("COURSE_LESSONS_DIR", str(L.DEFAULT_LESSONS)),
                    help="путь к library/lectures в репо lessons (семинары ищутся рядом)")
    args = ap.parse_args()
    manifests = build_all(args.seminars or SEMINARS, Path(args.lessons))
    ru, en = manifests["ru"], manifests["en"]
    print(f"\nГотово: {len(ru)} семинар(ов) RU + {len(en)} EN → docs/seminars/, манифест "
          f"{SEM_MANIFEST.relative_to(L.SITE)}")
    print("\n# nav-сниппет для mkdocs.yml:")
    print("  - Семинары:")
    for m in ru:
        print(f"      - seminars/{m['id']}.md")


if __name__ == "__main__":
    main()
