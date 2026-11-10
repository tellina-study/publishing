#!/usr/bin/env python3
"""Compose cards 1, 4, 5 with their new literal-scene art + text overlay.
All three art files are tight RECTANGULAR crops (no alpha matting) — a
per-pixel color-distance matte fights itself on these pastel/gradient
renders (either leaves a visible haze, or eats into pale foreground
fills), so a plain tight crop with a thin cream margin is the reliable
choice; the margin blends acceptably against the near-white card surface.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

BLUE = "#2a78d6"
ORANGE = "#eb6834"
AQUA = "#1baf7a"
RED = "#e34948"
INK = "#0b0b0b"
SEC_INK = "#52514e"
MUTED = "#898781"
SURFACE = "#fcfcfb"

L = "/home/harness/harness-projects/256/.worktrees/folder-304/session-c792b49e-e286eed0/pieces/20261106_harness_agents_pt1/linkedin"
G = f"{L}/genart"


def art_box(art_path, box_w, cx, cy):
    art = mpimg.imread(art_path)
    h, w = art.shape[0], art.shape[1]
    box_h = box_w * h / w
    x0, x1 = cx - box_w / 2, cx + box_w / 2
    y0, y1 = cy - box_h / 2, cy + box_h / 2
    return art, (x0, x1, y0, y1)


def new_fig():
    fig, ax = plt.subplots(figsize=(6, 6), dpi=200)
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    return fig, ax


def save(fig, name):
    fig.savefig(f"{L}/{name}.png", facecolor=SURFACE, bbox_inches="tight", pad_inches=0.3)
    plt.close(fig)
    print("wrote", name)


# =====================================================================
# CARD 1 — quality didn't move (balance scale + switch)
# =====================================================================
fig, ax = new_fig()
ax.text(5, 9.6, "SAME AGENT. HARNESS ON vs OFF.", fontsize=13.5, color=MUTED, ha="center", fontweight="bold")
ax.text(5, 8.85, "One task, 3 agents — the only one\nwhere quality varied at all:", fontsize=12, color=SEC_INK, ha="center")

art, (x0, x1, y0, y1) = art_box(f"{G}/card1_cropped_v4.png", box_w=7.33, cx=5.0, cy=5.75)
ax.imshow(art, extent=[x0, x1, y0, y1], zorder=2)

ax.text(5, 2.75, "DeepSeek Harness, Claude Code, Hermes —\nflip the switch, the scale doesn't move.", fontsize=11.5, color=SEC_INK, ha="center")
ax.text(5, 1.2, "Quality didn't move once — for any of the three.", fontsize=13.5, color=INK, ha="center", fontweight="bold")
save(fig, "card1_quality_flat")

# =====================================================================
# CARD 4 — cheap model, different payoff (price tag + stars)
# =====================================================================
fig, ax = new_fig()
ax.text(5, 9.5, "SAME MOVE: SWITCH TO THE CHEAPER MODEL.", fontsize=11.5, color=MUTED, ha="center", fontweight="bold")
ax.text(5, 8.8, "Two different agents, two different payoffs:", fontsize=11.5, color=SEC_INK, ha="center")

art, (x0, x1, y0, y1) = art_box(f"{G}/card4_cropped_v4.png", box_w=6.2, cx=5.0, cy=5.9)
ax.imshow(art, extent=[x0, x1, y0, y1], zorder=2)

ax.text(2.65, 3.35, "Claude Code\nbill ÷9", fontsize=10.5, color=BLUE, ha="center", fontweight="bold")
ax.text(7.35, 3.35, "DeepSeek Harness\ncheap model only", fontsize=10, color="#3a8f5a", ha="center", fontweight="bold")

ax.text(5, 2.2, "On the one task we could compare before/after: Claude Code's quality\nfell by half on the cheaper model. DeepSeek Harness still scored full marks.", fontsize=9.8, color=SEC_INK, ha="center")
ax.text(5, 0.8, "Bigger isn't automatically better. Cheaper isn't automatically worse.", fontsize=12, color=INK, ha="center", fontweight="bold")
save(fig, "card4_cheap_model")

# =====================================================================
# CARD 5 — zero changes, higher price (price tag + zero checklist)
# =====================================================================
fig, ax = new_fig()
ax.text(5, 9.5, "ZERO FILES CHANGED.", fontsize=20, color=INK, ha="center", fontweight="bold")
ax.text(5, 8.8, "Same task, same model, for Hermes:", fontsize=12, color=SEC_INK, ha="center")

art, (x0, x1, y0, y1) = art_box(f"{G}/card5_raw_v3.png", box_w=4.5, cx=5.0, cy=5.85)
ax.imshow(art, extent=[x0, x1, y0, y1], zorder=2)

ax.text(3.85, 3.25, "price", fontsize=10.5, color=MUTED, ha="center")
ax.text(6.15, 3.25, "result", fontsize=10.5, color=MUTED, ha="center")

ax.text(5, 2.3, "≈4× higher price for the identical\nzero-result outcome — harness off or on", fontsize=11.5, color=RED, ha="center", fontweight="bold")
ax.text(5, 0.9, "Effort moved. The result didn't.", fontsize=13.5, color=INK, ha="center", fontweight="bold")
save(fig, "card5_zero_result")

print("done")
