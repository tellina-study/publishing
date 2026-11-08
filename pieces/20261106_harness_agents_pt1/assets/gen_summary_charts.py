#!/usr/bin/env python3
"""Two summary visualizations for ru.md: an overview scatter (all 54 cells, normalized
per task) for the opening, and a candlestick-style with/without recap for the closing.
All numbers read from equalized_matrix.csv / normalized_scatter.json, both re-derived
from the primary source this session (see tasks.md / full_results.md in
workain/research-results for the same data, publicly).
"""
import csv
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D

BLUE = "#2a78d6"      # Claude Code
ORANGE = "#eb6834"    # Hermes
AQUA = "#1baf7a"      # dsh
RED = "#e34948"
GOOD = "#0ca30c"
INK = "#0b0b0b"
SEC_INK = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
BASELINE = "#c3c2b7"
SURFACE = "#fcfcfb"

AGENT_COLOR = {"Claude Code": BLUE, "Hermes": ORANGE, "dsh": AQUA}
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
# SUMMARY 1 — overview scatter, all 54 cells (for the opening)
# =====================================================================
data = json.load(open(f"{OUT}/normalized_scatter.json"))
fig, ax = new_fig(8.5, 6.5)

for task, agent, state, norm_req, norm_tpr, quality in data:
    color = AGENT_COLOR[agent]
    marker = "o" if state == "with" else "o"
    facecolor = color if state == "with" else "none"
    edgecolor = color
    ax.scatter(norm_req, norm_tpr, s=90, marker=marker, facecolors=facecolor,
               edgecolors=edgecolor, linewidths=1.6, zorder=3, alpha=0.92)
    if task == "G":
        ax.scatter(norm_req, norm_tpr, s=220, marker="o", facecolors="none",
                   edgecolors=INK, linewidths=1.3, zorder=5)

ax.axvline(1.0, color=MUTED, linewidth=0.8, linestyle=(0, (3, 3)), zorder=1)
ax.axhline(1.0, color=MUTED, linewidth=0.8, linestyle=(0, (3, 3)), zorder=1)
ax.set_xlabel("число шагов, нормировано на среднее по задаче (1,0 = средний для этой задачи)", fontsize=9.5, color=SEC_INK)
ax.set_ylabel("цена шага, нормировано на среднее по задаче (1,0 = средний для этой задачи)", fontsize=9.5, color=SEC_INK)
ax.set_title("Все 54 прогона сразу: шаги × цена шага, по агенту и по харнесу", fontsize=13, color=INK, loc="left", pad=14)

agent_handles = [Line2D([0], [0], marker="o", color="none", markerfacecolor=c, markeredgecolor=c,
                         markersize=9, label=a) for a, c in AGENT_COLOR.items()]
state_handles = [
    Line2D([0], [0], marker="o", color="none", markerfacecolor=MUTED, markeredgecolor=MUTED, markersize=9, label="с харнесом (залито)"),
    Line2D([0], [0], marker="o", color="none", markerfacecolor="none", markeredgecolor=MUTED, markersize=9, label="без харнеса (контур)"),
]
leg1 = ax.legend(handles=agent_handles, loc="upper left", frameon=False, fontsize=9, title="Агент", title_fontsize=9, labelcolor=SEC_INK)
ax.add_artist(leg1)
leg2 = ax.legend(handles=state_handles, loc="upper right", frameon=False, fontsize=9, labelcolor=SEC_INK)
ax.add_artist(leg2)
ring_handle = [Line2D([0], [0], marker="o", color="none", markerfacecolor="none", markeredgecolor=INK,
                       markersize=11, label="задача G — единственная с разбросом качества")]
ax.legend(handles=ring_handle, loc="lower right", frameon=False, fontsize=8.8, labelcolor=SEC_INK)

ax.grid(color=GRID, linewidth=0.6, zorder=0)
ax.set_axisbelow(True)
ax.set_xlim(0, 3.6)
ax.set_ylim(0.3, 2.0)
save(fig, "s1_overview_scatter")

# =====================================================================
# SUMMARY 2 — candlestick-style with/without recap, total tokens per task (for the close)
# =====================================================================
rows = list(csv.DictReader(open(f"{OUT}/equalized_matrix.csv")))
tasks_order = ["T1", "T2", "T3", "F", "M", "S", "G", "H", "J"]
agents_order = ["Claude Code", "Hermes", "dsh"]

fig, ax = new_fig(10, 6.0)
width = 0.22
group_gap = 0.9
x_base = {t: i * group_gap for i, t in enumerate(tasks_order)}

for ai, agent in enumerate(agents_order):
    offset = (ai - 1) * (width + 0.03)
    for t in tasks_order:
        wo = [r for r in rows if r["task"] == t and r["agent"] == agent and r["state"] == "without"][0]
        w = [r for r in rows if r["task"] == t and r["agent"] == agent and r["state"] == "with"][0]
        lo_tok, hi_tok = int(wo["tokens"]), int(w["tokens"])
        up = hi_tok >= lo_tok
        color = RED if up else BLUE
        x = x_base[t] + offset
        lo, hi = sorted([lo_tok, hi_tok])
        ax.add_patch(plt.Rectangle((x - width / 2, lo), width, hi - lo, facecolor=color,
                                    edgecolor="none", alpha=0.9, zorder=3))
        # wick-style baseline marker for "without" (open) to read direction
        ax.plot([x - width / 2 - 0.015, x - width / 2 - 0.015], [lo_tok, lo_tok], marker=">",
                color=INK, markersize=0, zorder=4)

for t in tasks_order:
    ax.text(x_base[t], -0.11, t, ha="center", va="top", fontsize=10, color=INK,
            fontweight="bold", transform=ax.get_xaxis_transform())

ax.set_yscale("log")
ax.set_ylabel("токенов за прогон (лог. шкала)", fontsize=10, color=SEC_INK)
ax.set_xticks([])
ax.set_xlim(-0.6, x_base[tasks_order[-1]] + 0.6)
ax.grid(axis="y", color=GRID, linewidth=0.6, zorder=0)
ax.set_axisbelow(True)
ax.set_title("Каждая задача, каждый агент: харнес поднял счёт или опустил", fontsize=13, color=INK, loc="left", pad=48)

dir_handles = [mpatches.Patch(color=RED, label="харнес поднял токены"), mpatches.Patch(color=BLUE, label="харнес снизил токены")]
ax.legend(handles=dir_handles, loc="upper center", bbox_to_anchor=(0.5, 1.17), ncol=2, frameon=False, fontsize=9.3, labelcolor=SEC_INK)

ax.text(0.5, 1.09, "в каждой тройке слева направо: Claude Code, Hermes, dsh", transform=ax.transAxes,
        ha="center", va="bottom", fontsize=8.8, color=MUTED, style="italic")

save(fig, "s2_candlestick_recap")
