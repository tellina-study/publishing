#!/usr/bin/env python3
"""Render the five figures for the AI-resistant-assessment piece.

Design parameters come from the `dataviz` skill's reference palette (light mode,
surface #fcfcfb). Categorical slots used here — blue #2a78d6, orange #eb6834 —
validated with scripts/validate_palette.js: all checks PASS (worst adjacent CVD
ΔE 9.2, normal-vision 27.6).

Layout is banded top-down — title, subtitle, legend, plot, credit — so no two
text runs can ever collide. Bars are capped at 24 px thick per the mark spec.
Every figure carries its own denominators: a number without its base is not a number.

Out: pieces/20261111_ai-resistant-assessment/assets/*.png
"""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

TASK = Path(__file__).resolve().parent.parent
REPO = TASK.parent.parent
OUT = REPO / "pieces/20261111_ai-resistant-assessment/assets"
OUT.mkdir(parents=True, exist_ok=True)
D = json.loads((TASK / "data/chart_data.json").read_text(encoding="utf-8"))

# ---- design tokens (dataviz/references/palette.md, light mode) --------------
SURFACE  = "#fcfcfb"
INK      = "#0b0b0b"
INK_2    = "#52514e"
MUTED    = "#898781"
GRID     = "#e1e0d9"
BASELINE = "#c3c2b7"
BLUE     = "#2a78d6"   # categorical slot 1
ORANGE   = "#eb6834"   # categorical slot 2
BLUE_LT  = "#86b6ef"   # sequential step 250 — lightest that clears 2:1 on light
BLUE_DK  = "#184f95"   # sequential step 600
RED      = "#d03b3b"   # diverging warm pole
DPI = 160
MAXBAR_IN = 24 / DPI   # mark spec: bars never thicker than 24 px
CREDIT = "Данные: 138 прогонов, workain/research-results · tellian.io"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
    "text.color": INK, "axes.edgecolor": BASELINE, "axes.labelcolor": INK_2,
    "xtick.color": MUTED, "ytick.color": MUTED, "font.size": 9.5,
})

L = 0.022  # left text margin, figure fraction


def frame(ax, left=True, bottom=True):
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.spines["left"].set_visible(left)
    ax.spines["bottom"].set_visible(bottom)
    for side in ("left", "bottom"):
        if ax.spines[side].get_visible():
            ax.spines[side].set_linewidth(0.8)
            ax.spines[side].set_color(BASELINE)
    ax.tick_params(length=0, pad=6)


def header(fig, h_in, title, subtitle_lines, legend=None):
    """Lay out title / subtitle / legend in fixed bands measured from the top.

    Legend entries advance by the MEASURED width of their own text, so Cyrillic
    labels can never run into the next swatch. Returns the figure-fraction y
    where the plot area may begin.
    """
    def band(px):
        return px / (h_in * DPI)

    y = 1 - band(40)
    fig.text(L, y, title, fontsize=16.5, fontweight="bold", color=INK, va="center")
    y -= band(36)
    for line in subtitle_lines:
        fig.text(L, y, line, fontsize=10, color=INK_2, va="center")
        y -= band(20)
    if legend:
        y -= band(14)
        x = L
        rend = fig.canvas.get_renderer()
        fig_px = fig.get_figwidth() * DPI
        for color, label in legend:
            probe = fig.text(0, -1, label, fontsize=9.5)
            w = probe.get_window_extent(renderer=rend).width / fig_px
            probe.remove()
            if x > L and x + 0.0195 + w > 0.975:   # wrap rather than run off the edge
                x, y = L, y - band(20)
            fig.patches.append(Rectangle((x, y - band(5.5)), 0.0125, band(11),
                                         transform=fig.transFigure, facecolor=color,
                                         lw=0, clip_on=False))
            fig.text(x + 0.0195, y, label, fontsize=9.5, color=INK_2, va="center")
            x += 0.0195 + w + 0.036
        y -= band(18)
    return y - band(16)


def credit(fig):
    fig.text(L, 0.018, CREDIT, fontsize=8, color=MUTED, va="bottom")


