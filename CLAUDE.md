# ACMP solutions

Solutions to acmp.ru tasks, one file per task: `NNN.py` (task number zero-padded to 3 digits, e.g. `056.py`).
Some tasks also have solutions in other languages (`.cpp`, `.pas`, `.go`).

## Solving one task (the scheduled routine does exactly this, once per run)

1. Sync: `git fetch origin`. Work on the branch `next_tasks`: check it out from `origin/next_tasks` if it exists, otherwise create it from `origin/main`.
2. Pick the task: `python3 tools/acmp.py next` prints the smallest number > 100 without a `NNN.*` file.
3. Read it: `python3 tools/acmp.py task N`. If it prints `IMAGE:` lines and the statement depends on a picture, download it (`curl -s -o /tmp/img.gif URL`) and look at it.
4. Solve in Python 3 following the code rules below. Test on every example from the statement; add a brute-force check when unsure.
5. Submit: `python3 tools/acmp.py submit N NNN.py` (needs `ACMP_LOGIN` / `ACMP_PASSWORD` in the environment). It prints the verdict row.
   On anything other than `Accepted`, fix and resubmit. If the tool says the submission was not registered, wait ~5 minutes (acmp drops bursts) and retry once.
6. Commit only the accepted file to `next_tasks` with message `NNN` and push it.
7. Batch merge: when `next_tasks` holds 10 new task files compared to `origin/main`:
   - N = number of unique task numbers in the repo (`ls | grep -E '^[0-9]{3,}\.' | sed 's/\..*//' | sort -u | wc -l`);
   - update the count in `README.md` ("There are currently N tasks here"), commit;
   - push the branch as `<N>_tasks`, open a PR titled `<N>`, squash-merge it into `main` (commit message `<N>`), delete `<N>_tasks` and `next_tasks`.
8. Reply with one line: task number and verdict.

## Code rules (priority order)

0. Correct.
1. Fits the time/memory limits. The acmp judge is ~4x slower than a laptop for Python: budget local run time at ≤ 1/4 of the limit; prefer C-level work (`map`, `accumulate`, big-int bit tricks) over Python loops; hardcode a precomputed table when the input space is tiny.
2. Minimal number of characters, not counting whitespace. Keep normal formatting.
3. Everything else.

Formatting:
- Code at top level: no `def solve()`, no `if __name__ == "__main__"`, no comments.
- One statement per line, no `;`.
- Spaces around all binary operators, including inside indexes and slices (`d[2 + n]`, `range(t + 1)`), except `**` (`10**9`).
- A space after commas; no spaces right inside brackets; 4-space indents.
- One-letter variable names.
- Shortest input method (`input()`, `open(0).read().split()`, ...); output with plain `print`.

Known acmp quirks:
- "Округлить до целого" means round half up, not Python's banker's `round()`.
- Floating-point boundary cases: prefer exact arithmetic (`fractions.Fraction`) when a comparison with a tolerance decides the answer.
