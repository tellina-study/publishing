#!/usr/bin/env python3
"""5 standalone LinkedIn stat cards for the harness-agents-pt1 series.
Square-ish (1200x1200), big hero numbers, minimal supporting text — built to
read unambiguously with zero surrounding article context. Every number here
is copied from the already fact-checked ru.md/en.md — nothing re-derived.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

BLUE = "#2a78d6"      # Claude Code
ORANGE = "#eb6834"    # Hermes
AQUA = "#1baf7a"      # DeepSeek Harness
RED = "#e34948"
INK = "#0b0b0b"
SEC_INK = "#52514e"
MUTED = "#898781"
SURFACE = "#fcfcfb"
GOOD = "#0ca30c"

# Darker, text-safe variants of AQUA/ORANGE — the raw marker hues above read
# fine as large hero numbers or fills, but fail WCAG contrast (~2.8:1 / 3.2:1
# against SURFACE) at body-text sizes. Use these two whenever the color sits
# on actual words rather than a big number or a filled shape.
AQUA_TEXT = "#0e7a52"
ORANGE_TEXT = "#a8431c"

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


def toggle(ax, cx, y, on, color, width=1.1, height=0.46):
    """A single on/off toggle switch, centered at (cx, y).

    Same color for OFF and ON — only the fill changes (outline = off, solid =
    on), mirroring the article's own convention (color = agent, fill =
    harness on, outline = harness off). A grey-vs-color track would make
    every agent's OFF state look identical instead of carrying its identity.
    """
    x0 = cx - width / 2
    boxstyle = f"round,pad=0,rounding_size={height / 2}"
    if on:
        track = mpatches.FancyBboxPatch(
            (x0, y - height / 2), width, height, boxstyle=boxstyle,
            linewidth=0, facecolor=color, zorder=3,
        )
    else:
        track = mpatches.FancyBboxPatch(
            (x0, y - height / 2), width, height, boxstyle=boxstyle,
            linewidth=2.4, edgecolor=color, facecolor=SURFACE, zorder=3,
        )
    ax.add_patch(track)
    knob_r = height / 2 - 0.06
    knob_x = x0 + width - height / 2 if on else x0 + height / 2
    knob_color = "white" if on else color
    knob = mpatches.Circle((knob_x, y), knob_r, facecolor=knob_color, edgecolor="none", zorder=4)
    ax.add_patch(knob)


def toggle_pair(ax, cx, y, color, label_above=None):
    """OFF -> arrow -> ON, centered at cx."""
    if label_above:
        ax.text(cx, y + 0.62, label_above, fontsize=8.5, color=MUTED, ha="center")
    toggle(ax, cx - 0.95, y, on=False, color=color)
    ax.text(cx, y, "→", fontsize=15, color=MUTED, ha="center", va="center")
    toggle(ax, cx + 0.95, y, on=True, color=color)


# =====================================================================
# CARD 1 — quality didn't move (relative ranking, no raw small-n counts)
# =====================================================================
fig, ax = new_fig()
ax.text(5, 9.1, "SAME AGENT. HARNESS ON vs OFF.", fontsize=14.5, color=MUTED, ha="center", fontweight="bold")
ax.text(5, 8.2, "One task, 3 agents — the only one\nwhere quality varied at all:", fontsize=12.5, color=SEC_INK, ha="center")

ax.text(3.4, 7.15, "without harness", fontsize=9, color=MUTED, ha="center")
ax.text(6.6, 7.15, "with harness", fontsize=9, color=MUTED, ha="center")

rows = [
    ("DeepSeek Harness", AQUA_TEXT, "full marks", "full marks"),
    ("Claude Code", BLUE, "partial", "partial"),
    ("Hermes", ORANGE_TEXT, "zero", "zero"),
]
y0 = 6.6
for i, (name, color, wo, w) in enumerate(rows):
    y = y0 - i * 1.8
    ax.text(5, y, name, fontsize=14.5, color=INK, ha="center", va="center", fontweight="bold")
    yv = y - 0.72
    ax.text(3.4, yv, wo, fontsize=14, color=color, ha="center", va="center", fontweight="bold")
    ax.text(5, yv, "=", fontsize=16, color=MUTED, ha="center", va="center")
    ax.text(6.6, yv, w, fontsize=14, color=color, ha="center", va="center", fontweight="bold")

ax.text(5, 0.9, "Quality didn't move once — for any of the three.", fontsize=13, color=INK, ha="center", fontweight="bold")
save(fig, "card1_quality_flat")

# =====================================================================
# CARD 2 — agent noise bigger than the harness signal (unchanged)
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
# CARD 3 — mirror effect on the same switch, with an actual toggle
# =====================================================================
fig, ax = new_fig()
ax.text(5, 9.3, "SAME SWITCH. SAME TASK.", fontsize=16, color=MUTED, ha="center", fontweight="bold")
ax.text(5, 8.45, "Flipping the harness ON moved token spend:", fontsize=12, color=SEC_INK, ha="center")

toggle_pair(ax, 3, 7.15, BLUE, label_above="harness")
toggle_pair(ax, 7.3, 7.15, ORANGE, label_above="harness")

ax.text(3, 5.7, "+333%", fontsize=36, color=RED, ha="center", fontweight="bold")
ax.text(3, 4.75, "Claude Code", fontsize=13, color=INK, ha="center", fontweight="bold")

ax.text(7.3, 5.7, "−74%", fontsize=36, color=BLUE, ha="center", fontweight="bold")
ax.text(7.3, 4.75, "Hermes", fontsize=13, color=INK, ha="center", fontweight="bold")

ax.plot([5.1, 5.1], [4.1, 7.9], color="#d8d7ce", linewidth=1.5)

ax.text(5, 2.9, "Correct answers either way: 0 out of 4.\nFor both agents.", fontsize=12.5, color=SEC_INK, ha="center")
ax.text(5, 1.1, "One switch. Opposite reactions. Same outcome.", fontsize=13.5, color=INK, ha="center", fontweight="bold")
save(fig, "card3_mirror_effect")

# =====================================================================
# CARD 4 — cheaper model: savings differ hugely, quality isn't automatic
# =====================================================================
fig, ax = new_fig()
ax.text(5, 9.25, "SAME ADVICE: “USE THE CHEAPER MODEL.”", fontsize=13, color=MUTED, ha="center", fontweight="bold")
ax.text(5, 8.5, "Two agents, same cheap/pricier pair, same tasks:", fontsize=11.5, color=SEC_INK, ha="center")

ax.text(3, 6.9, "÷9", fontsize=46, color=BLUE, ha="center", fontweight="bold")
ax.text(3, 5.85, "Claude Code", fontsize=12.5, color=INK, ha="center", fontweight="bold")

ax.text(7.3, 6.9, "÷56", fontsize=46, color=ORANGE, ha="center", fontweight="bold")
ax.text(7.3, 5.85, "Hermes", fontsize=12.5, color=INK, ha="center", fontweight="bold")

ax.plot([5.1, 5.1], [5.3, 7.9], color="#d8d7ce", linewidth=1.5)

ax.text(5, 4.3, "Quality on the one task we could compare\nbefore → after the switch:", fontsize=10.5, color=SEC_INK, ha="center")
ax.text(3, 3.1, "full → half", fontsize=15, color=BLUE, ha="center", fontweight="bold")
ax.text(3, 2.45, "Claude Code", fontsize=9.5, color=MUTED, ha="center")
ax.text(7.3, 3.25, "full marks\n(cheap model only)", fontsize=12, color=AQUA_TEXT, ha="center", fontweight="bold")
ax.text(7.3, 2.45, "DeepSeek Harness", fontsize=9.5, color=MUTED, ha="center")

ax.text(5, 0.6, "Bigger isn't automatically better. Cheaper isn't automatically worse.", fontsize=12, color=INK, ha="center", fontweight="bold")
save(fig, "card4_cheap_model")

# =====================================================================
# CARD 5 — effort vs outcome: zero files changed, still cost more
# =====================================================================
fig, ax = new_fig()
ax.text(5, 9.25, "ZERO FILES CHANGED.", fontsize=22, color=INK, ha="center", fontweight="bold")
ax.text(5, 8.4, "Same task, same model, for Hermes:", fontsize=12.5, color=SEC_INK, ha="center")

toggle_pair(ax, 5, 6.95, ORANGE, label_above="harness")

ax.text(3, 5.5, "0 files", fontsize=22, color=MUTED, ha="center", fontweight="bold")
ax.text(3, 4.75, "without harness", fontsize=10, color=MUTED, ha="center")

ax.text(7, 5.5, "0 files", fontsize=22, color=MUTED, ha="center", fontweight="bold")
ax.text(7, 4.75, "with harness", fontsize=10, color=MUTED, ha="center")

ax.text(5, 3.3, "≈4×", fontsize=40, color=RED, ha="center", fontweight="bold")
ax.text(5, 2.3, "higher price for the identical\nzero-result outcome", fontsize=11, color=SEC_INK, ha="center")

ax.text(5, 0.7, "Effort moved. The result didn't.", fontsize=13.5, color=INK, ha="center", fontweight="bold")
save(fig, "card5_zero_result")

print("done: 5 LinkedIn cards")
