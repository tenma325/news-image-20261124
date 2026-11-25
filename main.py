#!/usr/bin/env python3
"""Write the entry image for 'Sum up 24 November's world news in one image'.

The program copies the image held in this repository (entry.png, in the
repository root beside this file) to /output/entry.png. It uses only the Python standard library, makes no
network requests, and always writes exactly the same bytes, so two runs
produce identical output.

An alternate destination can be given with the ENTRY_OUTPUT_PATH
environment variable (used only for local testing); by default the
program writes to /output/entry.png as the bounty requires. If /output
cannot be created (for example when running as an unprivileged user on a
developer machine), it falls back to ./output/entry.png.
"""

import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DEFAULT_DEST = "/output/entry.png"


def main() -> int:
    dest = os.environ.get("ENTRY_OUTPUT_PATH", DEFAULT_DEST)
    try:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
    except PermissionError:
        dest = os.path.join(os.getcwd(), "output", "entry.png")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copyfile(SOURCE, dest)
    print(f"Wrote {dest} ({os.path.getsize(dest)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
