"""Rebuild images/thumbs/ from the full-size photos. Run after adding or removing photos.

The site shows these smaller copies in the photo grids (faster on phones) and opens
the full-size photo in the viewer.
"""
import os
import shutil
from PIL import Image

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "images")
THUMBS = os.path.join(ROOT, "thumbs")

shutil.rmtree(THUMBS, ignore_errors=True)
count = 0
for sub in ("projects", "gallery"):
    for dirpath, _, files in os.walk(os.path.join(ROOT, sub)):
        for name in sorted(files):
            if not name.lower().endswith(".jpg"):
                continue
            src = os.path.join(dirpath, name)
            dst = os.path.join(THUMBS, os.path.relpath(src, ROOT))
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            im = Image.open(src).convert("RGB")
            im.thumbnail((800, 800), Image.LANCZOS)
            im.save(dst, "JPEG", quality=76, optimize=True, progressive=True)
            count += 1
print(f"{count} thumbnails written to {THUMBS}")
