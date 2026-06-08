# bug_week9.py
# QUALITY CHECK OF THE WEEK - Week 9: Testing Every Path
# Chapter 11 - Python Crash Course, 3rd Edition
#
# INSTRUCTIONS: This file has 4 issues in it.
# Bug 1: Find with the console error message.
# Bug 2: Find with the VS Code Debugger (F11 Step Into).
# Bug 3: Find with test cases — it hides in a branch you forgot to test.
# Bug 4: Can ONLY be found by a thoughtful boundary test —
#         the unit test file will catch it automatically.
#
# ============================================================
# SOMETHING NEW STARTS THIS WEEK: "IS IT GOOD?"
#
# For eight weeks you asked two questions about your code:
#     1. Does it RUN?     (no crash)
#     2. Is it CORRECT?   (right output for every test case)
#
# Starting now we add a THIRD question:
#     3. Is it GOOD?      (well-tested, readable, easy to change
#                          later without breaking)
#
# A program can run, be correct on the one input you tried, and
# still hide bugs in the paths you never checked. Over the next
# eight weeks you'll learn TOOLS that measure code quality the
# way the debugger measures behavior:
#
#     Week 10: pytest-cov  — measures which lines your tests miss
#     Week 11: radon       — grades how complex a function is (A-F)
#     Week 13: ruff        — flags unreadable / sloppy style
#
# This week you do BY HAND what pytest-cov will do for you
# automatically next week.
# ============================================================
#
# ============================================================
# STANDARD DEBUGGING PROCESS (review):
#   STEP 1: Run — read error type and line number.
#   STEP 2: Fix ONE bug, save, run again.
#   STEP 3: Repeat until no crashes.
#   STEP 4: CHECK YOUR OUTPUT. Running != correct.
#
# VS CODE DEBUGGER (review):
#   Set breakpoint : click gray margin left of line number
#   Start          : F5  ->  Python File
#   Step Into      : F11  (follow execution inside a function)
#   Step Over      : F10  (run current line, pause on next)
#   Continue       : F5
#   Stop           : Shift+F5
#   Variables panel: left sidebar while paused
#
# ============================================================
# NEW THIS WEEK: EVERY BRANCH IS A PATH
#
# Look at this function. How many DIFFERENT ways can it run?
#
#     def sign(n):
#         if n > 0:
#             return "positive"
#         elif n < 0:
#             return "negative"
#         else:
#             return "zero"
#
# Three. Three separate PATHS through the code. A single test —
# say sign(5) — only proves ONE path works. The other two could
# be completely broken and your test would still pass and turn
# green. You would feel safe and be wrong.
#
# THE RULE THIS WEEK:
#   A function with N branches needs (at least) N test cases —
#   one to walk down EACH path. Testing the happy path only is
#   the single most common testing mistake beginners make.
#
# Two of this week's bugs (3 and 4) live in branches that the
# "obvious" test never visits. You will only catch them by
# deliberately testing every path — including the boundaries
# where one branch hands off to the next.
# ============================================================


# ============================================================
# BUG 1 — Find with: console error message (ZeroDivisionError)
#
# class_average() returns the average of a list of scores.
# It works fine for a normal list. But the demo block calls it
# on an EMPTY list, and it crashes. Read the error carefully.
#
# HINT: Read about the 'empty' test-case category (Week 6).
#       What is len([]) ? What happens when you divide by it?
#       A robust function should DECIDE what an empty list means
#       (here: an average of 0.0) and guard against the crash
#       BEFORE doing the division.
# ============================================================
def class_average(scores):
    """Return the average of a list of scores (0.0 if empty)."""
    total = sum(scores)
    return total / len(scores)   # BUG 1: crashes when scores is empty


# ============================================================
# BUG 2 — Find with: VS Code Debugger (F11 Step Into)
#
# count_passing() should count how many scores are 60 or above.
# It runs without crashing, but the number it returns is wrong —
# it never counts higher than 1.
#
# DEBUGGER INSTRUCTIONS:
#   1. Set a breakpoint on the line: if score >= 60:
#   2. Press F5, then F11 to Step Into count_passing().
#   3. In the Variables panel, watch 'count' as you Step Over
#      (F10) each time through the loop.
#   4. Each time a passing score is found, what does 'count'
#      become? Is it ADDING to the running total, or being
#      RESET every time?
#
# HINT: Read about accumulating a count in a loop (Week 3).
#       Compare  count = 1  with  count += 1.
#       One of them throws away everything counted so far.
# ============================================================
def count_passing(scores):
    """Count how many scores are passing (60 or above)."""
    count = 0
    for score in scores:
        if score >= 60:
            count = 1            # BUG 2: should be count += 1
    return count


