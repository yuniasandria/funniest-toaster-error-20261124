#!/usr/bin/env python3
"""make.fun entry: The Funniest Toaster Error Message.

Writes one deadpan error line from a kitchen toaster to /output/entry.txt.
Pure standard library; no third-party packages, no network.
"""

import os

PART_A = "E01: Slot 2 is haunted. "
PART_B = "Please use Slot 1."
LINE = PART_A + PART_B
assert LINE == "E01: Slot 2 is haunted. Please use Slot 1."
assert 1 <= len(LINE) <= 120


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
