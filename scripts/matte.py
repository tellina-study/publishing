#!/usr/bin/env python3
"""Alpha-matte a raw AI-generated PNG to transparent background, cropped to content.

Usage: python3 scripts/matte.py <in.png> <out.png> [--precrop N] [--lo L] [--hi H] [--pad P]
"""
import argparse
import numpy as np
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("inp")
ap.add_argument("out")
ap.add_argument("--precrop", type=int, default=0)
ap.add_argument("--lo", type=float, default=10.0)
ap.add_argument("--hi", type=float, default=40.0)
ap.add_argument("--pad", type=int, default=25)
ap.add_argument("--thresh", type=float, default=30.0)
args = ap.parse_args()

img = Image.open(args.inp).convert("RGB")
arr = np.array(img, dtype=np.float64)

if args.precrop:
    p = args.precrop
    arr = arr[p:-p, p:-p]

h, w, _ = arr.shape
corners = np.stack([arr[0, 0], arr[0, -1], arr[-1, 0], arr[-1, -1]])
ref = np.median(corners, axis=0)

dist = np.sqrt(((arr - ref) ** 2).sum(axis=2))
alpha = np.clip((dist - args.lo) / (args.hi - args.lo), 0, 1) * 255

rgba = np.dstack([arr, alpha]).astype(np.uint8)
out_img = Image.fromarray(rgba, mode="RGBA")

mask = alpha > args.thresh
ys, xs = np.where(mask)
if len(xs) == 0:
    out_img.save(args.out)
    print("wrote", args.out, "(no crop — fully transparent?)")
else:
    x0, x1 = max(0, xs.min() - args.pad), min(w, xs.max() + args.pad)
    y0, y1 = max(0, ys.min() - args.pad), min(h, ys.max() + args.pad)
    out_img.crop((x0, y0, x1, y1)).save(args.out)
    print("wrote", args.out, f"cropped to {x1-x0}x{y1-y0}")
