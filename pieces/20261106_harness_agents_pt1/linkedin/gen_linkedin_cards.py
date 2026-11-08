#!/usr/bin/env python3
"""5 standalone LinkedIn stat cards for the harness-agents-pt1 series.
Square-ish (1200x1200), big hero numbers, minimal supporting text — built to
read unambiguously with zero surrounding article context. Every number here
is copied from the already fact-checked ru.md/en.md — nothing re-derived.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLUE = "#2a78d6"      # Claude Code
ORANGE = "#eb6834"    # Hermes
AQUA = "#1baf7a"      # dsh
RED = "#e34948"
INK = "#0b0b0b"
SEC_INK = "#52514e"
MUTED = "#898781"
SURFACE = "#fcfcfb"
GOOD = "#0ca30c"

OUT = "/home/harness/harness-projects/256/.worktrees/folder-304/session-c792b49e-e286eed0/pieces/20261106_harness_agents_pt1/linkedin"


def new_fig():
    fig, ax = plt.subplots(figsize=(6, 6), dpi=200)
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    return fig, ax


def save(fig, name):
    fig.savefig(f"{OUT}/{name}.png", facecolor=SURFACE, bbox_inches="tight", pad_inches=0.3)
    plt.close(fig)
    print("wrote", name)


# =====================================================================
# CARD 1 — quality didn't move
# =====================================================================
fig, ax = new_fig()
ax.text(5, 9.1, "SAME AGENT. HARNESS ON vs OFF.", fontsize=15, color=MUTED, ha="center", fontweight="bold")
ax.text(5, 8.2, "One task, 3 agents — the only one\nwhere quality varied at all:", fontsize=12.5, color=SEC_INK, ha="center")

rows = [("dsh", AQUA, "2 / 2", "2 / 2"), ("Claude Code", BLUE, "1 / 2", "1 / 2"), ("Hermes", ORANGE, "0 / 2", "0 / 2")]
y0 = 6.3
for i, (name, color, wo, w) in enumerate(rows):
    y = y0 - i * 1.55
    ax.text(0.6, y, name, fontsize=15, color=INK, ha="left", va="center", fontweight="bold")
    ax.text(5.2, y, wo, fontsize=20, color=color, ha="center", va="center", fontweight="bold")
    ax.text(6.3, y, "=", fontsize=18, color=MUTED, ha="center", va="center")
    ax.text(7.4, y, w, fontsize=20, color=color, ha="center", va="center", fontweight="bold")

ax.text(5.2, 7.3, "without harness", fontsize=9.5, color=MUTED, ha="center")
ax.text(7.4, 7.3, "with harness", fontsize=9.5, color=MUTED, ha="center")

ax.text(5, 0.9, "Quality didn't move once — for any of the three.", fontsize=13, color=INK, ha="center", fontweight="bold")
save(fig, "card1_quality_flat")

# =====================================================================
# CARD 2 — agent noise bigger than the harness signal
# =====================================================================
fig, ax = new_fig()
ax.text(5, 9.1, "RUN IT TWICE.", fontsize=22, color=INK, ha="center", fontweight="bold")
ax.text(5, 8.25, "Same task. Same settings. Nothing changed.", fontsize=12.5, color=SEC_INK, ha="center")

ax.text(2.6, 5.7, "9.3×", fontsize=42, color=ORANGE, ha="center", fontweight="bold")
ax.text(2.6, 4.4, "Hermes,\ntwo identical runs", fontsize=10.5, color=SEC_INK, ha="center")

ax.text(7.6, 5.7, "4.33×", fontsize=42, color=BLUE, ha="center", fontweight="bold")
ax.text(7.6, 4.4, "Claude Code's loudest\nharness effect in the test", fontsize=10.5, color=SEC_INK, ha="center")

ax.plot([5.1, 5.1], [3.9, 7.0], color="#d8d7ce", linewidth=1.5)

ax.text(5, 1.3, "The agent's own noise outsized\nthe harness effect we were testing.", fontsize=13.5, color=INK, ha="center", fontweight="bold")
save(fig, "card2_noise_vs_signal")

# =====================================================================
# CARD 3 — mirror effect on the same switch
# =====================================================================
fig, ax = new_fig()
ax.text(5, 9.1, "SAME SWITCH. SAME TASK.", fontsize=16, color=MUTED, ha="center", fontweight="bold")
ax.text(5, 8.25, "Turning the harness ON changed token spend:", fontsize=12.5, color=SEC_INK, ha="center")

ax.text(3, 5.9, "+333%", fontsize=40, color=RED, ha="center", fontweight="bold")
ax.text(3, 4.85, "Claude Code", fontsize=13, color=INK, ha="center", fontweight="bold")

ax.text(7.3, 5.9, "−74%", fontsize=40, color=BLUE, ha="center", fontweight="bold")
ax.text(7.3, 4.85, "Hermes", fontsize=13, color=INK, ha="center", fontweight="bold")

ax.plot([5.1, 5.1], [4.2, 7.1], color="#d8d7ce", linewidth=1.5)

ax.text(5, 2.9, "Correct answers either way: 0 out of 4.\nFor both agents.", fontsize=12.5, color=SEC_INK, ha="center")
ax.text(5, 1.1, "One switch. Opposite reactions. Same outcome.", fontsize=13.5, color=INK, ha="center", fontweight="bold")
save(fig, "card3_mirror_effect")

# =====================================================================
# CARD 4 — cheap model payoff differs 6x
# =====================================================================
fig, ax = new_fig()
ax.text(5, 9.1, '"JUST USE A CHEAPER MODEL."', fontsize=15.5, color=MUTED, ha="center", fontweight="bold")
ax.text(5, 8.25, "Same advice, two agents, same cheap/expensive pair:", fontsize=12, color=SEC_INK, ha="center")

ax.text(3, 5.8, "÷9", fontsize=50, color=BLUE, ha="center", fontweight="bold")
ax.text(3, 4.6, "Claude Code", fontsize=13, color=INK, ha="center", fontweight="bold")

ax.text(7.3, 5.8, "÷56", fontsize=50, color=ORANGE, ha="center", fontweight="bold")
ax.text(7.3, 4.6, "Hermes", fontsize=13, color=INK, ha="center", fontweight="bold")

ax.plot([5.1, 5.1], [3.9, 7.0], color="#d8d7ce", linewidth=1.5)

ax.text(5, 1.3, "Same advice. More than 6× difference in payoff.", fontsize=13.5, color=INK, ha="center", fontweight="bold")
save(fig, "card4_cheap_model_payoff")

# =====================================================================
# CARD 5 — no agent wins both cost and quality
# =====================================================================
fig, ax = new_fig()
ax.text(5, 9.1, "CHEAPEST ≠ BEST.", fontsize=22, color=INK, ha="center", fontweight="bold")
ax.text(5, 8.25, "54 runs, 3 agents, tokens + a quality rubric:", fontsize=12.5, color=SEC_INK, ha="center")

rows5 = [
    ("Hermes", ORANGE, "cheapest", "lowest quality"),
    ("dsh", AQUA, "mid cost", "highest quality"),
    ("Claude Code", BLUE, "most expensive", "mid quality"),
]
y0 = 6.5
for i, (name, color, cost, qual) in enumerate(rows5):
    y = y0 - i * 1.5
    ax.text(0.6, y, name, fontsize=14.5, color=INK, ha="left", va="center", fontweight="bold")
    ax.text(5.6, y, cost, fontsize=12.5, color=color, ha="center", va="center", fontweight="bold")
    ax.text(8.7, y, qual, fontsize=12.5, color=color, ha="center", va="center", fontweight="bold")

ax.text(5.6, 7.3, "on cost", fontsize=9, color=MUTED, ha="center")
ax.text(8.7, 7.3, "on quality", fontsize=9, color=MUTED, ha="center")

ax.text(5, 0.9, "No agent wins on both at once.", fontsize=14, color=INK, ha="center", fontweight="bold")
save(fig, "card5_no_free_lunch")

print("done: 5 LinkedIn cards")
