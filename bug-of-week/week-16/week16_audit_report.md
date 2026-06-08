# Week 16 Capstone — Code Quality Audit Report

**Name(s):** ______________________   **Module audited:** `morse_stats.py`   **Date:** __________

You are the quality engineer for this module. Run all four tools, document what
you find, fix it, and prove it's fixed. Fill in every blank.

---

## 1. Before / After Scoreboard

Run each tool on the **starting** code, record the result, then run it again
after all your fixes and record the **final** result.

| Tool | Command | Before | After (goal) |
|------|---------|--------|--------------|
| pytest | `python -m pytest test_week16.py -v` | ___ passed / ___ failed | all pass |
| coverage | `python -m pytest test_week16.py --cov=morse_stats --cov-report=term-missing` | ______ % | 100% |
| radon | `radon cc morse_stats.py -s` | worst grade: ___ | every function A or B |
| ruff | `ruff check morse_stats.py` | ___ findings | All checks passed! |

---

## 2. Findings Log

One row per problem you found. Severity is your judgment: **High** = wrong
results / crashes, **Med** = will cause bugs later, **Low** = readability only.

| # | Tool that found it | What it found | Where (function / line) | Severity | How you fixed it |
|---|--------------------|---------------|--------------------------|----------|------------------|
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |
| 4 |  |  |  |  |  |
| 5 |  |  |  |  |  |
| 6 |  |  |  |  |  |
| 7 |  |  |  |  |  |
| 8 |  |  |  |  |  |

(Add rows as needed. You should find more ruff items than the table assumes.)

---

## 3. The Two Findings No Tool Named

Some problems no single tool reports outright. Describe how you found each.

**Duplication (DRY):** Which two functions held copy-pasted timing logic? How
did the copies disagree, and which produced a wrong answer?

> ____________________________________________________________________

**Missing validation:** Which function trusted its input? Give an example input
that made it return a confident but wrong number, and describe the guard you
added.

> ____________________________________________________________________

---

## 4. The Coverage Bug

Coverage flagged several untested branches, but only one hid an actual bug.

- The buggy untested branch was: ____________________________________
- It returned ______________ but should have returned ______________
- The test I wrote to expose it: `____________________________________`

One of the OTHER untested branches turned out to be correct. Which one, and
what does that teach you about coverage?

> ____________________________________________________________________

---

## 5. The Refactor

- `classify_message` started at radon grade ______ (score ______).
- After refactoring it was grade ______ (score ______).
- I kept the tests green the whole time:  ☐ yes  ☐ no
- Briefly, how did you break it up?

> ____________________________________________________________________

---

## 6. Sign-off

I confirm all four tools are green at the same time:

- ☐ pytest: all tests pass
- ☐ coverage: 100%
- ☐ radon: every function graded A or B
- ☐ ruff: "All checks passed!"

**Signed:** ______________________

---

### Reflection (a few sentences each — see the questions at the bottom of `morse_stats.py`)

1. Tools vs. judgment:

2. Why refactor correct code:

3. Coverage worth it on correct branches?:

4. Your one-sentence copy-paste rule:

5. Your "definition of done" for the real Morse project:
