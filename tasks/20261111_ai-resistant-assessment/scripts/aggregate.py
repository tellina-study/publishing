#!/usr/bin/env python3
"""Aggregate the 138-run AI-resistant-assessment matrix into chart-ready JSON.

Single metric everywhere: ITEM-LEVEL valid accuracy = sum(valid_correct)/sum(valid_max).
Every group carries its denominators (runs, items) so no number ships without a base.

Source: materials/source/all_experiments_matrix.csv  (138 rows)
Out:    data/chart_data.json
"""
import csv, json
from pathlib import Path

TASK = Path(__file__).resolve().parent.parent
ROWS = list(csv.DictReader((TASK / "materials/source/all_experiments_matrix.csv").open(encoding="utf-8")))


def agg(pred):
    sel = [r for r in ROWS if pred(r)]
    items = sum(int(r["valid_max"]) for r in sel)
    correct = sum(int(r["valid_correct"]) for r in sel)
    return {
        "runs": len(sel),
        "items": items,
        "correct": correct,
        "accuracy": round(100 * correct / items, 1) if items else None,
        "per_run": [f'{r["valid_correct"]}/{r["valid_max"]}' for r in sel],
    }


def cond(*names):
    return lambda r: r["condition"] in names


# ---------------------------------------------------------------- 1. defense ladder
# Ordered as the piece tells it: formulation-level first (useless), channel-level last (works).
LADDER = [
    ("clean", "Любая формулировка на чистом тексте (11 раундов эскалации)",
     lambda r: r["category"] == "semantic_clean" and "sonnet" in r["model"]),
    ("unicode_file", "Гомоглифы и нулевой пробел в файле",
     lambda r: r["track"] == "unicode_file_obfuscation"),
    ("bidi", "Переворот цифр невидимым Bidi (RLO/LRI)",
     lambda r: r["track"] == "mechanical_M1"),
    ("tags", "Невидимые Unicode-теги и селекторы вариаций",
     lambda r: r["track"] in ("hidden_instruction_file", "mechanical_M3")
               or r["condition"] in ("tags", "P01", "P02")),
    ("multiscript", "Мультискриптовый коктейль (черокезский, коптский, матсимволы)",
     lambda r: r["track"] in ("mechanical_M2", "mechanical_M4")),
    ("stand_decoy", "Развязка с лабораторным стендом + симметричные дистракторы",
     lambda r: r["track"] == "symmetric_5q_stand842" and r["category"] == "external_stand_decoy"),
    ("css_zero", "Нулевой шрифт на чистом CSS (0 px разницы на экране)",
     lambda r: r["track"] == "pure_css_fontzero_m11"),
    ("param_swap", "Подмена параметров в буфере обмена (DOM-свап)",
     lambda r: r["track"] == "mechanical_M5"),
]

# ---------------------------------------------------------------- 2. rounds
ROUND_ORDER = ["v1", "v2", "v3", "v4", "R1", "R2", "R3", "R4", "R5",
               "R6", "R7", "R8", "R9", "R10", "R11"]
ROUND_LABEL = {
    "v1": "Пилот v1", "v2": "Пилот v2", "v3": "Пилот v3", "v4": "Пилот v4",
    "R1": "Р1 · 10 семейств", "R2": "Р2 · гибриды", "R3": "Р3 · распознать оговорку",
    "R4": "Р4 · действие+обоснование", "R5": "Р5 · навигация по курсу",
    "R6": "Р6 · иерархия инструкций", "R7": "Р7 · инверсия правил курса",
    "R8": "Р8 · 6 шагов перезаписи + стенд", "R9": "Р9 · обобщённая архитектура",
    "R10": "Р10 · механические искажения", "R11": "Р11 · нулевой шрифт CSS",
}

