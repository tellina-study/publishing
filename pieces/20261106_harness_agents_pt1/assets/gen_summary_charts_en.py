#!/usr/bin/env python3
"""English variant of the opening overview scatter (s1) for en.md.
Same data/logic as gen_summary_charts.py — text translated.
"""
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

BLUE = "#2a78d6"      # Claude Code
ORANGE = "#eb6834"    # Hermes
AQUA = "#1baf7a"      # dsh
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


data = json.load(open(f"{OUT}/normalized_scatter.json"))
fig, ax = new_fig(8.5, 6.5)

for task, agent, state, norm_req, norm_tpr, quality in data:
    color = AGENT_COLOR[agent]
    facecolor = color if state == "with" else "none"
    edgecolor = color
    ax.scatter(norm_req, norm_tpr, s=90, marker="o", facecolors=facecolor,
               edgecolors=edgecolor, linewidths=1.6, zorder=3, alpha=0.92)
    if task == "G":
        ax.scatter(norm_req, norm_tpr, s=220, marker="o", facecolors="none",
                   edgecolors=INK, linewidths=1.3, zorder=5)

ax.axvline(1.0, color=MUTED, linewidth=0.8, linestyle=(0, (3, 3)), zorder=1)
ax.axhline(1.0, color=MUTED, linewidth=0.8, linestyle=(0, (3, 3)), zorder=1)
ax.set_xlabel("step count, normalized to that task's own average (1.0 = average for this task)", fontsize=9.5, color=SEC_INK)
ax.set_ylabel("price per step, normalized to that task's own average (1.0 = average for this task)", fontsize=9.5, color=SEC_INK)
ax.set_title("All 54 runs at once: steps × price per step, by agent and by harness", fontsize=13, color=INK, loc="left", pad=14)

agent_handles = [Line2D([0], [0], marker="o", color="none", markerfacecolor=c, markeredgecolor=c,
                         markersize=9, label=a) for a, c in AGENT_COLOR.items()]
state_handles = [
    Line2D([0], [0], marker="o", color="none", markerfacecolor=MUTED, markeredgecolor=MUTED, markersize=9, label="with harness (filled)"),
    Line2D([0], [0], marker="o", color="none", markerfacecolor="none", markeredgecolor=MUTED, markersize=9, label="without harness (outline)"),
]
leg1 = ax.legend(handles=agent_handles, loc="upper left", frameon=False, fontsize=9, title="Agent", title_fontsize=9, labelcolor=SEC_INK)
ax.add_artist(leg1)
leg2 = ax.legend(handles=state_handles, loc="upper right", frameon=False, fontsize=9, labelcolor=SEC_INK)
ax.add_artist(leg2)
ring_handle = [Line2D([0], [0], marker="o", color="none", markerfacecolor="none", markeredgecolor=INK,
                       markersize=11, label="task G — the only one with quality spread")]
ax.legend(handles=ring_handle, loc="lower right", frameon=False, fontsize=8.8, labelcolor=SEC_INK)

ax.grid(color=GRID, linewidth=0.6, zorder=0)
ax.set_axisbelow(True)
ax.set_xlim(0, 3.6)
ax.set_ylim(0.3, 2.0)
save(fig, "s1_overview_scatter_en")