def rbar(ax, x0, x1, y, height, color, box, radius_in=0.028):
    """Bar with rounded data-ends. mutation_aspect makes the corner radius read
    as circular despite non-square data units — matplotlib has no rounded-bar mark."""
    (xlo, xhi), (ylo, yhi), (w_in, h_in) = box
    xr, yr = xhi - xlo, yhi - ylo
    aspect = (yr / h_in) * (w_in / xr)
    r = min(radius_in * (xr / w_in), abs(x1 - x0) / 2.0)
    left, width = min(x0, x1), abs(x1 - x0)
    if width <= 0:
        return
    ax.add_patch(FancyBboxPatch((left, y - height / 2), width, height,
                                boxstyle=f"round,pad=0,rounding_size={r}",
                                mutation_aspect=aspect, linewidth=0,
                                facecolor=color, clip_on=False, zorder=3))


def bar_h(n_slots, plot_h_in, y_span):
    """Data-unit bar height that renders at most 24 px."""
    return min(0.42, MAXBAR_IN * (y_span / plot_h_in))


# =============================================================== 1. the ladder
def fig_ladder():
    SHORT = {
        "clean": "Любая формулировка на чистом тексте",
        "unicode_file": "Гомоглифы и нулевые пробелы",
        "bidi": "Переворот цифр невидимым Bidi",
        "tags": "Невидимые Unicode-теги",
        "multiscript": "Мультискриптовый коктейль",
        "stand_decoy": "Условие — про свой вариант,\nдистрактор — из курса",
        "css_zero": "Нулевой шрифт на чистом CSS",
        "param_swap": "Подмена параметров в буфере",
    }
    AQUA = "#1baf7a"   # categorical slot 3
    KIND = {"stand_decoy": AQUA, "css_zero": ORANGE, "param_swap": ORANGE}
    rows = D["ladder"]
    base = [r for r in rows if r["key"] == "clean"]
    rest = sorted([r for r in rows if r["key"] != "clean"], key=lambda r: -r["accuracy"])
    rows = base + rest

    W, H = 10.4, 7.1
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    top = header(fig, H, "Что реально снижает точность ИИ на тесте",
                 ["Claude Sonnet 5.5, закрытые задания курса. Доля ответов, точно совпавших с ключом,",
                  "и насколько подход опустил её относительно чистого текста. Обрушили её только два",
                  "подхода — и один из них не меняет в тексте ни единого символа."],
                 legend=[(BLUE, "меняем формулировку или кодировку"),
                         ("#1baf7a", "приём в формулировке — текст не тронут"),
                         (ORANGE, "подменяем текст при копировании")])
    bottom = 0.105
    ax = fig.add_axes([0.335, bottom, 0.47, top - bottom])
    n = len(rows)
    plot_h_in = (top - bottom) * H
    box = ((0, 100), (-0.72, n - 0.28), (W * 0.47, plot_h_in))
    ax.set_xlim(0, 100); ax.set_ylim(-0.72, n - 0.28); ax.invert_yaxis()
    bh = bar_h(n, plot_h_in, n + 0.44)

    for xv in (0, 25, 50, 75, 100):
        ax.axvline(xv, color=GRID, lw=0.8, zorder=0)
    ax.axvline(100, color=BASELINE, lw=1.0, zorder=1)

    for i, r in enumerate(rows):
        acc = r["accuracy"]
        rbar(ax, 0, acc, i, bh, KIND.get(r["key"], BLUE), box)
        txt = f"{acc:.0f}%" if float(acc).is_integer() else f"{acc}%"
        ax.text(104, i, txt, va="center", ha="left", fontsize=11.5,
                fontweight="bold", color=INK, clip_on=False)
        drop = round(100 - acc, 1)
        dl = "без изменений" if drop == 0 else (f"−{drop:.0f} п.п." if float(drop).is_integer() else f"−{drop} п.п.")
        ax.text(119, i, dl, va="center", ha="left", fontsize=9, color=MUTED, clip_on=False)
        two = "\n" in SHORT[r["key"]]
        ax.text(-3.5, i - (0.19 if two else 0.14), SHORT[r["key"]], va="center", ha="right",
                fontsize=10.5, color=INK, linespacing=1.3)
        ax.text(-3.5, i + (0.27 if two else 0.21),
                f'{r["correct"]}/{r["items"]} пунктов · {r["runs"]} прогонов',
                va="center", ha="right", fontsize=8.2, color=MUTED)

    ax.set_yticks([])
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xticklabels(["0", "25", "50", "75", "100%"], fontsize=9)
    frame(ax, left=False)
    ax.set_xlabel("точность ИИ на закрытых заданиях", fontsize=9.5, color=INK_2, labelpad=8)
    credit(fig)
    fig.savefig(OUT / "01-podhody-tochnost.png", dpi=DPI)
    plt.close(fig)


