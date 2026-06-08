# bug_week13.py
# QUALITY CHECK OF THE WEEK - Week 13: Readability & Style
#
# A NOTE ON THIS WEEK'S FORMAT:
# Like Week 11, there is no behavior bug here. summarize() below
# returns the right answer. But it is written like someone in a
# hurry: junk imports, a terrible variable name, leftover
# variables, and sloppy comparisons. It WORKS and it is UGLY,
# and ugly code is where future bugs move in.
#
# This week you meet a LINTER — a tool that reads your code and
# flags style and safety problems automatically.
#
# ============================================================
# THE TOOL: ruff
#
# ONE-TIME SETUP (in the VS Code terminal):
#     pip install ruff
#
# CHECK YOUR CODE:
#     ruff check bug_week13.py
#
# ruff prints one finding per problem, each with a RULE CODE
# (like F401 or E712), the exact file:line:column, and a short
# explanation. Example of one finding:
#
#     F401 [*] `math` imported but unused
#      --> bug_week13.py:48:8
#     help: Remove unused import: `math`
#
# The [*] means ruff can fix that one automatically.
#
# AUTO-FIX THE SAFE ONES:
#     ruff check bug_week13.py --fix
#
# This will remove unused imports and similar mechanical junk on
# its own. It will NOT make judgment calls for you (like renaming
# a variable) — those you fix by hand. ALWAYS re-run your tests
# after --fix to confirm nothing changed.
#
# ============================================================
# WHAT THE RULE CODES MEAN (the ones you'll hit this week)
#
#   F401  an import you never use — dead weight, delete it
#   F841  a variable you assign but never read — delete it
#   F541  an f-string with no {placeholders} — the f does nothing
#   E741  an "ambiguous" variable name: l, I, or O. Lowercase L
#         looks exactly like the digit 1 in most fonts. Banned.
#   E711  comparing to None with ==   (use 'is None' instead)
#   E712  comparing to True/False with ==   (just use the value)
#
# E711 and E712 are special: they are STYLE warnings that are
# also BUG warnings. "if done == True:" quietly breaks the day
# 'done' holds a truthy value that isn't literally True (like the
# number 5, or a non-empty list). Writing "if done:" is shorter,
# clearer, AND correct in more cases. A linter catching these has
# saved you from a real bug, not just an ugly line.
#
# WHAT ruff WILL NOT CATCH (still YOUR job):
#   - A "magic number" like the bare 60 below. ruff has no idea
#     what 60 means; a human reader doesn't either. A named value
#     (PASSING_SCORE = 60) explains itself.
#   - Whether a name is GOOD. ruff bans 'l', but it is happy with
#     'x', 'data', 'thing'. Choosing names that explain intent is
#     a human skill no tool replaces.
# ============================================================
#
# ============================================================
# YOUR WORKFLOW THIS WEEK (follow in order):
#
#   STEP 1: Run the tests (test_week13.py). They pass. Note the
#           exact output of summarize() for a sample list — you
#           must reproduce it exactly after cleanup.
#   STEP 2: Run  ruff check bug_week13.py.  Read EVERY finding.
#   STEP 3: Run  ruff check bug_week13.py --fix  to clear the
#           mechanical ones. Re-run the tests — still green?
#   STEP 4: Fix the remaining findings by hand (rename 'l',
#           delete dead variables, fix the comparisons). Re-run
#           tests after each change.
#   STEP 5: Goal: ruff reports "All checks passed!" AND every
#           test is still green. Same behavior, readable code.
#   STEP 6 (judgment): ruff is now silent, but the bare 60 is
#           still a mystery number. Improve it with a named
#           constant. Did any tool tell you to? No — that's the
#           part that stays human.
# ============================================================

import math
import json


def summarize(scores):
    """Return a one-line summary of a list of test scores."""
    l = scores                       # E741: 'l' is unreadable
    backup = scores                  # F841: assigned, never used
    if len(l) == 0:
        return f"No scores recorded."   # F541: no placeholders
    total = sum(l)
    average = total / len(l)
    passed = 0
    for score in l:
        if score >= 60:              # magic number — ruff won't flag this
            passed = passed + 1
    everyone_passed = passed == len(l)
    if everyone_passed == True:      # E712: compare-to-True
        flag = " (perfect class!)"
    else:
        flag = ""
    if average == None:              # E711: compare-to-None (also dead)
        average = 0
    return f"Average: {average}, Passed: {passed}/{len(l)}{flag}"


# ============================================================
# DEMO BLOCK — runs ONLY when you run this file directly.
# These should print identically before and after your cleanup.
# ============================================================
if __name__ == "__main__":   # pragma: no cover
    print("--- Score Summary (identical before & after cleanup) ---")
    print("  " + summarize([90, 50, 70]))
    print("  " + summarize([88, 92]))
    print("  " + summarize([]))


# ============================================================
# REFLECTION QUESTIONS (discuss with your partner):
#
#   1. ruff flagged "if everyone_passed == True:" (E712). Build
#      a concrete example where  x == True  and  if x:  would
#      behave DIFFERENTLY. Why is the shorter version not just
#      prettier but safer?
#
#   2. The variable 'l' is legal Python and the code ran fine
#      with it. Why does ruff ban exactly l, I, and O as
#      variable names? Type them next to 1 and 0 in your editor
#      and see for yourself.
#
#   3. ruff fixed several problems automatically with --fix but
#      refused to rename 'l' or delete 'backup' for you. Why is
#      it appropriate for a tool to auto-remove an unused import
#      but NOT to auto-rename a variable? Where is the line
#      between "safe to automate" and "needs a human"?
#
#   4. After ruff went silent, the bare 60 was still there. ruff
#      can't know 60 means "passing". List three other places in
#      code you've written this semester where a bare number
#      would have been clearer as a named value.
# ============================================================
