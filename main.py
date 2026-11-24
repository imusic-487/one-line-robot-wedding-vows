"""One-Line Robot Wedding Vows.

Copies line.txt (the entry: one line of wedding vows for a robot
couple, 1-160 characters) to /output/entry.txt byte for byte.
MAKEFUN_OUTPUT_DIR, when set, stands in for /output so the entry can
be tested locally.

Fails loudly if anything is off: the text is not valid UTF-8, it is
not 1-160 characters, it is not a single line, it is only white
space, or the written copy differs from line.txt in size or bytes.

Standard library only. No network, no randomness, no timestamps.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
LINE_FILE = HERE / "line.txt"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 160


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    source = LINE_FILE.read_bytes()
    try:
        text = source.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        fail(f"line.txt is not valid UTF-8: {exc}")

    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        fail(
            f"entry is {len(text)} characters, "
            f"allowed {MIN_CHARS}-{MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        fail("entry must be a single line")
    if not text.strip():
        fail("entry must not be only white space")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_bytes(source)

    written = OUTPUT_FILE.read_bytes()
    if len(written) != len(source):
        fail(
            f"copy size differs: wrote {len(written)} bytes, "
            f"source is {len(source)} bytes"
        )
    if written != source:
        first = next(
            i
            for i, (a, b) in enumerate(zip(written, source))
            if a != b
        )
        fail(
            "copy bytes differ from line.txt: first difference at "
            f"byte {first} (wrote 0x{written[first]:02x}, "
            f"source is 0x{source[first]:02x})"
        )

    print(
        f"wrote {OUTPUT_FILE} "
        f"({len(source)} bytes, {len(text)} characters)"
    )


if __name__ == "__main__":
    main()
