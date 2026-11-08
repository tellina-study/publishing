#!/usr/bin/env python3
"""English variants (a1,a2,a3,h1,h2,h3) of gen_charts.py for en.md.
Same numbers/logic as gen_charts.py — text and decimal separator translated.
"""
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["svg.fonttype"] = "none"

BLUE = "#2a78d6"      # Claude Code
ORANGE = "#eb6834"    # Hermes
AQUA = "#1baf7a"      # dsh
RED = "#e34948"
INK = "#0b0b0b"
SEC_INK = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
BASELINE = "#c3c2b7"
SURFACE = "#fcfcfb"

AGENT_COLOR = {"Claude Code": BLUE, "Hermes": ORANGE, "dsh": AQUA}


def en(x, nd=2):
    return f"{x:.{nd}f}"

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
labels = ["≤1.2×", "1.75×–≥3.5×", "≤9.3×"]
y = list(range(len(agents)))[::-1]

for yi, a, l, h, lab in zip(y, agents, lo, hi, labels):
    ax.plot([l, h], [yi, yi], color=AGENT_COLOR[a], linewidth=6, solid_capstyle="round", zorder=3)
    ax.plot([h], [yi], marker="o", markersize=7, color=AGENT_COLOR[a], zorder=4)
    ax.text(h + 0.25, yi, lab, va="center", ha="left", color=INK, fontsize=11, fontweight="bold")

ax.axvline(4.33, color=MUTED, linewidth=1, linestyle=(0, (4, 3)), zorder=1)
ax.text(4.33, 1.5, "4.33× — Claude Code's reaction\nto the harness on task J", color=SEC_INK,
        fontsize=8.5, ha="center", va="center", backgroundcolor=SURFACE)

ax.set_yticks(y)
ax.set_yticklabels(agents, fontsize=11, color=INK)
ax.set_xlim(0.5, 11.5)
ax.set_ylim(-0.7, 2.7)
ax.set_xlabel("repeat-run spread, same task, same setup (×)", color=SEC_INK, fontsize=10)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0)
ax.set_axisbelow(True)
ax.set_title("How much an agent agrees with itself on a repeat", fontsize=13, color=INK, loc="left", pad=12)
save(fig, "a1_repeat_run_noise_en")

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

ax.text(0, -0.85, "dsh: tested only on the cheap model — nothing to compare against",
        fontsize=9, color=MUTED, ha="left", va="top", style="italic")
ax.set_xlim(0, 66)
ax.set_ylim(-1.1, 1.6)
ax.set_xlabel("how many times the token bill drops when switching to the cheap model of the same lineup", color=SEC_INK, fontsize=10)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0)
ax.set_axisbelow(True)
ax.set_title("Same advice (\"get a cheaper model\") — a different payoff", fontsize=12.5, color=INK, loc="left", pad=12)
save(fig, "a2_cheap_model_savings_en")

# =====================================================================
# CHART A3 — capability at the cheap model, task G (agent axis)
# =====================================================================
fig, ax = new_fig(6.2, 3.2)
agents3 = ["dsh", "Claude Code", "Hermes"]
score3 = [2, 1, 0]
colors3 = [AGENT_COLOR[a] for a in agents3]
bars = ax.barh(agents3, score3, color=colors3, height=0.55, zorder=3)
extra = {0: " — 0 files changed in either run"}
for i, (b, s) in enumerate(zip(bars, score3)):
    label = f"{s} out of 2" + extra.get(s, "")
    x = b.get_width() + 0.06 if s > 0 else 0.06
    ax.text(x, b.get_y() + b.get_height() / 2, label, va="center", ha="left",
            fontsize=12, fontweight="bold", color=INK)

ax.set_xlim(0, 2.9)
ax.set_xticks([0, 1, 2])
ax.set_ylim(-0.7, 2.7)
ax.set_xlabel("rubric score on task G, same cheap model for all three (harness is on for all three in this comparison)", color=SEC_INK, fontsize=9.5)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0)
ax.set_axisbelow(True)
ax.set_title("At the same price, not every agent pulls it off", fontsize=13, color=INK, loc="left", pad=12)
save(fig, "a3_cheap_model_capability_en")

# =====================================================================
# CHART H1 — round-ratio x per-round-ratio by genre (harness axis)
# =====================================================================
fig, ax = new_fig(7.0, 3.6)
genres = ["\"investigate\"", "\"build\""]
round_ratio = [0.84, 1.16]
perround_ratio = [1.17, 1.14]
product = [0.98, 1.32]

