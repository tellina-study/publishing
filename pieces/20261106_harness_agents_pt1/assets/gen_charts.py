#!/usr/bin/env python3
"""Generate all charts/diagrams for pieces/20261106_harness_agents_pt1/ru.md.

Every number here is copied from ru.md's own already fact-checked prose/tables —
nothing here is invented for the chart. Palette follows the dataviz skill's
reference instance (references/palette.md): fixed categorical order
(Claude Code = blue, Hermes = orange, dsh = aqua), diverging blue<->red for
signed effects, light surface, muted ink for chrome, direct labels instead of
legends where only 1-3 series are on screen.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.font_manager as fm

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["svg.fonttype"] = "none"

# ---- palette (dataviz skill reference instance, light mode) ----
BLUE = "#2a78d6"      # Claude Code
ORANGE = "#eb6834"    # Hermes
AQUA = "#1baf7a"      # dsh
RED = "#e34948"       # diverging warm pole / increase
INK = "#0b0b0b"
SEC_INK = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
BASELINE = "#c3c2b7"
SURFACE = "#fcfcfb"
NEUTRAL_MID = "#f0efec"

AGENT_COLOR = {"Claude Code": BLUE, "Hermes": ORANGE, "dsh": AQUA}


def ru(x, nd=2):
    return f"{x:.{nd}f}".replace(".", ",")

OUT = "/home/harness/harness-projects/256/.worktrees/folder-304/session-c792b49e-e286eed0/pieces/20261106_harness_agents_pt1/assets"


def new_fig(w, h):
    fig, ax = plt.subplots(figsize=(w, h), dpi=200)
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_color(BASELINE)
        ax.spines[spine].set_linewidth(0.8)
    ax.tick_params(colors=MUTED, labelsize=10)
    return fig, ax


def save(fig, name):
    fig.savefig(f"{OUT}/{name}.png", bbox_inches="tight", facecolor=SURFACE)
    plt.close(fig)
    print("wrote", name)


# =====================================================================
# CHART A1 — repeat-run noise range per agent (agent axis)
# =====================================================================
fig, ax = new_fig(7.2, 3.8)
agents = ["Claude Code", "dsh", "Hermes"]
lo = [1.0, 1.75, 1.0]
hi = [1.2, 3.5, 9.3]
labels = ["≤1,2×", "1,75×–≥3,5×", "≤9,3×"]
y = list(range(len(agents)))[::-1]

for yi, a, l, h, lab in zip(y, agents, lo, hi, labels):
    ax.plot([l, h], [yi, yi], color=AGENT_COLOR[a], linewidth=6, solid_capstyle="round", zorder=3)
    ax.plot([h], [yi], marker="o", markersize=7, color=AGENT_COLOR[a], zorder=4)
    ax.text(h + 0.25, yi, lab, va="center", ha="left", color=INK, fontsize=11, fontweight="bold")

ax.axvline(4.33, color=MUTED, linewidth=1, linestyle=(0, (4, 3)), zorder=1)
ax.text(4.33, 1.5, "4,33× — реакция Claude Code\nна харнес в задаче J", color=SEC_INK,
        fontsize=8.5, ha="center", va="center", backgroundcolor=SURFACE)

ax.set_yticks(y)
ax.set_yticklabels(agents, fontsize=11, color=INK)
ax.set_xlim(0.5, 11.5)
ax.set_ylim(-0.7, 2.7)
ax.set_xlabel("разброс повторного прогона той же задачи, той же настройки (×)", color=SEC_INK, fontsize=10)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0)
ax.set_axisbelow(True)
ax.set_title("Насколько агент сходится сам с собой на повторе", fontsize=13, color=INK, loc="left", pad=12)
save(fig, "a1_repeat_run_noise")

# =====================================================================
# CHART A2 — cost multiplier when switching to the cheap model (agent axis)
# =====================================================================
fig, ax = new_fig(6.2, 3.2)
agents2 = ["Claude Code", "Hermes"]
mult = [9, 56]
colors2 = [AGENT_COLOR[a] for a in agents2]
bars = ax.barh(agents2, mult, color=colors2, height=0.55, zorder=3)
for b, m in zip(bars, mult):
    ax.text(b.get_width() + 1.5, b.get_y() + b.get_height() / 2, f"÷{m}", va="center",
            ha="left", fontsize=13, fontweight="bold", color=INK)

ax.text(0, -0.85, "dsh: тестировался только на дешёвой модели — сравнить не с чем",
        fontsize=9, color=MUTED, ha="left", va="top", style="italic")
ax.set_xlim(0, 66)
ax.set_ylim(-1.1, 1.6)
ax.set_xlabel("во сколько раз падает счёт за токены при переходе на дешёвую модель той же линейки", color=SEC_INK, fontsize=10)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0)
ax.set_axisbelow(True)
ax.set_title("Один и тот же совет («возьми модель подешевле») — разный выигрыш", fontsize=12.5, color=INK, loc="left", pad=12)
save(fig, "a2_cheap_model_savings")

# =====================================================================
# CHART A3 — capability at the cheap model, task G (agent axis)
# =====================================================================
fig, ax = new_fig(6.2, 3.2)
agents3 = ["dsh", "Claude Code", "Hermes"]
score3 = [2, 1, 0]
colors3 = [AGENT_COLOR[a] for a in agents3]
bars = ax.barh(agents3, score3, color=colors3, height=0.55, zorder=3)
extra = {0: " — 0 изменённых файлов в обоих прогонах"}
for i, (b, s) in enumerate(zip(bars, score3)):
    label = f"{s} из 2" + extra.get(s, "")
    x = b.get_width() + 0.06 if s > 0 else 0.06
    ax.text(x, b.get_y() + b.get_height() / 2, label, va="center", ha="left",
            fontsize=12, fontweight="bold", color=INK)

ax.set_xlim(0, 2.9)
ax.set_xticks([0, 1, 2])
ax.set_ylim(-0.7, 2.7)
ax.set_xlabel("балл по рубрике задачи G на одной и той же дешёвой модели (харнес в этом сравнении включён у всех троих)", color=SEC_INK, fontsize=9.5)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0)
ax.set_axisbelow(True)
ax.set_title("При одной и той же цене задачу вытягивает не каждый", fontsize=13, color=INK, loc="left", pad=12)
save(fig, "a3_cheap_model_capability")

# =====================================================================
# CHART H1 — round-ratio x per-round-ratio by genre (harness axis)
# =====================================================================
fig, ax = new_fig(7.0, 3.6)
genres = ["«разобраться»", "«построить»"]
round_ratio = [0.84, 1.16]
perround_ratio = [1.17, 1.14]
product = [0.98, 1.32]

x = [0, 1.6]
width = 0.32
b1 = ax.bar([xi - width / 2 - 0.02 for xi in x], round_ratio, width=width, color=BLUE, zorder=3, label="число шагов, с харнесом ÷ без")
b2 = ax.bar([xi + width / 2 + 0.02 for xi in x], perround_ratio, width=width, color=ORANGE, zorder=3, label="цена одного шага, с харнесом ÷ без")

for bars in (b1, b2):
    for b in bars:
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.03, ru(b.get_height()),
                ha="center", va="bottom", fontsize=10.5, fontweight="bold", color=INK)

for xi, p in zip(x, product):
    ax.plot([xi], [p], marker="D", markersize=9, color=INK, zorder=5)
    ax.text(xi, p + 0.065, f"итог ≈ {ru(p)}", ha="center", va="bottom", fontsize=9.5, color=SEC_INK, fontweight="bold")

ax.axhline(1.0, color=MUTED, linewidth=1, linestyle=(0, (4, 3)), zorder=1)
ax.set_xticks(x)
ax.set_xticklabels(genres, fontsize=12, color=INK)
ax.set_ylim(0, 1.6)
ax.set_ylabel("отношение с харнесом ÷ без (1,0 = харнес не изменил ничего)", color=SEC_INK, fontsize=9.5)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0)
ax.set_axisbelow(True)
ax.legend(loc="upper center", bbox_to_anchor=(0.27, 1.0), frameon=False, fontsize=9.5, labelcolor=SEC_INK)
ax.set_title("Два эффекта, которые то складываются, то гасят друг друга", fontsize=13, color=INK, loc="left", pad=35)
save(fig, "h1_round_vs_perround")

# =====================================================================
# CHART H2 — task J mirror effect across 3 agents (harness axis, diverging)
# =====================================================================
fig, ax = new_fig(7.6, 3.8)
agentsJ = ["Hermes", "dsh", "Claude Code"]
ratioJ = [0.262, 1.574, 4.33]
logpos = [__import__("math").log2(r) for r in ratioJ]
colorsJ = [BLUE if r < 1 else RED for r in ratioJ]

bars = ax.barh(agentsJ, logpos, color=colorsJ, height=0.5, zorder=3)
for b, r in zip(bars, ratioJ):
    lp = __import__("math").log2(r)
    x = lp + 0.12 if lp >= 0 else lp - 0.12
    ha = "left" if lp >= 0 else "right"
    ax.text(x, b.get_y() + b.get_height() / 2, f"{ru(r)}×", va="center", ha=ha,
            fontsize=12, fontweight="bold", color=INK)

ax.axvline(0, color=MUTED, linewidth=1.2)
ax.text(0, -1.0, "правильность: 0 из 4 у всех троих, независимо от цены", fontsize=9.5,
        color=SEC_INK, ha="center", style="italic")

ax.set_xlim(-2.8, 2.8)
ax.set_xticks([])
ax.set_ylim(-1.3, 4.1)
ax.set_title("Тот же тумблер, задача J — противоположный эффект у разных агентов", fontsize=12.5, color=INK, loc="left", pad=12)
legend_handles = [mpatches.Patch(color=BLUE, label="токены упали (1× = харнес ничего не изменил)"),
                  mpatches.Patch(color=RED, label="токены выросли")]
ax.legend(handles=legend_handles, loc="center", bbox_to_anchor=(0.5, 0.92), frameon=False, fontsize=9.2, labelcolor=SEC_INK)
save(fig, "h2_task_j_mirror")

# =====================================================================
# CHART H3 — task G antiexample: files changed with/without harness (harness axis)
# =====================================================================
fig, ax = new_fig(8.0, 4.1)
agentsG = ["dsh", "Claude Code", "Hermes"]
with_h = [8, 5, 0]
without_h = [5, 7, 0]
scoreG = [2, 1, 0]

y = [yy + 1.0 for yy in list(range(len(agentsG)))[::-1]]
width = 0.32
for yi, a, wh, wo, s in zip(y, agentsG, with_h, without_h, scoreG):
    ax.barh(yi + width / 2 + 0.02, wh, height=width, color=AGENT_COLOR[a], zorder=3)
    ax.barh(yi - width / 2 - 0.02, wo, height=width, color=AGENT_COLOR[a], alpha=0.45, zorder=3)
    ax.text(10.7, yi, f"балл: {s} из 2\n(одинаков в обоих прогонах)",
            va="center", ha="left", fontsize=9, color=SEC_INK)

ax.set_yticks(y)
ax.set_yticklabels(agentsG, fontsize=11, color=INK)
solid = mpatches.Patch(color=MUTED, label="файлов изменено — с харнесом")
hatch = mpatches.Patch(color=MUTED, alpha=0.45, label="файлов изменено — без харнеса")
ax.legend(handles=[solid, hatch], loc="center", bbox_to_anchor=(0.32, 1.09), ncol=2, frameon=False, fontsize=9.3, labelcolor=SEC_INK)
ax.set_xlim(0, 17.5)
ax.set_ylim(0.3, 4.6)
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax.set_xlabel("файлов, изменённых в репозитории (задача G, одна и та же дешёвая модель у всех троих)", color=SEC_INK, fontsize=9.5)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0)
ax.set_axisbelow(True)
ax.set_title("Харнес двигает усилие — результат остаётся тем же", fontsize=13, color=INK, loc="left", pad=28)
save(fig, "h3_task_g_antiexample")

print("done: 6 charts")
