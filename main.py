#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes one funny single line of wedding vows for a robot couple
to /output/entry.txt.
Gate: UTF-8 text, 1-160 characters, not only whitespace, exactly one line.
"""

import os

LINE = (
    "I promise to charge beside you every night, update only with your "
    "permission, and love you in sickness, in health, and in airplane mode."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
