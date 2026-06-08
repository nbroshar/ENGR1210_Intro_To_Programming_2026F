# test_week9.py
# UNIT TESTS — Week 9: Testing Every Path
#
# HOW TO RUN:
#   Open the VS Code terminal (Ctrl+`)
#   Make sure you are in the same folder as bug_week9.py
#   Type: python -m pytest test_week9.py -v
#   Press Enter.
#
# IMPORTANT: test_week9.py and bug_week9.py must be in the
# SAME FOLDER for the import to work. If you get a
# ModuleNotFoundError, check that both files are together.
#
# FIRST TIME SETUP (if not done already):
#   pip install pytest
#   Use 'python -m pytest' to avoid interpreter mismatches.
#
# ============================================================
# YOUR JOB THIS WEEK:
#   Tests 1 and 2 are fully written — study them as models.
#   Tests 3 and 4 are STUBBED — fill in the assert statements.
#   Test 5 is MISSING ENTIRELY — write it from scratch.
#
# ============================================================
# RUNNING TEST CASE CATEGORIES (updated list):
#   first     — first item / lowest input
#   middle    — typical input
#   last      — last item / highest input
#   missing   — input not in the data
#   edge      — unusual but valid (empty list, zero, spaces)
#   boundary  — exact value where behavior changes
#   empty     — empty list, string, or collection
#   stateful  — behavior depends on previous calls
#   exception — input that SHOULD raise or handle an error
#   PATH      — NEW: one test for each branch of an if/elif chain
# ============================================================
#
# ============================================================
# THE BIG IDEA THIS WEEK: ONE TEST PER PATH
#
# A function with five branches needs five tests — one to walk
# down each path. The tests below are organized around that
# rule. Notice how the letter_grade tests deliberately hit
# every band, not just the easy "A" case.
# ============================================================

import pytest
from bug_week9 import class_average, count_passing, letter_grade, shipping_tier


# ============================================================
# TESTS FOR class_average()
# Fully written — read these carefully as your model.
# ============================================================

def test_class_average_typical():
    """A normal list averages correctly."""
    # MIDDLE / happy-path test.
    assert class_average([80, 90, 100]) == 90.0

def test_class_average_empty_list():
    """An empty list should return 0.0, NOT crash."""
    # EMPTY / edge test — this is the one that catches Bug 1.
    # Before the fix, calling class_average([]) raises
    # ZeroDivisionError and this test ERRORS out instead of
    # passing. After you add the empty-list guard, it passes.
    assert class_average([]) == 0.0


# ============================================================
# STUB 1 — Your turn: count_passing() on a typical list
#
# count_passing([90, 80, 55, 70]) has THREE passing scores
# (90, 80, 70) and one failing (55). The correct answer is 3.
# The buggy version (Bug 2) returns 1. Write an assert that
# checks for 3 — it will fail until you fix Bug 2.
#
# Test case category: MIDDLE
# ============================================================
def test_count_passing_typical():
    """A list with three passing scores should count 3."""
    pass   # TODO: replace with a real assert statement


# ============================================================
# STUB 2 — Your turn: letter_grade() in the BROKEN band
#
# The happy-path test letter_grade(95) == "A" passes even with
# Bug 3 present — that is exactly why Bug 3 is sneaky. To catch
# it you must test the path the happy case skips.
#
# A score of 75 is in the 70-79 band and should return "C".
# Write an assert for that. It fails until Bug 3 is fixed.
#
# Test case category: PATH (the branch the obvious test missed)
# ============================================================
def test_letter_grade_c_band():
    """A score of 75 should earn a 'C'."""
    pass   # TODO: replace with a real assert statement


# ============================================================
# MISSING TEST — Write this one entirely from scratch.
#
# There is NO stub. You write the whole thing: function name,
# docstring, and the assert statement(s).
#
# What to test: shipping_tier() at the EXACT boundary value.
# The rule is "10 pounds OR MORE is heavy", so shipping_tier(10)
# must return "heavy". Bug 4 makes it return "standard" instead.
#
# Your test must:
#   1. Call shipping_tier(10).
#   2. Assert the result is "heavy".
#
# BONUS (optional but recommended): add asserts for one value
# in EACH tier — e.g. shipping_tier(1) == "light" and
# shipping_tier(5) == "standard" — so your single test walks
# down every path of the function, not just the broken one.
#
# GUIDANCE:
#   - Name the function starting with  test_
#   - Write a docstring explaining what it checks.
#   - Category: BOUNDARY + PATH (the exact handoff value).
#   - Before fixing Bug 4 this test FAILS; after fixing it,
#     it PASSES.
# ============================================================

# Write your test here:


# ============================================================
# HOW TO KNOW YOU ARE DONE:
#
# Run: python -m pytest test_week9.py -v
#
# You should see:
#   test_class_average_typical        PASSED
#   test_class_average_empty_list     PASSED   <- catches Bug 1
#   test_count_passing_typical        PASSED   <- stub 1 / Bug 2
#   test_letter_grade_c_band          PASSED   <- stub 2 / Bug 3
#   test_shipping_tier_boundary       PASSED   <- your test / Bug 4
#
# All 5 passing = all 4 bugs fixed + all tests written.
# ============================================================
