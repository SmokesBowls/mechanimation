#!/usr/bin/env python3
"""
Generate placeholder part images for the example rig.
"""
import os
from pathlib import Path
from PIL import Image, ImageDraw

OUT_DIR = Path(__file__).parent / "parts"
OUT_DIR.mkdir(parents=True, exist_ok=True)

parts = {
    "torso.png": (128, 192, (180, 130, 100)),
    "head.png": (64, 64, (200, 180, 160)),
    "left_arm.png": (32, 96, (160, 120, 140)),
    "right_arm.png": (32, 96, (160, 120, 140)),
}

for name, (w, h, color) in parts.items():
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, w, h], fill=color)
    # simple pivot marker
    draw.ellipse([w/2-3, h/2-3, w/2+3, h/2+3], fill=(255,255,255,255))
    img.save(OUT_DIR / name)

print(f"Generated {len(parts)} part images in {OUT_DIR}")
print("Run: python3 primeanim_v4a.py --rig examples/example_rig.json --anim examples/example_anim.json --out examples/output/example_spritesheet.png --size 256")
