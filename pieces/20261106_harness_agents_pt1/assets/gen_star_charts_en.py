#!/usr/bin/env python3
"""English variant of the closing per-agent type-radar chart (s3) for en.md.
Same data/logic as gen_star_charts.py — category labels translated:
  анализ -> analysis, управление -> management, реализация -> execution
"""
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE = "#2a78d6"      # Claude Code
ORANGE = "#eb6834"    # Hermes
AQUA = "#1baf7a"      # dsh
INK = "#0b0b0b"
SEC_INK = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
SURFACE = "#fcfcfb"

AGENT_COLOR = {"Claude Code": BLUE, "Hermes": ORANGE, "dsh": AQUA}
AGENTS = ["Claude Code", "Hermes", "dsh"]
CATS_RU = ["анализ", "управление", "реализация"]
CATS_EN = ["analysis", "management", "execution"]
OUT = "/home/harness/harness-projects/256/.worktrees/folder-304/session-c792b49e-e286eed0/pieces/20261106_harness_agents_pt1/assets"

data_ru = json.load(open(f"{OUT}/star_ratios.json"))
data = {agent: {en_c: data_ru[agent][ru_c] for ru_c, en_c in zip(CATS_RU, CATS_EN)} for agent in AGENTS}
CATS = CATS_EN

n = len(CATS)
angles = [i * 2 * np.pi / n for i in range(n)] + [0]

fig, axes = plt.subplots(1, 3, figsize=(18, 6.0), dpi=200, subplot_kw={"polar": True})
fig.patch.set_facecolor(SURFACE)
fig.subplots_adjust(wspace=1.3, top=0.74, bottom=0.12, left=0.06, right=0.97)

r_max = 2.6
r_ticks = [0.5, 1.0, 1.5, 2.0, 2.5]
CAT_LABEL_R = r_max + 0.28

LABEL_ALIGN = {
    "analysis": dict(ha="center", va="bottom"),
    "management": dict(ha="left", va="top"),
    "execution": dict(ha="right", va="top"),
}

for ax, agent in zip(axes, AGENTS):
    ax.set_facecolor(SURFACE)
    color = AGENT_COLOR[agent]
    vals = [data[agent][c] for c in CATS] + [data[agent][CATS[0]]]

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_ylim(0, r_max)
    ax.set_yticks(r_ticks)
    ax.set_yticklabels([str(t) for t in r_ticks], fontsize=7, color=MUTED)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels([])
    for ang, cat in zip(angles[:-1], CATS):
        ax.text(ang, CAT_LABEL_R, cat, fontsize=11, color=INK, **LABEL_ALIGN[cat])
    ax.grid(color=GRID, linewidth=0.7)
    ax.spines["polar"].set_color(GRID)

    base = [1.0] * (n + 1)
    ax.plot(angles, base, color=MUTED, linewidth=1.1, linestyle=(0, (4, 3)), zorder=2)

    ax.plot(angles, vals, color=color, linewidth=2.2, zorder=4)
    ax.fill(angles, vals, color=color, alpha=0.18, zorder=3)
    ax.scatter(angles[:-1], vals[:-1], s=40, color=color, zorder=5, edgecolors=SURFACE, linewidths=1)

    ax.set_title(agent, fontsize=13, color=INK, pad=40, fontweight="bold")

fig.suptitle(
    "The harness by task type: how many times tokens change (with ÷ without), per agent",
    fontsize=13.5, color=INK, x=0.5, y=0.98,
)
fig.text(
    0.5, 0.03,
    "dashed circle — 1.0× (harness changed nothing); exact numbers — in the table below; \"management\" is a single task (M), not an average, the other two spokes are 4 tasks each",
    fontsize=8.6, color=MUTED, ha="center", style="italic",
)

fig.savefig(f"{OUT}/s3_type_stars_en.png", bbox_inches="tight", facecolor=SURFACE)
plt.close(fig)
print("wrote s3_type_stars_en")
