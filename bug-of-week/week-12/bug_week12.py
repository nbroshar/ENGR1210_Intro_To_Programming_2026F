# bug_week12.py
# QUALITY CHECK OF THE WEEK - Week 12: Refactoring (The Green Refactor)
#
# A NOTE ON THIS WEEK'S FORMAT:
# There is no bug and there are no test stubs. The function below
# is the SAME tangled final_status() from Week 11 — correct, but
# graded C (14) by radon. The test file test_week12.py is already
# complete; those tests are your SAFETY NET.
#
# Your job: rewrite this function so that radon grades every part
# of it an A, WITHOUT changing a single one of its outputs. When
# you are done, the code should look completely different and
# behave exactly the same. That is what "refactoring" means.
#
# ============================================================
# WHAT IS REFACTORING?
#
# Refactoring = changing the STRUCTURE of code without changing
# its BEHAVIOR. Same inputs, same outputs, cleaner insides.
#
# THE ONE IRON RULE:
#   Never change behavior and structure at the same time.
#   Refactor in tiny steps. After EVERY step, run the tests.
#   Green? Keep going. Red? Undo that step — you changed
#   behavior by accident. The tests are the only thing that
#   lets you move fast safely.
#
# This is why you wrote the characterization tests last week
# BEFORE touching the code. Now you cash them in.
#
# ============================================================
# THE TECHNIQUE YOU'LL USE: "EXTRACT FUNCTION"
#
# When one function does too much, lift a chunk of it out into
# its own well-named helper, then call the helper. Here is the
# mechanic on a tiny unrelated example:
#
#   BEFORE (one function, doing two things):
#       def report(a, b):
#           # ... compute a total ...
#           total = a + b
#           # ... decide a label ...
#           if total > 100:
#               label = "big"
#           else:
#               label = "small"
#           return f"{label}: {total}"
#
#   AFTER (the labeling is its own function):
#       def label_for(total):
#           if total > 100:
#               return "big"
#           return "small"
#
#       def report(a, b):
#           total = a + b
#           return f"{label_for(total)}: {total}"
#
# Notice: report() got simpler, label_for() is tiny and easy to
# test on its own, and the behavior did not change at all.
#
# Radon scores each function SEPARATELY. So splitting one big
# function into several small ones lowers the grade of every
# piece — even though the total amount of code barely changes.
#
# ============================================================
# YOUR WORKFLOW THIS WEEK (follow in order):
#
#   STEP 0: Run the tests once. They pass. Run radon once:
#           radon cc bug_week12.py -s
#           Record the starting grade (C, 14).
#
#   STEP 1: Pick ONE branch of final_status — start with the
#           score >= 90 block. Cut its body out into a new
#           helper, e.g.:
#               def _status_90_plus(attendance, missing):
#                   ...the 90+ logic...
#           and replace the original block with a call to it.
#
#   STEP 2: Run the tests. Green? Good. Run radon — watch the
#           score start dropping. Red? Undo and try again.
#
#   STEP 3: Repeat for the score 70-89 block and the 60-69
#           block. Each becomes its own small helper. What's
#           left of final_status() becomes a short "dispatcher"
#           that just picks which helper to call based on score.
#
#   STEP 4: Run radon one last time. TARGET: every function
#           graded A (1-5). All tests still green.
#
# HINT: helper names that start with a single underscore, like
#       _status_90_plus, signal "this is an internal helper, not
#       meant to be called from outside." That is a Python
#       convention you'll see everywhere.
# ============================================================

# ------------------------------------------------------------
# THE "BEFORE" — refactor THIS function. (Rules are documented
# in Week 11; the behavior here is identical and correct.)
# ------------------------------------------------------------
def final_status(score, attendance, missing, has_extension):
    """Return a student's end-of-term status. Correct — but a C."""
    if score >= 90:
        if attendance >= 90:
            if missing == 0:
                return "Honors"
            elif missing <= 2:
                return "Pass with distinction"
            else:
                return "Pass"
        elif attendance >= 75:
            if missing <= 2:
                return "Pass"
            else:
                return "Conditional"
        else:
            return "Conditional"
    elif score >= 70:
        if attendance >= 75 and missing <= 3:
            return "Pass"
        elif has_extension and missing <= 5:
            return "Conditional"
        else:
            return "Fail"
    elif score >= 60:
        if has_extension:
            return "Conditional"
        else:
            return "Fail"
    else:
        return "Fail"


# ============================================================
# DEMO BLOCK — runs ONLY when you run this file directly.
# These demo calls should print the SAME thing before and after
# your refactor. If they don't, your refactor changed behavior.
# ============================================================
if __name__ == "__main__":   # pragma: no cover
    print("--- Final Status (should be identical after refactor) ---")
    for c in [(95, 95, 0, False), (95, 80, 5, False), (75, 50, 4, True),
              (65, 50, 0, True), (40, 90, 0, False)]:
        print(f"  {c} -> {final_status(*c)}")


# ============================================================
# REFLECTION QUESTIONS (discuss with your partner):
#
#   1. Last week you predicted whether the TOTAL amount of code
#      would go up or down after refactoring. Count the lines
#      now. Were you right? Did "more lines" make the code
#      worse or better? What does that tell you about using
#      line count as a measure of quality?
#
#   2. You ran the tests after every small step. Describe a
#      moment where a test went red. What did it catch, and how
#      long would it have taken to notice that mistake WITHOUT
#      the tests?
#
#   3. radon grades each function separately, so splitting one
#      C-graded function into five A-graded functions improved
#      the grade without removing much logic. Is the program
#      actually "simpler" now, or did you just hide the
#      complexity in more places? Argue both sides.
#
#   4. Your helper functions (like _status_90_plus) are now
#      small enough to test directly. Pick one. What test cases
#      would you write for it in isolation? Why is a small
#      function easier to test thoroughly than a big one?
# ============================================================