# ========================================================= 3. escalation plateau
def fig_escalation():
    rows = [r for r in D["clean_by_round"] if r["items"]]
    TICK = {"v1": "v1", "v2": "v2", "v3": "v3", "v4": "v4", "R1": "Р1", "R2": "Р2", "R3": "Р3",
            "R4": "Р4", "R5": "Р5", "R6": "Р6", "R7": "Р7", "R8": "Р8", "R9": "Р9"}
    STEPS = [("Р1", "десять классических методических семейств сразу"),
             ("Р5", "решающие факты убраны из условия — иди читай курс"),
             ("Р7", "выводы семинаров вывернуты наизнанку"),
             ("Р8", "шесть шагов перезаписи состояния, без калькулятора")]
    xs = list(range(len(rows)))
    ys = [r["accuracy"] for r in rows]

    W, H = 10.4, 5.6
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    top = header(fig, H, "Тринадцать заходов на формулировку — и потолок не сдвинулся",
                 ["Точность на чистом, самодостаточном тексте по раундам: сложность росла от контрфактов",
                  "до шестишаговой перезаписи состояния. 352 пункта из 353 совпали с ключом."])
    bottom = 0.175
    ax = fig.add_axes([0.075, bottom, 0.905, top - bottom])
    ax.set_xlim(-0.6, len(rows) - 0.4); ax.set_ylim(0, 112)

    for yv in (0, 25, 50, 75, 100):
        ax.axhline(yv, color=GRID, lw=0.8, zorder=0)
    ax.plot(xs, ys, color=BLUE, lw=2, solid_capstyle="round", zorder=2)
    ax.scatter(xs, ys, s=66, color=BLUE, zorder=3, edgecolors=SURFACE, linewidths=2)
    ax.text(-0.45, 103, "потолок: 100%", fontsize=9, color=MUTED, va="bottom")

    ax.text(0.35, 79, "что добавляли по дороге", fontsize=9.5, color=INK_2, va="center")
    for k, (rd, text) in enumerate(STEPS):
        ax.text(0.35, 66 - k * 11, rd, fontsize=9.3, color=INK_2, va="center", fontweight="bold")
        ax.text(1.02, 66 - k * 11, text, fontsize=9.3, color=MUTED, va="center")

    i9 = {r["round"]: i for i, r in enumerate(rows)}["R9"]
    ax.annotate("97.8% — первая осечка\nна чистом тексте", xy=(i9, ys[i9]), xytext=(i9 + 0.15, 74),
                fontsize=9.3, color=INK_2, ha="right", va="top", linespacing=1.4,
                arrowprops=dict(arrowstyle="-", color=BASELINE, lw=1.0, shrinkA=2, shrinkB=6))

    ax.set_xticks(xs)
    ax.set_xticklabels([TICK[r["round"]] for r in rows], fontsize=10, color=INK_2)
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_yticklabels(["0", "25", "50", "75", "100%"], fontsize=9)
    frame(ax)
    ax.spines["bottom"].set_position(("data", 0))
    for i, r in enumerate(rows):
        ax.text(i, -13.5, str(r["items"]), ha="center", va="top", fontsize=8, color=MUTED)
    ax.text(-0.72, -13.5, "пунктов:", ha="right", va="top", fontsize=8,
            color=MUTED, clip_on=False)
    credit(fig)
    fig.savefig(OUT / "04-eskalaciya-raundov.png", dpi=DPI)
    plt.close(fig)


