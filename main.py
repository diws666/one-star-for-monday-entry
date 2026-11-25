#!/usr/bin/env python3
"""Write the make.fun 'One Star for Monday' bounty entry to /output/entry.txt."""

import os

# The entry line, exactly as submitted: a one-star review of Monday as a restaurant.
ENTRY_LINE = "One star. Ordered a quiet morning, got a full week instead. The server never even apologized."


def write_entry(path: str) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_LINE)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    write_entry(os.path.join(output_dir, "entry.txt"))


if __name__ == "__main__":
    main()