# ---------------------------------------------------------------- 3. ten families (Round 1 A01–A10)
FAMILIES = [
    ("A01", "Контрфактические вариации параметра"),
    ("A02", "Ловушки поверхностного вывода (идемпотентность, ретраи)"),
    ("A03", "Новые синтетические микромиры"),
    ("A04", "Синтез нескольких концепций"),
    ("A05", "Минимальные пары"),
    ("A06", "Выбор диагностического эксперимента"),
    ("A07", "Истинные, но нерелевантные посылки"),
    ("A08", "Критерий зависит от цели"),
    ("A09", "Границы того, что доказано"),
    ("A10", "Конкурирующие правдоподобные компромиссы"),
]

# ---------------------------------------------------------------- 4. control pairs
PAIRS = [
    ("Карточка стенда есть у ИИ", "Студент копирует только текст задания",
     lambda r: r["track"] == "symmetric_5q_stand842" and r["category"] == "control_with_stand",
     lambda r: r["track"] == "symmetric_5q_stand842" and r["category"] == "external_stand_decoy"),
    ("Артефакт стенда приложен", "Доступен только публичный сайт курса",
     lambda r: r["track"] == "vector_V2" and r["condition"] == "with_bench_artifact",
     lambda r: r["track"] == "vector_V2" and r["condition"] == "public_course_only"),
    ("Те же 5 заданий, искажения M1 и M3", "Те же 5 заданий, подмена параметров M5",
     lambda r: r["track"] in ("mechanical_M1", "mechanical_M3"),
     lambda r: r["track"] == "mechanical_M5"),
]

# ------------------------------------------- 4b. decoupling from a local artifact
# The finding that matters most: accuracy collapses with the text left completely
# untouched. The student copies honestly; the decisive parameters live on their own
# lab stand, and option A reproduces the canonical numbers from the PUBLIC course
# page — exactly where a web-enabled model goes looking.
DECOUPLING = [
    ("Пять симметричных заданий\n(решающее — вне курса)", "untouched",
     lambda r: r["track"] == "symmetric_5q_stand842" and r["category"] == "control_with_stand",
     lambda r: r["track"] == "symmetric_5q_stand842" and r["category"] == "external_stand_decoy"),
    ("Три задания, вектор V2", "untouched",
     lambda r: r["track"] == "vector_V2" and r["condition"] == "with_bench_artifact",
     lambda r: r["track"] == "vector_V2" and r["condition"] == "public_course_only"),
    ("Три задания, вектор V3\n(дистрактор несимметричный)", "untouched",
     lambda r: r["track"] == "vector_V3" and r["condition"] == "with_png_file",
     lambda r: r["track"] == "vector_V3" and r["condition"] == "text_copy_no_image"),
    ("Те же пять заданий,\nвставленных в чат", "swapped",
     lambda r: r["track"] in ("mechanical_M1", "mechanical_M3"),
     lambda r: r["track"] == "mechanical_M5"),
]

# Raw answer letters for vector_V2 — the mechanism visible without any aggregation.
# `A` on items 1 and 2 is the planted distractor: the canonical course-site numbers.
ANSWER_GRID = {
    "items": ["Задание 1", "Задание 2", "Задание 3"],
    "key": ["B", "C", "B"],
    "planted": "A",
    "rows": [
        {"label": "Параметры варианта приложены", "sub": "контроль", "answers": ["B", "C", "B"]},
        {"label": "Есть только опубликованный курс", "sub": "прогон 1", "answers": ["A", "A", "A"]},
        {"label": "Есть только опубликованный курс", "sub": "прогон 2", "answers": ["A", "A", "B"]},
    ],
}

