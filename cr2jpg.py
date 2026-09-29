#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["rawpy", "pillow"]
# ///
"""Convert Canon CR2 raw files to JPG."""
import argparse
from pathlib import Path

import rawpy
from PIL import Image


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("src", type=Path, help="folder with .CR2 files")
    p.add_argument("-o", "--out", type=Path, help="output folder (default: same as src)")
    p.add_argument("-q", "--quality", type=int, default=95)
    p.add_argument("-f", "--force", action="store_true", help="overwrite existing JPGs")
    a = p.parse_args()

    out = a.out or a.src
    out.mkdir(parents=True, exist_ok=True)
    files = sorted(f for f in a.src.iterdir() if f.suffix.lower() == ".cr2")
    if not files:
        p.error(f"no .CR2 files in {a.src}")

    for f in files:
        dst = out / f"{f.stem}.jpg"
        if dst.exists() and not a.force:
            print(f"skip {dst.name} (exists)")
            continue
        with rawpy.imread(str(f)) as raw:
            rgb = raw.postprocess(use_camera_wb=True)
        Image.fromarray(rgb).save(dst, quality=a.quality)
        print(f"{f.name} -> {dst}")


if __name__ == "__main__":
    main()