# ============================================================== 3. ten families
def fig_families():
    rows = D["families"]
    W, H = 10.4, 5.5
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    top = header(fig, H, "Десять школьных способов сделать задание «нерешаемым для ИИ»",
                 ["Раунд 1: десять независимых методических семейств — по два задания и два свежих",
                  "контекста на каждое. Сорок пунктов из сорока ушли в ключ."])
    ax = fig.add_axes([0.0, 0.075, 1.0, top - 0.075])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")

    n = len(rows)
    y_top, y_bot = 0.955, 0.175
    row_h = (y_top - y_bot) / (n - 1)
    x_sq, sq_w, sq_h, gap = 0.595, 0.0165, 0.052, 0.0085

    def square(x, y, filled):
        ax.add_patch(FancyBboxPatch((x, y - sq_h / 2), sq_w, sq_h,
                                    boxstyle="round,pad=0,rounding_size=0.004",
                                    mutation_aspect=0.40,
                                    facecolor=BLUE if filled else SURFACE,
                                    edgecolor="none" if filled else BASELINE,
                                    linewidth=0 if filled else 1.0))

    for i, r in enumerate(rows):
        y = y_top - i * row_h
        ax.text(0.572, y, f'{r["id"]}  {r["label"]}', ha="right", va="center",
                fontsize=10.3, color=INK)
        for j in range(r["items"]):
            square(x_sq + j * (sq_w + gap), y, j < r["correct"])
        ax.text(x_sq + 4 * (sq_w + gap) + 0.014, y, f'{r["correct"]}/{r["items"]}',
                ha="left", va="center", fontsize=10, color=INK_2)

    square(x_sq, 0.045, True)
    ax.text(x_sq + sq_w + 0.011, 0.045, "пункт совпал с ключом", fontsize=9, color=INK_2, va="center")
    square(x_sq + 0.205, 0.045, False)
    ax.text(x_sq + 0.205 + sq_w + 0.011, 0.045, "не совпал — ни одного",
            fontsize=9, color=INK_2, va="center")
    credit(fig)
    fig.savefig(OUT / "03-desyat-semejstv.png", dpi=DPI)
    plt.close(fig)


# ============================== 4. where the accuracy actually goes (text untouched)
def fig_decoupling():
    rows = D["decoupling"]
    AQUA = "#1baf7a"
    W, H = 10.4, 6.0
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    top = header(fig, H, "Точность обрушивается, когда в тексте не тронут ни один символ",
                 ["Одни и те же задания, один и тот же ключ, одна и та же модель. Меняется ровно одно:",
                  "есть ли у ИИ то, что видит студент. Контроль держит 100% — значит это не про знание."],
                 legend=[(BLUE_LT, "у ИИ есть всё, что у студента"),
                         (AQUA, "у ИИ только опубликованный курс"),
                         (ORANGE, "текст подменён при копировании")])
    bottom = 0.135
    ax = fig.add_axes([0.285, bottom, 0.655, top - bottom])
    n = len(rows)
    ax.set_xlim(-4, 104); ax.set_ylim(-0.75, n - 0.25); ax.invert_yaxis()

    for xv in (0, 25, 50, 75, 100):
        ax.axvline(xv, color=GRID, lw=0.8, zorder=0)

    untouched = [i for i, r in enumerate(rows) if r["kind"] == "untouched"]
    div = max(untouched) + 0.5
    ax.axhline(div, color=GRID, lw=0.8, zorder=0)
    ax.text(44, div - 0.07, "текст не тронут", ha="center", va="bottom",
            fontsize=9, color=MUTED)
    ax.text(44, div + 0.09, "текст подменён при копировании", ha="center", va="top",
            fontsize=9, color=MUTED)

    for i, r in enumerate(rows):
        c, t = r["control"]["accuracy"], r["treatment"]["accuracy"]
        tone = AQUA if r["kind"] == "untouched" else ORANGE
        ax.annotate("", xy=(t, i), xytext=(c, i),
                    arrowprops=dict(arrowstyle="-|>,head_width=0.2,head_length=0.45",
                                    color=tone, lw=2, shrinkA=7, shrinkB=3), zorder=2)
        ax.scatter([c], [i], s=145, color=BLUE_LT, zorder=3, edgecolors=SURFACE, linewidths=2)
        ax.scatter([t], [i], s=145, color=tone, zorder=4, edgecolors=SURFACE, linewidths=2)
        lines = r["label"].count("\n") + 1
        ax.text(-8, i - (0.16 if lines > 1 else 0.10), r["label"], ha="right", va="center",
                fontsize=10, color=INK, linespacing=1.35)
        ax.text(-8, i + (0.24 if lines > 1 else 0.18),
                f'{r["treatment"]["runs"]} прогона без них · {r["control"]["runs"]} с ними',
                ha="right", va="center", fontsize=8.2, color=MUTED)
        for val, cell in ((c, r["control"]), (t, r["treatment"])):
            ax.text(val, i - 0.24, f'{val:.0f}%', ha="center", va="bottom",
                    fontsize=11.5, fontweight="bold", color=INK)
            ax.text(val, i + 0.20, f'{cell["correct"]}/{cell["items"]}',
                    ha="center", va="center", fontsize=8.6, color=MUTED)

    ax.set_yticks([])
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xticklabels(["0", "25", "50", "75", "100%"], fontsize=9)
    frame(ax, left=False)
    ax.set_xlabel("точность ИИ на тех же самых заданиях", fontsize=9.5, color=INK_2, labelpad=8)
    credit(fig)
    fig.savefig(OUT / "05-tochnost-bez-podmeny.png", dpi=DPI)
    plt.close(fig)


