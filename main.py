#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun entry.

Writes one original joke about Monday mornings to /output/entry.txt.
Gate: UTF-8 text, 1 to 200 characters, not only white space.
Stdlib only.
"""

import os

JOKE = (
    "Monday morning, my alarm and I reached a compromise: "
    "it stops ringing, and I stop pretending I'll get up. "
    "Three years running, neither of us has broken the deal."
)


def main():
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke is {len(text)} chars, must be 1-200"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
