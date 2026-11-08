#!/usr/bin/env python3
"""Compose the AI-generated illustrations for LinkedIn cards 1, 2, 4, 5 with
their text overlay, mirroring card 3's finished recipe (alpha-matted art,
extent sized to the art's true aspect ratio, "Harness" label added as real
text wherever a switch appears in the art, never asked of the image model).
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

G = "/home/harness/harness-projects/256/.worktrees/folder-304/session-c792b49e-e286eed0/pieces/20261106_harness_agents_pt1/linkedin/genart"


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
    fig.savefig(f"{G}/{name}.png", facecolor=SURFACE, bbox_inches="tight", pad_inches=0.3)
    plt.close(fig)
    print("wrote", name)


# =====================================================================
# CARD 1 — quality didn't move
# =====================================================================
fig, ax = new_fig()
ax.text(5, 9.55, "SAME AGENT. HARNESS ON vs OFF.", fontsize=13.5, color=MUTED, ha="center", fontweight="bold")
ax.text(5, 8.75, "One task, 3 agents — the only one\nwhere quality varied at all:", fontsize=12, color=SEC_INK, ha="center")

art, (x0, x1, y0, y1) = art_box(f"{G}/card1_transparent.png", box_w=7.0, cx=5.0, cy=6.0)
ax.imshow(art, extent=[x0, x1, y0, y1], zorder=2)
ax.text(5.0, y0 + 0.78 * (y1 - y0), "Harness", fontsize=13, color=INK, ha="center", va="center", fontweight="bold", zorder=3)

ax.text(5, 3.5, "DeepSeek Harness, Claude Code, Hermes —\nthree different levels, same answer every time.", fontsize=11.5, color=SEC_INK, ha="center")
ax.text(5, 1.4, "Quality didn't move once — for any of the three.", fontsize=13.5, color=INK, ha="center", fontweight="bold")
save(fig, "card1_FINAL")

# =====================================================================
# CARD 2 — run it twice
# =====================================================================
fig, ax = new_fig()
ax.text(5, 9.4, "RUN IT TWICE.", fontsize=20, color=INK, ha="center", fontweight="bold")
ax.text(5, 8.7, "Same task. Same settings. Nothing changed.", fontsize=12, color=SEC_INK, ha="center")

art, (x0, x1, y0, y1) = art_box(f"{G}/card2_transparent.png", box_w=7.6, cx=5.0, cy=6.1)
ax.imshow(art, extent=[x0, x1, y0, y1], zorder=2)

ax.text(2.85, 3.5, "Hermes —\ntwo identical runs", fontsize=10.5, color=SEC_INK, ha="center")
ax.text(7.7, 3.5, "Claude Code's loudest\nharness effect in the test", fontsize=10.5, color=SEC_INK, ha="center")

ax.text(5, 1.4, "The agent's own noise outsized\nthe harness effect we were testing.", fontsize=13, color=INK, ha="center", fontweight="bold")
save(fig, "card2_FINAL")

# =====================================================================
# CARD 4 — bigger isn't always better
# =====================================================================
fig, ax = new_fig()
ax.text(5, 9.4, "SAME ADVICE: “USE THE CHEAPER MODEL.”", fontsize=12.5, color=MUTED, ha="center", fontweight="bold")
ax.text(5, 8.7, "Two agents, same cheap/pricier pair, same tasks:", fontsize=11.5, color=SEC_INK, ha="center")

art, (x0, x1, y0, y1) = art_box(f"{G}/card4_transparent.png", box_w=7.6, cx=5.0, cy=6.2)
ax.imshow(art, extent=[x0, x1, y0, y1], zorder=2)

ax.text(2.85, 3.9, "Claude Code  (÷9)", fontsize=12, color=BLUE, ha="center", fontweight="bold")
ax.text(7.7, 3.9, "Hermes  (÷56)", fontsize=12, color=ORANGE, ha="center", fontweight="bold")

ax.text(5, 2.5, "On the one task we could compare: Claude Code's quality fell\nby half on the cheap model — DeepSeek Harness held full marks.", fontsize=10.5, color=SEC_INK, ha="center")
ax.text(5, 0.9, "Bigger isn't automatically better. Cheaper isn't automatically worse.", fontsize=12, color=INK, ha="center", fontweight="bold")
save(fig, "card4_FINAL")

# =====================================================================
# CARD 5 — zero changes, higher price
# =====================================================================
fig, ax = new_fig()
ax.text(5, 9.4, "ZERO FILES CHANGED.", fontsize=20, color=INK, ha="center", fontweight="bold")
ax.text(5, 8.7, "Same task, same model, for Hermes:", fontsize=12, color=SEC_INK, ha="center")

art, (x0, x1, y0, y1) = art_box(f"{G}/card5_transparent.png", box_w=7.6, cx=5.0, cy=6.3)
ax.imshow(art, extent=[x0, x1, y0, y1], zorder=2)
ax.text(5.0, y0 + 0.82 * (y1 - y0), "Harness", fontsize=12.5, color=INK, ha="center", va="center", fontweight="bold", zorder=3)

ax.text(2.6, 4.1, "without harness", fontsize=10, color=MUTED, ha="center")
ax.text(7.6, 4.1, "with harness", fontsize=10, color=MUTED, ha="center")

ax.text(5, 2.7, "≈4× higher price for the identical\nzero-result outcome", fontsize=12, color=RED, ha="center", fontweight="bold")
ax.text(5, 1.1, "Effort moved. The result didn't.", fontsize=13.5, color=INK, ha="center", fontweight="bold")
save(fig, "card5_FINAL")

print("done")
