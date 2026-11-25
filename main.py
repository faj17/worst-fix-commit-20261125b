"""Worst Fix Ever: Funniest Commit Message — make.fun entry.

The whole entry is a single commit message for a bug fix that made
everything worse: the slow query got "fixed" by caching the wrong
answer, so it now returns instantly — and wrong. The script validates
the line and drops it into /output/entry.txt.
"""

from pathlib import Path

# The commit message itself: one line, exactly 66 characters.
ENTRY = "Fix slow query by caching the wrong answer so it returns instantly"

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 100


def validate(line: str) -> str:
    """Strip and sanity-check the entry; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text:
        raise ValueError("entry must not be only whitespace")
    return text


def main() -> None:
    text = validate(ENTRY)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
