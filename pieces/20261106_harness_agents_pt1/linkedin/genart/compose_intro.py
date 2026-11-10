#!/usr/bin/env python3
"""Compose the intro/overview card: where the three agents land on
cost x quality, literally off the article's own summary table."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

BLUE = "#2a78d6"
ORANGE = "#eb6834"
AQUA = "#1baf7a"
INK = "#0b0b0b"
SEC_INK = "#52514e"
MUTED = "#898781"
SURFACE = "#fcfcfb"

L = "/home/harness/harness-projects/256/.worktrees/folder-304/session-c792b49e-e286eed0/pieces/20261106_harness_agents_pt1/linkedin"
G = f"{L}/genart"

fig, ax = plt.subplots(figsize=(6, 6), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

ax.text(5, 9.5, "54 RUNS IN, HERE'S WHERE THEY LAND.", fontsize=13, color=MUTED, ha="center", fontweight="bold")
ax.text(5, 8.8, "Quality vs. token cost, all three agents at once:", fontsize=12, color=SEC_INK, ha="center")

art = mpimg.imread(f"{G}/card_intro_transparent_v1.png")
h, w = art.shape[0], art.shape[1]
box_w = 6.4
box_h = box_w * h / w
cx, cy = 5.0, 5.55
x0, x1 = cx - box_w / 2, cx + box_w / 2
y0, y1 = cy - box_h / 2, cy + box_h / 2
ax.imshow(art, extent=[x0, x1, y0, y1], zorder=2)

ax.text(x0 - 0.35, y0 + 0.12 * box_h, "quality", fontsize=10, color=MUTED, ha="center", rotation=90, zorder=3)
ax.text(x0 + 0.5 * box_w, y0 - 0.25, "tokens spent", fontsize=10, color=MUTED, ha="center", zorder=3)

# dot positions read off the art (fractions of the box, left-right / bottom-top);
# labels sit clear ABOVE each dot, never on top of its fill
ax.text(x0 + 0.44 * box_w, y0 + 0.95 * box_h, "DeepSeek Harness", fontsize=10.5, color=AQUA, ha="center", fontweight="bold", zorder=3)
ax.text(x0 + 0.67 * box_w, y0 + 0.65 * box_h, "Claude Code", fontsize=10.5, color=BLUE, ha="center", fontweight="bold", zorder=3)
ax.text(x0 + 0.21 * box_w, y0 + 0.43 * box_h, "Hermes", fontsize=10.5, color=ORANGE, ha="center", fontweight="bold", zorder=3)

ax.text(5, 1.5, "DeepSeek Harness: less than Claude Code, better than both.", fontsize=11.5, color=SEC_INK, ha="center")
ax.text(5, 0.6, "No clean harness win yet — but an early favorite among the three.", fontsize=12.5, color=INK, ha="center", fontweight="bold")

fig.savefig(f"{L}/card_intro_overview.png", facecolor=SURFACE, bbox_inches="tight", pad_inches=0.3)
plt.close(fig)
print("wrote card_intro_overview.png")
