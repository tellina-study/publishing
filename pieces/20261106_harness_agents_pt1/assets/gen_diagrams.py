#!/usr/bin/env python3
"""Structural diagrams (not data charts): agent architecture comparison, and
the harness-off vs harness-on process flow. Content is a direct restatement of
ru.md's own prose (sections "Как был устроен эксперимент" and "Чем агенты
отличаются друг от друга") — no new claims are introduced here.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

BLUE = "#2a78d6"
ORANGE = "#eb6834"
AQUA = "#1baf7a"
INK = "#0b0b0b"
SEC_INK = "#52514e"
MUTED = "#898781"
SURFACE = "#fcfcfb"
BOX_FILL = "#ffffff"
BOX_EDGE = "#c3c2b7"

OUT = "/home/harness/harness-projects/256/.worktrees/folder-304/session-c792b49e-e286eed0/pieces/20261106_harness_agents_pt1/assets"


def box(ax, x, y, w, h, text, fill=BOX_FILL, edge=BOX_EDGE, textcolor=INK, fontsize=9.3, weight="normal"):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.06",
                        linewidth=1.1, edgecolor=edge, facecolor=fill, zorder=3)
    ax.add_patch(p)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fontsize,
            color=textcolor, fontweight=weight, wrap=True, zorder=4)
    return p


def arrow(ax, x1, y1, x2, y2, color=MUTED):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=14,
                         linewidth=1.3, color=color, zorder=2)
    ax.add_patch(a)


# =====================================================================
# DIAGRAM D1 — three agents, structurally
# =====================================================================
fig, ax = plt.subplots(figsize=(10.5, 7.1), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)
ax.set_xlim(0, 10.5)
ax.set_ylim(0, 7.1)
ax.axis("off")

cols = [("Claude Code", BLUE, 0.3), ("Hermes", ORANGE, 3.75), ("dsh", AQUA, 7.2)]
col_w = 3.0
row_labels = ["Выбор модели", "Правила", "Инструменты", "Память между шагами"]
row_y = [4.55, 3.35, 2.15, 0.95]
row_h = 0.95

cells = {
    "Claude Code": [
        "флаг командной строки —\nкороткое имя может\nразрешиться в другую\nверсию модели",
        "CLAUDE.md\n(файл правил)",
        "встроенный набор +\nMCP-серверы;\nможет порождать\nсобственных суб-агентов",
        "заметки в рамках\nтекущей задачи",
    ],
    "Hermes": [
        "общий конфигурационный\nфайл, один на все\nсессии агента на машине",
        "файл правил\n(аналог системного\nпромпта)",
        "свой набор\nподключаемых\nинструментов",
        "заметки в рамках\nтекущей задачи",
    ],
    "dsh": [
        "параметр запуска —\nне потребовал\nобхода в этом\nэксперименте",
        "подключается\nплагином",
        "подключаются\nплагинами",
        "подключается\nплагином",
    ],
}

for name, color, x in cols:
    box(ax, x, 5.75, col_w, 0.7, name, fill=color, edge=color, textcolor="#ffffff", fontsize=13, weight="bold")
    for lbl, y, h in zip(row_labels, row_y, [row_h] * 4):
        box(ax, x, y, col_w, h, cells[name][row_labels.index(lbl)], fontsize=8.8)

for lbl, y in zip(row_labels, row_y):
    ax.text(-0.15, y + row_h / 2, lbl, ha="right", va="center", fontsize=10, color=SEC_INK, fontweight="bold")

ax.text(0.3, 6.82, "Три агента — три разных устройства харнеса", fontsize=15, color=INK, fontweight="bold")
fig.savefig(f"{OUT}/d1_agent_architecture.png", bbox_inches="tight", facecolor=SURFACE)
plt.close(fig)
print("wrote d1_agent_architecture")

# =====================================================================
# DIAGRAM D2 — harness off vs harness on, process flow
# =====================================================================
fig, ax = plt.subplots(figsize=(10.5, 5.1), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)
ax.set_xlim(0, 10.5)
ax.set_ylim(0, 5.1)
ax.axis("off")

ax.text(0.2, 4.8, "Без харнеса", fontsize=13, color=INK, fontweight="bold")
off_boxes = ["Формулировка\nзадачи", "Действует сразу:\nоткрывает файлы\nпо наитию, пробует"]
xw = 3.1
xpos = [0.2, 4.0]
for x, t in zip(xpos, off_boxes):
    box(ax, x, 3.8, xw, 0.85, t, fontsize=10)
arrow(ax, xpos[0] + xw, 3.8 + 0.42, xpos[1], 3.8 + 0.42)

ax.text(0.2, 2.95, "С харнесом", fontsize=13, color=INK, fontweight="bold")
ax.text(10.3, 2.95, "+3 шага перед тем, как начать действовать", fontsize=9.3, color=SEC_INK,
        ha="right", va="center", style="italic")
on_boxes = ["Формулировка\nзадачи", "Читает файл\nправил", "Проверяет,\nкакие инструменты\nразрешены", "Сверяется\nс памятью по\nзадаче", "Действует по\nпредписанной\nсхеме"]
n = len(on_boxes)
xw2 = 1.9
gap = 0.18
xpos2 = [0.2 + i * (xw2 + gap) for i in range(n)]
for x, t in zip(xpos2, on_boxes):
    box(ax, x, 1.55, xw2, 1.15, t, fontsize=8.8)
for i in range(n - 1):
    arrow(ax, xpos2[i] + xw2, 1.55 + 0.57, xpos2[i + 1], 1.55 + 0.57)

fig.savefig(f"{OUT}/d2_harness_flow.png", bbox_inches="tight", facecolor=SURFACE)
plt.close(fig)
print("wrote d2_harness_flow")
