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

ax.text(5, 9.4, "SAME SWITCH. SAME TASK.", fontsize=16, color=MUTED, ha="center", fontweight="bold")
ax.text(5, 8.75, "Flipping the harness ON moved token spend:", fontsize=12, color=SEC_INK, ha="center")

art = mpimg.imread(art_path)
ax.imshow(art, extent=[1.2, 8.8, 4.667, 7.933], zorder=2)

ax.text(2.5, 3.6, "+333%", fontsize=28, color=RED, ha="center", fontweight="bold")
ax.text(2.5, 3.0, "Claude Code", fontsize=12.5, color=INK, ha="center", fontweight="bold")

ax.text(7.4, 3.6, "−74%", fontsize=28, color=BLUE, ha="center", fontweight="bold")
ax.text(7.4, 3.0, "Hermes", fontsize=12.5, color=INK, ha="center", fontweight="bold")

ax.text(5, 1.9, "Both still scored 0 out of 4 — correct answers either way.", fontsize=11, color=SEC_INK, ha="center")

fig.savefig(f"{HERE}/{out_name}.png", facecolor=SURFACE, bbox_inches="tight", pad_inches=0.3)
plt.close(fig)
print("wrote", f"{HERE}/{out_name}.png")