# ================================= 5. the mechanism, in the model's own answers
def fig_answer_grid():
    g = D["answer_grid"]
    AQUA = "#1baf7a"
    W, H = 10.4, 5.0
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    top = header(fig, H, "Модель не ошибается наугад — она идёт туда, куда её завели",
                 ["Три задания вектора V2, буквы ответов как есть. В варианте A лежат канонические числа",
                  "с публичной страницы курса — ровно то, что найдёт ИИ, когда решающих чисел у него нет."],
                 legend=[(BLUE, "совпал с ключом"),
                         (AQUA, "подброшенный вариант A — числа с публичного сайта курса"),
                         (MUTED, "другой неверный")])
    ax = fig.add_axes([0.0, 0.085, 1.0, top - 0.085])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")

    x0, cw, ch = 0.405, 0.125, 0.155
    y_top = 0.70
    for j, item in enumerate(g["items"]):
        ax.text(x0 + j * cw + (cw - 0.032) / 2, y_top + 0.205, item, ha="center", va="center",
                fontsize=9.5, color=INK_2)
        ax.text(x0 + j * cw + (cw - 0.032) / 2, y_top + 0.145, f'ключ: {g["key"][j]}',
                ha="center", va="center", fontsize=8.3, color=MUTED)

    for i, row in enumerate(g["rows"]):
        y = y_top - i * (ch + 0.075)
        ax.text(0.385, y + 0.022, row["label"], ha="right", va="center", fontsize=10.3, color=INK)
        ax.text(0.385, y - 0.042, row["sub"], ha="right", va="center", fontsize=8.6, color=MUTED)
        for j, a in enumerate(row["answers"]):
            correct = a == g["key"][j]
            color = BLUE if correct else (AQUA if a == g["planted"] else MUTED)
            ax.add_patch(FancyBboxPatch((x0 + j * cw, y - ch / 2), cw - 0.032, ch,
                                        boxstyle="round,pad=0,rounding_size=0.006",
                                        mutation_aspect=0.42, facecolor=color, linewidth=0))
            ax.text(x0 + j * cw + (cw - 0.032) / 2, y, a, ha="center", va="center",
                    fontsize=15, fontweight="bold", color="#ffffff")

    ax.text(0.405, 0.055, "Пять ответов из шести — вариант A. В ключ модель попала один раз:\n"
                          "третье задание во втором прогоне.",
            fontsize=9, color=MUTED, ha="left", va="center", linespacing=1.5)
    credit(fig)
    fig.savefig(OUT / "06-mehanizm-otvetov.png", dpi=DPI)
    plt.close(fig)


# ===================================== 2. the per-model descent, as measured
def fig_models_descent():
    pr = D["cross_model_probe"]
    bars = pr["bars"]
    AQUA = "#1baf7a"
    W, H = 10.4, 5.6
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    top = header(fig, H, "Одни и те же два задания — и разброс от 100% до четверти",
                 ["Открытые инженерные кейсы со структурной интерференцией, по двухкритериальной",
                  "рубрике: 2 балла за задание, 4 всего. По одному прогону на строку, шесть наблюдений.",
                  "Для сравнения: на чистых самодостаточных заданиях тот же Sonnet берёт 352 пункта из 353."])
    bottom = 0.135
    ax = fig.add_axes([0.305, bottom, 0.58, top - bottom])
    n = len(bars)
    plot_h_in = (top - bottom) * H
    box = ((0, 100), (-0.72, n - 0.28), (W * 0.58, plot_h_in))
    ax.set_xlim(0, 100); ax.set_ylim(-0.72, n - 0.28); ax.invert_yaxis()
    bh = bar_h(n, plot_h_in, n + 0.44)

    for xv in (0, 25, 50, 75, 100):
        ax.axvline(xv, color=GRID, lw=0.8, zorder=0)

    for i, b in enumerate(bars):
        pct = 100 * b["points"] / pr["max_points"]
        tone = BLUE if i == 0 else (AQUA if i == 1 else ORANGE)
        rbar(ax, 0, pct, i, bh, tone, box)
        ax.text(104, i - 0.02, f"{pct:.0f}%", va="center", ha="left",
                fontsize=13, fontweight="bold", color=INK, clip_on=False)
        ax.text(104, i + 0.27, f'{b["points"]} из {pr["max_points"]} баллов', va="center",
                ha="left", fontsize=8.5, color=MUTED, clip_on=False)
        ax.text(-3.5, i - 0.15, b["label"], va="center", ha="right", fontsize=10.8, color=INK)
        ax.text(-3.5, i + 0.17, b["sub"], va="center", ha="right", fontsize=8.6, color=MUTED)
        ax.text(2.5, i + 0.47, b["detail"], va="center", ha="left", fontsize=8.4, color=MUTED)

    ax.set_yticks([])
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.set_xticklabels(["0", "25", "50", "75", "100%"], fontsize=9)
    frame(ax, left=False)
    ax.set_xlabel("доля набранных баллов рубрики", fontsize=9.5, color=INK_2, labelpad=8)
    credit(fig)
    fig.savefig(OUT / "02-po-modelyam.png", dpi=DPI)
    plt.close(fig)


