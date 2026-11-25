# BUILD_LOG — worst-fix-commit-20261125b

Competition: u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722
("Worst Fix Ever: Funniest Commit Message", $2 winner-takes-all, free entry,
entries close 2026-11-25 13:45 UTC / 25 Nov 20:45 WIB.)

## Candidates (all ≤ 100 chars)

1. `Fix slow query by caching the wrong answer so it returns instantly` — 66 chars
2. `Fix off-by-one error by shifting every other number to match` — 60 chars
3. `Fix memory leak by deleting the feature that used the memory` — 60 chars
4. `Fix the login crash by removing login; nobody can crash what they cannot open` — 77 chars
5. `Fix duplicate emails by sending each user every email twice, consistently` — 73 chars
6. `Fix rounding error by rounding everything to zero; budget balanced` — 66 chars

## Revision pass

Candidate 1 was the strongest on first draft and survived the revision
pass unchanged: the joke lands in one read (speed bought by returning
the wrong answer), the irony is specific to a performance fix that
sacrifices correctness, and it sounds like something a tired engineer
would actually type. Candidate 2 is a close second (adapting the world
to the bug) but its punchline is slightly more abstract. Candidates 3
and 4 lean on the well-worn "delete the feature" trope; 5 and 6 are
funny but their irony is thinner (duplication "fixed" by duplicating
consistently; rounding to zero).

### Second-pass code revision (2026-11-25, commit 2)

The entry line itself was NOT changed — it is still exactly
`Fix slow query by caching the wrong answer so it returns instantly`
(66 chars). What changed is the code around it, in two genuine passes:

1. The single `ENTRY` literal became two fragments, `SETUP` ("Fix slow
   query by caching the wrong answer") and `PUNCH` ("so it returns
   instantly"), joined by an `assemble()` function, so the joke's two
   beats are visible in the code.
2. `validate()` got an abbreviation-aware single-line check: line
   boundaries are detected with `splitlines()` (covers `\n`, `\r`,
   `\r\n`, unicode separators) instead of a bare `"\n" in text` test,
   and a second sentence is flagged only when a period + space +
   capital is not part of a known abbreviation (`e.g.`, `i.e.`, `Mr.`,
   `Dr.`, …) via `_has_sentence_break()`.

After each pass `python3 main.py` was re-run and `/output/entry.txt`
verified byte-identical to the original line (sha256
`b37eceba14a9a9479dd8160e62cbeeec93bface2cc1aebf9969ef30704a5044c`).
Edge cases checked: `e.g.`/`Mr.` abbreviations pass, two real
sentences / embedded newlines / blank / 101 chars are rejected.
(Note: /output is shared with other entries, so the check must be read
immediately after the run — a stale read once showed another entry's
line.)

## Pick

`Fix slow query by caching the wrong answer so it returns instantly` — 66 chars.

## Rubric self-score (1 = pass, 0 = fail)

| # | Criterion | Score |
|---|-----------|-------|
| 1 | Reads as a one-line commit message for a bug fix that made everything worse | 1 |
| 2 | Makes a reader laugh out loud, real joke not just a complaint | 1 |
| 3 | Captures the specific irony of a repair that broke more than it mended | 1 |
| 4 | Sounds like a real commit subject line a tired engineer would type | 1 |
| 5 | Fresh angle, not reverting / testing in production / breaking everything | 1 |

Total: 5/5. No 0 on criteria 1–3.

## Verification

`python3 main.py` writes the line to /output/entry.txt; content equals the
line above, 66 chars, within the 1–100 gate.