x = [0, 1.6]
width = 0.32
b1 = ax.bar([xi - width / 2 - 0.02 for xi in x], round_ratio, width=width, color=BLUE, zorder=3, label="step count, with harness ÷ without")
b2 = ax.bar([xi + width / 2 + 0.02 for xi in x], perround_ratio, width=width, color=ORANGE, zorder=3, label="price per step, with harness ÷ without")

for bars in (b1, b2):
    for b in bars:
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.03, en(b.get_height()),
                ha="center", va="bottom", fontsize=10.5, fontweight="bold", color=INK)

for xi, p in zip(x, product):
    ax.plot([xi], [p], marker="D", markersize=9, color=INK, zorder=5)
    ax.text(xi, p + 0.065, f"product ≈ {en(p)}", ha="center", va="bottom", fontsize=9.5, color=SEC_INK, fontweight="bold")

ax.axhline(1.0, color=MUTED, linewidth=1, linestyle=(0, (4, 3)), zorder=1)
ax.set_xticks(x)
ax.set_xticklabels(genres, fontsize=12, color=INK)
ax.set_ylim(0, 1.6)
ax.set_ylabel("ratio, with harness ÷ without (1.0 = harness changed nothing)", color=SEC_INK, fontsize=9.5)
ax.grid(axis="y", color=GRID, linewidth=0.7, zorder=0)
ax.set_axisbelow(True)
ax.legend(loc="upper center", bbox_to_anchor=(0.3, 1.0), frameon=False, fontsize=9.5, labelcolor=SEC_INK)
ax.set_title("Two effects that sometimes add up, sometimes cancel out", fontsize=13, color=INK, loc="left", pad=35)
save(fig, "h1_round_vs_perround_en")

# =====================================================================
# CHART H2 — task J mirror effect across 3 agents (harness axis, diverging)
# =====================================================================
fig, ax = new_fig(7.6, 3.8)
agentsJ = ["Hermes", "dsh", "Claude Code"]
ratioJ = [0.262, 1.574, 4.33]
logpos = [math.log2(r) for r in ratioJ]
colorsJ = [BLUE if r < 1 else RED for r in ratioJ]

bars = ax.barh(agentsJ, logpos, color=colorsJ, height=0.5, zorder=3)
for b, r in zip(bars, ratioJ):
    lp = math.log2(r)
    x = lp + 0.12 if lp >= 0 else lp - 0.12
    ha = "left" if lp >= 0 else "right"
    ax.text(x, b.get_y() + b.get_height() / 2, f"{en(r)}×", va="center", ha=ha,
            fontsize=12, fontweight="bold", color=INK)

ax.axvline(0, color=MUTED, linewidth=1.2)
ax.text(0, -1.0, "correctness: 0 out of 4 for all three, regardless of price", fontsize=9.5,
        color=SEC_INK, ha="center", style="italic")

ax.set_xlim(-2.8, 2.8)
ax.set_xticks([])
ax.set_ylim(-1.3, 4.1)
ax.set_title("Same switch, task J — opposite effect across agents", fontsize=12.5, color=INK, loc="left", pad=12)
legend_handles = [mpatches.Patch(color=BLUE, label="tokens dropped (1× = harness changed nothing)"),
                  mpatches.Patch(color=RED, label="tokens rose")]
ax.legend(handles=legend_handles, loc="center", bbox_to_anchor=(0.5, 0.92), frameon=False, fontsize=9.2, labelcolor=SEC_INK)
save(fig, "h2_task_j_mirror_en")

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
    ax.text(10.7, yi, f"score: {s} out of 2\n(identical in both runs)",
            va="center", ha="left", fontsize=9, color=SEC_INK)

ax.set_yticks(y)
ax.set_yticklabels(agentsG, fontsize=11, color=INK)
solid = mpatches.Patch(color=MUTED, label="files changed — with harness")
hatch = mpatches.Patch(color=MUTED, alpha=0.45, label="files changed — without harness")
ax.legend(handles=[solid, hatch], loc="center", bbox_to_anchor=(0.34, 1.09), ncol=2, frameon=False, fontsize=9.3, labelcolor=SEC_INK)
ax.set_xlim(0, 17.5)
ax.set_ylim(0.3, 4.6)
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax.set_xlabel("files changed in the repo (task G, same cheap model for all three)", color=SEC_INK, fontsize=9.5)
ax.grid(axis="x", color=GRID, linewidth=0.7, zorder=0)
ax.set_axisbelow(True)
ax.set_title("The harness moves effort — the outcome stays the same", fontsize=13, color=INK, loc="left", pad=28)
save(fig, "h3_task_g_antiexample_en")

print("done: 6 charts")