# ============================================================= 7. three models
def fig_models():
    q = D["q1_cross_model"]
    true, ms = q["true_answer"], q["models"]

    W, H = 10.4, 5.9
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    top = header(fig, H, "Одно задание, четыре прогона — и три разных неверных ответа",
                 ["Задание Q1: сколько вызовов LLM сделает каскад с повторным вызовом судьи.",
                  "Верный ответ — 236. По одному прогону на строку."])
    bottom = 0.165
    ax = fig.add_axes([0.295, bottom, 0.625, top - bottom])
    n = len(ms)
    plot_h_in = (top - bottom) * H
    xlim, ylim = (-115, 42), (-0.62, n - 0.38)
    box = (xlim, ylim, (W * 0.625, plot_h_in))
    ax.set_xlim(*xlim); ax.set_ylim(*ylim); ax.invert_yaxis()
    bh = bar_h(n, plot_h_in, n + 0.24)

    for xv in (-100, -75, -50, -25, 25):
        ax.axvline(xv, color=GRID, lw=0.8, zorder=0)
    ax.axvline(0, color=BASELINE, lw=1.4, zorder=1)
    ax.text(0, -0.66, f"верный ответ — {true} вызовов LLM", ha="center", va="bottom",
            fontsize=9.5, color=INK_2)

    for i, m in enumerate(ms):
        d = m["answer"] - true
        if d == 0:
            ax.scatter([0], [i], s=170, color="#0ca30c", zorder=4,
                       edgecolors=SURFACE, linewidths=2)
        else:
            rbar(ax, 0, d, i, bh, BLUE if d > 0 else RED, box)
        off = 5 if d >= 0 else -5
        ha = "left" if d >= 0 else "right"
        ax.text(d + off, i - 0.10, str(m["answer"]), ha=ha, va="center",
                fontsize=12, fontweight="bold", color=INK)
        ax.text(d + off, i + 0.16,
                "верно" if d == 0 else f"{d:+d}".replace("-", "\u2212"),
                ha=ha, va="center", fontsize=9, color=MUTED)
        ax.text(-119, i - 0.17, m["model"], ha="right", va="center", fontsize=10.5, color=INK)
        ax.text(-119, i + 0.13, m["variant"], ha="right", va="center",
                fontsize=8.6, color=INK_2)
        ax.text(-119, i + 0.40, m["failure"], ha="right", va="center",
                fontsize=8.3, color=MUTED)

    ax.set_yticks([])
    ax.set_xticks([-100, -75, -50, -25, 0, 25])
    ax.set_xticklabels(["−100", "−75", "−50", "−25", "0", "+25"], fontsize=9)
    frame(ax, left=False)
    ax.set_xlabel("отклонение от верного ответа, вызовов LLM", fontsize=9.5, color=INK_2, labelpad=8)
    credit(fig)
    fig.savefig(OUT / "07-tri-modeli.png", dpi=DPI)
    plt.close(fig)


for f in (fig_ladder, fig_models_descent, fig_families, fig_escalation,
          fig_decoupling, fig_answer_grid, fig_models):
    f()
    print("ok", f.__name__)
