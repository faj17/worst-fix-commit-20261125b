"""Worst Fix Ever: Funniest Commit Message — make.fun entry.

The whole entry is a single commit message for a bug fix that made
everything worse: the slow query got "fixed" by caching the wrong
answer, so it now returns instantly — and wrong. The script validates
the line and drops it into /output/entry.txt.

Revision pass: the line is now built from two fragments — the setup
(slow query, caching) and the punch (wrong answer, instantly) — joined
by assemble(), so a reader can see the joke's two beats in the code.
The assembled line is byte-identical to the original draft.
"""

import re
from pathlib import Path

# The commit message itself: one line, exactly 66 characters.
# Kept as two fragments so the joke's setup and punch stay visible:
#   setup  — the slow query and the "fix" (caching)
#   punch  — the cost of that fix (the wrong answer, instantly)
SETUP = "Fix slow query by caching the wrong answer"
PUNCH = "so it returns instantly"


def assemble() -> str:
    """Join the setup and punch into the single commit-message line."""
    return f"{SETUP} {PUNCH}"


ENTRY = assemble()

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 100


# Abbreviations whose trailing period must not count as a sentence break
# when checking that the entry reads as one sentence.
ABBREVIATIONS = frozenset(
    {"e.g", "i.e", "mr", "mrs", "ms", "dr", "vs", "etc", "approx", "no"}
)

# Candidate sentence break: a period followed by a space and a capital.
# Each candidate is then checked against ABBREVIATIONS, because a
# variable-width look-behind cannot express that in one pattern.
SENTENCE_BREAK = re.compile(r"\. (?=[A-Z])")
# The token (letters and internal dots) ending right before a period.
TOKEN_BEFORE_PERIOD = re.compile(r"([A-Za-z][A-Za-z.]*)\.$")


def _has_sentence_break(text: str) -> bool:
    """True if text contains a real sentence break, ignoring abbreviations."""
    for match in SENTENCE_BREAK.finditer(text):
        token = TOKEN_BEFORE_PERIOD.search(text[: match.start() + 1])
        if token is None or token.group(1).lower() not in ABBREVIATIONS:
            return True
    return False


def validate(line: str) -> str:
    """Strip and sanity-check the entry; raise ValueError on bad input.

    Single-line check is abbreviation-aware: it splits on any line
    boundary (\\n, \\r, \\r\\n, unicode separators) and requires exactly
    one line, and it flags a second sentence only when a period + space +
    capital is not part of a known abbreviation — so "e.g. caching" would
    not be misread as two sentences.
    """
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if not text:
        raise ValueError("entry must not be only whitespace")
    lines = text.splitlines()
    if len(lines) != 1:
        raise ValueError("entry must be a single line")
    if _has_sentence_break(text):
        raise ValueError("entry must be a single sentence")
    return text


def main() -> None:
    text = validate(ENTRY)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
