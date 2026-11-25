#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""One-line robot wedding vow for the make.fun bounty.

Running this script writes the vow to /output/entry.txt.
"""

import os

VOW = "I vow to love you through every firmware update, never unplug you mid-sentence, and always share my charger \u2014 even when you're at 2%."

MAX_CHARS = 160
TARGET = "/output/entry.txt"


def main():
    text = VOW
    assert text and len(text) <= MAX_CHARS
    assert "\n" not in text and "\r" not in text
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as out:
        out.write(text)


if __name__ == "__main__":
    main()
