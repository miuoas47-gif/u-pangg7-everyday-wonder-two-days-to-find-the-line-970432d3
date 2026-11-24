#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

Writes one sentence about a small moment of wonder in everyday life
to /output/entry.txt and prints it. Deterministic: the same line,
every run, no arguments, no input, no network.
"""

import os

LINE = "At noon my shadow sprints ahead of me down the pavement, arriving home before I do."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