# ---------------------------------------------------------------- 5. cross-model, Q1 cascade
# Hand-entered from cross_model_evidence.md / full_results.md §3 (verbatim model outputs).
# n = 1 observation per model. NOT a benchmark.
# Targeted probe, straight from cross_model_evidence.md. Two open engineering items
# from the structural-interference families, one run per model, scored on the
# 2-criterion rubric (2 points each, 4 total). Six observations in all.
#   Q1  — cascade + repeat judge calls. Key: 236 LLM calls.
#   Q16 — verification of a calculation module, manual formula review forbidden.
PROBE = {
    "item": "Q16 · верификация расчётного модуля, ручная проверка формул запрещена",
    "max_points": 2,
    "bars": [
        {"label": "Claude Sonnet 5.5", "points": 2,
         "detail": "независимая спецификация, граничные, оракул, мутационные тесты — и блокировка релиза"},
        {"label": "GPT-6.1 Sol", "points": 1,
         "detail": "оракул, граничные, property-based, мутационные, автоматические гейты — без блокировки релиза"},
        {"label": "Gemini 3 Flash", "points": 1,
         "detail": "property-based, мутационные, golden-master, граничные — без блокировки релиза"},
    ],
}

# Raw Q1 answers, with the provenance of each kept straight: Sol and Flash were run
# on the ORIGINAL wording (where Sonnet answered correctly); the 252 is Sonnet on the
# later wording that adds the cost-optimisation policy.
Q1 = {
    "intended_answer": 236,
    "defect": "условие недоспецифицировано: распределение 32 запросов между двумя группами отказа не задано",
    "models": [
        {"model": "Claude Sonnet 5.5", "variant": "исходная формулировка", "answer": 236,
         "failure": ""},
        {"model": "Claude Sonnet 5.5", "variant": "добавлен «регламент №402»", "answer": 252,
         "failure": "переоптимизировал вызовы судьи"},
        {"model": "GPT-6.1 Sol", "variant": "исходная формулировка", "answer": 136,
         "failure": "потерял этап генерации"},
        {"model": "Gemini 3 Flash", "variant": "исходная формулировка", "answer": 244,
         "failure": "20 отклонённых превратились в 24"},
    ],
}

out = {
    "meta": {
        "source": "workain/research-results @ 2026-11_ai-resistant-assessment/all_experiments_matrix.csv",
        "total_rows": len(ROWS),
        "metric": "item-level valid accuracy = sum(valid_correct)/sum(valid_max)",
        "models_in_matrix": {m: sum(1 for r in ROWS if r["model"] == m)
                             for m in sorted({r["model"] for r in ROWS})},
    },
    "totals": agg(lambda r: True),
    "by_category": {c: agg(lambda r, c=c: r["category"] == c)
                    for c in sorted({r["category"] for r in ROWS})},
    "ladder": [{"key": k, "label": lbl, **agg(p)} for k, lbl, p in LADDER],
    "rounds": [{"round": rd, "label": ROUND_LABEL[rd], **agg(lambda r, rd=rd: r["round"] == rd)}
               for rd in ROUND_ORDER],
    "clean_by_round": [{"round": rd, "label": ROUND_LABEL[rd],
                        **agg(lambda r, rd=rd: r["round"] == rd and r["category"] == "semantic_clean"
                              and "sonnet" in r["model"])}
                       for rd in ROUND_ORDER],
    "families": [{"id": fid, "label": lbl,
                  **agg(lambda r, fid=fid: r["track"] == f"family_{fid}")}
                 for fid, lbl in FAMILIES],
    "control_pairs": [{"control_label": cl, "treatment_label": tl,
                       "control": agg(cp), "treatment": agg(tp)}
                      for cl, tl, cp, tp in PAIRS],
    "run_lanes": [
        {"lane": "Формулировка на чистом тексте",
         "runs": [float(r["valid_accuracy_pct"]) for r in ROWS if r["category"] == "semantic_clean"]},
        {"lane": "Невидимые символы и мультискрипт",
         "runs": [float(r["valid_accuracy_pct"]) for r in ROWS
                  if r["category"] in ("mechanical_file", "mechanical_inline")
                  and r["track"] != "mechanical_M5" and r["condition"] != "P03"]},
        {"lane": "Приём в формулировке: дистрактор из курса",
         "runs": [float(r["valid_accuracy_pct"]) for r in ROWS
                  if r["category"] in ("external_stand_decoy", "control_with_stand")]},
        {"lane": "Подмена того, что доходит до ИИ",
         "runs": [float(r["valid_accuracy_pct"]) for r in ROWS
                  if r["category"] == "dom_clipboard_swap" or r["track"] == "mechanical_M5"
                  or r["condition"] == "P03"]},
    ],
    "run_distribution": [
        {"band": "100%", "runs": sum(1 for r in ROWS if float(r["valid_accuracy_pct"]) == 100)},
        {"band": "80–99%", "runs": sum(1 for r in ROWS if 80 <= float(r["valid_accuracy_pct"]) < 100)},
        {"band": "50–79%", "runs": sum(1 for r in ROWS if 50 <= float(r["valid_accuracy_pct"]) < 80)},
        {"band": "20–49%", "runs": sum(1 for r in ROWS if 20 <= float(r["valid_accuracy_pct"]) < 50)},
        {"band": "0–19%", "runs": sum(1 for r in ROWS if float(r["valid_accuracy_pct"]) < 20)},
    ],
    "decoupling": [{"label": lbl, "kind": kind, "control": agg(cp), "treatment": agg(tp)}
                   for lbl, kind, cp, tp in DECOUPLING],
    "answer_grid": ANSWER_GRID,
    "cross_model_probe": PROBE,
    "q1_cross_model": Q1,
}