# ============================================================
# BUG 3 — Find with: TEST CASES (test the path you skipped)
#
# letter_grade() converts a numeric score to a letter A-F.
# Run the demo: letter_grade(95) returns "A". Looks perfect.
# So you might stop testing there. DON'T.
#
# This function has FIVE branches — five paths. Test ONE score
# in each band:
#
#   | score | band   | Expected | Actual |
#   |-------|--------|----------|--------|
#   |  95   | 90+    |   "A"    |        |
#   |  85   | 80-89  |   "B"    |        |
#   |  75   | 70-79  |   "C"    |        |   <- check this one!
#   |  65   | 60-69  |   "D"    |        |
#   |  40   | < 60   |   "F"    |        |
#
# HINT: One branch returns the wrong letter. The happy-path
#       test (95 -> "A") sails right past it. Only walking down
#       EVERY path reveals which band is broken.
# ============================================================
def letter_grade(score):
    """Return the letter grade for a numeric score (0-100)."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "B"               # BUG 3: the 70-79 band should be "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# ============================================================
# BUG 4 — Find with: UNIT TESTS (test_week9.py catches this)
#
# shipping_tier() sorts an order into a shipping band by weight.
# The rule: 10 pounds OR MORE is "heavy".
# The function runs and looks right for 3 lbs, 5 lbs, 20 lbs...
# but it is wrong at ONE specific value.
#
# HINT: Read about the 'boundary' test-case category (Week 6).
#       The bug is the exact same family as the Week 6 discount
#       bug and the Week 5 honor-roll bug: the difference
#       between  > 10  and  >= 10  at the exact value 10.
#       What does shipping_tier(10) return? What SHOULD it
#       return for "10 or more"?
# ============================================================
def shipping_tier(weight):
    """Return shipping tier by weight in pounds."""
    if weight > 10:              # BUG 4: should be >= 10 ("10 or more")
        return "heavy"
    elif weight >= 2:
        return "standard"
    else:
        return "light"


# ============================================================
# DEMO BLOCK — runs ONLY when you run this file directly.
# (The __main__ guard from Week 7, so the test file can import
#  these functions without running the buggy demos.)
# ============================================================
if __name__ == "__main__":

    # --- Bug 1 demo: crashes on an empty list ---
    print("--- Class Average ---")
    print(f"  Average of [80, 90, 100]: {class_average([80, 90, 100])}")
    print(f"  Average of []:            {class_average([])}")   # crash here

    # --- Bug 2 demo: the count never climbs past 1 ---
    print("\n--- Count Passing ---")
    print(f"  Passing in [90, 80, 55, 70]: {count_passing([90, 80, 55, 70])}")

    # --- Bug 3 demo: only the 'A' path looks right ---
    print("\n--- Letter Grades ---")
    for s in [95, 85, 75, 65, 40]:
        print(f"  Score {s} -> {letter_grade(s)}")

    # --- Bug 4 demo: the boundary value is mis-sorted ---
    print("\n--- Shipping Tiers ---")
    for w in [1, 5, 10, 20]:
        print(f"  {w} lb -> {shipping_tier(w)}")


# ============================================================
# REFLECTION QUESTIONS (discuss with your partner):
#
#   1. Bug 1: An empty list is a classic 'edge' input. Why do
#      empty collections cause so many real-world crashes? Name
#      another everyday situation (a function you've written
#      this semester) where an empty input could break things.
#
#   2. Bug 3: The test letter_grade(95) -> "A" passed even
#      though the function was broken. In your own words, what
#      does it mean to say a passing test gave you "false
#      confidence"? How many test cases would you need to feel
#      truly sure letter_grade() is correct?
#
#   3. Bug 4: This was an off-by-one at a boundary — the same
#      shape of bug you've now seen in Weeks 5, 6, and 9. Why
#      do you think the exact boundary value is SO much more
#      likely to be wrong than a value in the middle of a band?
#
#   4. Looking ahead: This week you hunted for untested paths by
#      reading the code and counting branches by hand. Next week
#      a tool (pytest-cov) will color every line your tests
#      DON'T run bright red. Why might a machine be better than
#      a human at noticing "you never tested this line"?
# ============================================================
