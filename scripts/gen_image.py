#!/usr/bin/env python3
"""Generic OpenRouter image-generation helper, reused across pieces.

Usage: python3 scripts/gen_image.py <model> <size> <out.png> <<< "prompt text"
   or: python3 scripts/gen_image.py <model> <size> <out.png> "prompt text"
"""
import base64
import json
import os
import sys
import urllib.request

model = sys.argv[1]
size = sys.argv[2]
out_path = sys.argv[3]
prompt = sys.argv[4] if len(sys.argv) > 4 else sys.stdin.read()

key = os.environ.get("OPENROUTER_API_KEY")
if not key:
    sys.exit("OPENROUTER_API_KEY not set in environment")

body = json.dumps({"model": model, "prompt": prompt, "n": 1, "size": size}).encode()
req = urllib.request.Request(
    "https://openrouter.ai/api/v1/images/generations",
    data=body,
    headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    method="POST",
)
with urllib.request.urlopen(req, timeout=180) as resp:
    data = json.load(resp)

b64 = data["data"][0]["b64_json"]
with open(out_path, "wb") as f:
    f.write(base64.b64decode(b64))
print("wrote", out_path)