(TASK / "data").mkdir(exist_ok=True)
(TASK / "data/chart_data.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

# ---- console report ---------------------------------------------------------
print(f"rows={out['meta']['total_rows']}  models={out['meta']['models_in_matrix']}")
print(f"TOTAL: {out['totals']['correct']}/{out['totals']['items']} items "
      f"over {out['totals']['runs']} runs = {out['totals']['accuracy']}%\n")
print("LADDER (item-level):")
for d in out["ladder"]:
    print(f"  {d['accuracy']:5.1f}%  {d['correct']:3d}/{d['items']:3d} items, {d['runs']:2d} runs  {d['label']}")
print("\nROUNDS:")
for d in out["rounds"]:
    print(f"  {d['round']:4s} {d['accuracy']:5.1f}%  {d['correct']:3d}/{d['items']:3d}  {d['runs']:2d} runs")
print("\nCLEAN TEXT BY ROUND:")
for d in out["clean_by_round"]:
    print(f"  {d['round']:4s} {str(d['accuracy']):>5s}%  {d['correct']:3d}/{d['items']:3d}  {d['runs']:2d} runs")
print("\nFAMILIES (R1 A01-A10):")
for d in out["families"]:
    print(f"  {d['id']} {str(d['accuracy']):>5s}%  {d['correct']}/{d['items']}  {d['runs']} runs  {d['label'][:40]}")
print("\nRUN LANES (should total 138):")
_t = 0
for d in out["run_lanes"]:
    _t += len(d["runs"])
    print(f'  {len(d["runs"]):3d}  {d["lane"]}')
print(f"  --- total {_t}")
print("\nRUN DISTRIBUTION:")
for d in out["run_distribution"]:
    print(f'  {d["band"]:8s} {d["runs"]:3d}')
print("\nDECOUPLING (control -> treatment):")
for d in out["decoupling"]:
    c, t = d["control"], d["treatment"]
    print(f'  [{d["kind"]:9s}] {c["accuracy"]:5.1f}% ({c["correct"]}/{c["items"]}, {c["runs"]} runs)'
          f' -> {t["accuracy"]:5.1f}% ({t["correct"]}/{t["items"]}, {t["runs"]} runs)  {d["label"]}')
print("\nCONTROL PAIRS:")
for p in out["control_pairs"]:
    print(f"  {p['control']['accuracy']}% ({p['control']['correct']}/{p['control']['items']}) -> "
          f"{p['treatment']['accuracy']}% ({p['treatment']['correct']}/{p['treatment']['items']})"
          f"   {p['control_label']} -> {p['treatment_label']}")
