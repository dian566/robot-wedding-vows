#!/usr/bin/env python3
"""Entry for make.fun: One-Line Robot Wedding Vows."""

from os import makedirs

ENTRY = (
    "I vow to love you through every firmware update, never unplug you mid-sentence, and always share my charger \u2014 even when you're at 2%."
)


def write_entry() -> None:
    """Write the entry to /output/entry.txt, nothing else."""
    if len(ENTRY) > 160 or not ENTRY.strip():
        raise ValueError("entry must be a non-empty line of at most 160 characters")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":  # run as a script
    write_entry()
