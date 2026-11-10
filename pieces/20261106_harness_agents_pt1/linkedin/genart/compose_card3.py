#!/usr/bin/env python3
"""Composite the AI-generated gauge illustration (Qwen Image 2.1 Pro) with the
card 3 text overlay — step 2 of the attempt/overlay/review loop.
"""
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

BLUE = "#2a78d6"
ORANGE = "#eb6834"
RED = "#e34948"
INK = "#0b0b0b"
SEC_INK = "#52514e"
MUTED = "#898781"
SURFACE = "#fcfcfb"

HERE = "/home/harness/harness-projects/256/.worktrees/folder-304/session-c792b49e-e286eed0/pieces/20261106_harness_agents_pt1/linkedin/genart"

art_path = sys.argv[1] if len(sys.argv) > 1 else f"{HERE}/card3_attempt1.png"
out_name = sys.argv[2] if len(sys.argv) > 2 else "card3_composed_attempt1"

fig, ax = plt.subplots(figsize=(6, 6), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

ax.text(5, 9.45, "SAME SWITCH. SAME TASK.", fontsize=16, color=MUTED, ha="center", fontweight="bold")
ax.text(5, 8.85, "Flipping the harness ON moved token spend:", fontsize=12, color=SEC_INK, ha="center")

art = mpimg.imread(art_path)
# art is RGBA with a transparent (alpha-matted) background, not a cropped
# flat-color box — this is what makes it sit on a uniform white card
# instead of carrying its own slightly-off background as a visible rectangle.
art_h, art_w = art.shape[0], art.shape[1]
box_w = 6.6
box_h = box_w * art_h / art_w
cx, cy = 5.0, 6.3
x0, x1 = cx - box_w / 2, cx + box_w / 2
y0, y1 = cy - box_h / 2, cy + box_h / 2
ax.imshow(art, extent=[x0, x1, y0, y1], zorder=2)

# "Harness" sits directly above the switch, inside the illustration's own
# empty space (the switch is centered with nothing drawn above it) rather
# than as a separate caption outside the artwork.
ax.text(cx, y0 + 0.75 * box_h, "Harness", fontsize=13.5, color=INK, ha="center", va="center", fontweight="bold", zorder=3)

ax.text(2.5, 3.3, "+333%", fontsize=28, color=RED, ha="center", fontweight="bold")
ax.text(2.5, 2.7, "Claude Code", fontsize=12.5, color=INK, ha="center", fontweight="bold")

ax.text(7.4, 3.3, "−74%", fontsize=28, color=BLUE, ha="center", fontweight="bold")
ax.text(7.4, 2.7, "Hermes", fontsize=12.5, color=INK, ha="center", fontweight="bold")

ax.text(5, 1.5, "Both still scored 0 out of 4 — correct answers either way.", fontsize=11, color=SEC_INK, ha="center")

fig.savefig(f"{HERE}/{out_name}.png", facecolor=SURFACE, bbox_inches="tight", pad_inches=0.3)
plt.close(fig)
print("wrote", f"{HERE}/{out_name}.png")
