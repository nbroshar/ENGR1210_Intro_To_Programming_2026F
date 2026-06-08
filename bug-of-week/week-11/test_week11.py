# test_week11.py
# UNIT TESTS — Week 11: Code Complexity (Characterization Tests)
#
# HOW TO RUN:
#   python -m pytest test_week11.py -v
#
# WITH COVERAGE (do this too — see Step 4 in bug_week11.py):
#   python -m pytest test_week11.py --cov=bug_week11 --cov-report=term-missing
#
# Both files must be in the SAME FOLDER.
#
# ============================================================
# WHAT IS DIFFERENT THIS WEEK
#
# There is no bug. The function is already correct. So every
# test you write should PASS the first time you run it.
#
# That feels strange — why test code that already works? Because
# these are CHARACTERIZATION TESTS. They take a snapshot of what
# the function does today and freeze it. Next week you will tear
# the function apart and rebuild it to be simpler. If your
# rebuild accidentally changes any output, one of these frozen
# tests will turn red and catch the mistake instantly.
#
# Pros write the tests BEFORE refactoring, never after. The
# tests are the seatbelt you put on before driving fast.
#
# THE GOAL: write one test per PATH through final_status(). Use
# coverage to check you got them all. The number of tests you
# need should land close to radon's complexity score (14).
#
# RUNNING TEST CASE CATEGORIES:
#   first | middle | last | missing | edge | boundary | empty
#   | stateful | exception | PATH (one test per branch)
# ============================================================

import pytest
from bug_week11 import final_status


# ============================================================
# WORKED TESTS — fully written. Study how each one targets a
# SPECIFIC path described by the rules in bug_week11.py.
# ============================================================

def test_honors_path():
    """High score, high attendance, nothing missing -> Honors."""
    # PATH: score>=90, attendance>=90, missing==0
    assert final_status(95, 95, 0, False) == "Honors"

def test_failing_score_path():
    """A score below 60 always fails, regardless of everything else."""
    # PATH: the final else (score < 60)
    assert final_status(40, 100, 0, True) == "Fail"


# ============================================================
# STUB 1 — Your turn: the "Pass with distinction" path
#
# Per the rules: score>=90, attendance>=90, and 1-2 missing
# assignments earns "Pass with distinction". Write an assert
# for a student with score 95, attendance 95, and 1 missing.
#
# Test case category: PATH
# ============================================================
def test_pass_with_distinction_path():
    """90+ score, 90+ attendance, a couple missing -> distinction."""
    pass   # TODO: replace with a real assert statement


# ============================================================
# STUB 2 — Your turn: the mid-score "Pass" path
#
# Per the rules: a score of 70-89 with attendance >= 75 AND no
# more than 3 missing earns a plain "Pass". Write an assert for
# score 75, attendance 80, 2 missing, no extension.
#
# Test case category: PATH
# ============================================================
def test_mid_score_pass_path():
    """70-89 score with good attendance and few missing -> Pass."""
    pass   # TODO: replace with a real assert statement


# ============================================================
# STUB 3 — Your turn: the extension-rescues-a-low-score path
#
# Per the rules: a score of 60-69 earns "Conditional" IF the
# student has an extension, otherwise "Fail". Write an assert
# for score 65 WITH an extension (expect "Conditional").
#
# Test case category: PATH
# ============================================================
def test_low_score_with_extension_path():
    """60-69 score with an extension -> Conditional."""
    pass   # TODO: replace with a real assert statement


# ============================================================
# MISSING TEST — Write this one entirely from scratch.
#
# There is NO stub. Write the whole thing: function name,
# docstring, and assert.
#
# What to test: the SCORE BOUNDARY between the failing band and
# the 60-69 band. A score of exactly 60, with no extension,
# should be "Fail" (60-69 without an extension fails). But a
# score of exactly 60 WITH an extension should be "Conditional".
# Capturing both halves of the boundary in one test is good
# practice.
#
# Your test must:
#   1. Assert final_status(60, 80, 0, False) == "Fail"
#   2. Assert final_status(60, 80, 0, True)  == "Conditional"
#
# Category: BOUNDARY + PATH.
# ============================================================

# Write your test here:


# ============================================================
# HOW TO KNOW YOU ARE DONE:
#
# 1. Run: python -m pytest test_week11.py -v
#    All of your tests should PASS (the code is correct).
#
# 2. Run with coverage:
#    python -m pytest test_week11.py --cov=bug_week11 --cov-report=term-missing
#    Add tests for any remaining paths until you reach 100%.
#
# 3. Compare your final test count to radon's score of 14.
#    Close? Good — now you've FELT why complexity is expensive.
#
# Keep this file. Next week's refactor must keep every one of
# these tests green.
# ============================================================
