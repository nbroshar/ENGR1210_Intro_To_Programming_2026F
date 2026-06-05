# test_week8.py
# UNIT TESTS — Files and Exceptions
#
# HOW TO RUN:
#   Open the VS Code terminal (Ctrl+`)
#   Make sure you are in the same folder as bug_week8.py
#   Type: python -m pytest test_week8.py -v
#   Press Enter.
#
# IMPORTANT: test_week8.py and bug_week8.py must be in the
# SAME FOLDER for the import to work. If you get a
# ModuleNotFoundError, check that both files are together.
#
# FIRST TIME SETUP (if not done in Week 7):
#   pip install pytest
#   Verify: pytest --version
#   Use 'python -m pytest' to avoid interpreter mismatches.
#
# ============================================================
# YOUR JOB THIS WEEK:
#   Tests 1 and 2 are fully written — study them as models.
#   Tests 3, 4, and 5 are STUBBED — fill in the assert statements.
#   Test 6 is MISSING ENTIRELY — write it from scratch.
#
# ============================================================
# RUNNING TEST CASE CATEGORIES (updated list):
#   first     — first item / lowest input
#   middle    — typical input
#   last      — last item / highest input
#   missing   — input not in the data
#   edge      — unusual but valid (empty string, zero, spaces)
#   boundary  — exact value where behavior changes
#   empty     — empty list, string, or file
#   stateful  — behavior depends on previous calls (Week 7)
#   exception — input that SHOULD raise or handle an error
# ============================================================

# ============================================================
# IMPORTS
# (Reminder: full import coverage comes later in the course.
#  These two lines are required boilerplate for the test file.)
#
# import pytest
#   Makes pytest's testing machinery available. You won't call
#   it directly — 'python -m pytest' uses it automatically.
#   pytest is NOT standard library — install it once with:
#   pip install pytest
#
# from bug_week8 import ...
#   Pulls specific functions from bug_week8.py into this file
#   so the tests can call them. Both files must be in the
#   same folder for this to work.
#   If you add a new testable function to bug_week8.py,
#   add its name to this list too.
# ============================================================
import pytest
from bug_week8 import parse_score_line


# ============================================================
# NOTE ON WHAT WE CAN TEST THIS WEEK
#
# parse_score_line() is the only function in bug_week8.py
# that is PURE — it takes input and returns output without
# touching files, network, or global state. Pure functions
# are the easiest to unit test.
#
# Functions like read_course_list(), load_scores(), and
# save_score() touch the file system, which makes them
# harder to test in isolation. Testing file I/O properly
# requires "mocking" — a technique we'll cover when we
# reach Chapter 11. For now, those are tested manually
# using the test case log in bug_week8.py.
#
# This is an important real-world lesson:
#   The EASIER a function is to unit test, the BETTER
#   it is designed. Functions that do one thing and
#   return a value are always easier to test than
#   functions that do many things and touch the outside world.
# ============================================================


# ============================================================
# TESTS FOR parse_score_line()
# Fully written — read these carefully as your model.
# ============================================================

def test_parse_score_line_typical():
    """A clean 'name: score' line parses correctly."""
    # MIDDLE test case — the happy path, clean input.
    # Verifies both the name string and the integer score.
    name, score = parse_score_line("alice: 95")
    assert name  == "alice"
    assert score == 95

def test_parse_score_line_returns_integer_score():
    """Score in the returned tuple must be an int, not a string."""
    # TYPE test case — a subtle but important check.
    # int("95") == 95 is True, but type matters downstream
    # when you do math with the score. This test catches
    # a function that forgets to call int() on the score.
    _, score = parse_score_line("bob: 82")
    assert isinstance(score, int)


# ============================================================
# STUB 1 — Your turn: test with leading whitespace on the name
#
# What should parse_score_line(" alice: 95") return?
# (Note the space before "alice")
# The name in the result should be "alice", not " alice".
#
# Write an assert that catches the whitespace bug.
# After fixing Bug 4, this test should pass.
#
# Test case category: EDGE (leading whitespace)
# ============================================================
def test_parse_score_line_leading_whitespace_on_name():
    """ ' alice: 95' should return name 'alice' without the space."""
    pass   # TODO: replace with a real assert statement


# ============================================================
# STUB 2 — Your turn: test with trailing whitespace on the score
#
# What should parse_score_line("alice: 95 ") return?
# (Note the trailing space after 95)
# The score should still be the integer 95.
# Without .strip(), int(" 95 ") raises a ValueError.
#
# Write an assert that verifies the score is still 95.
#
# Test case category: EDGE (trailing whitespace)
# ============================================================
def test_parse_score_line_trailing_whitespace_on_score():
    """'alice: 95 ' should return score 95 despite trailing space."""
    pass   # TODO: replace with a real assert statement


# ============================================================
# STUB 3 — Your turn: test with double space after the colon
#
# What should parse_score_line("alice:  95") return?
# (Note two spaces between colon and score)
# The score should still be the integer 95.
#
# Write an assert that verifies this edge case.
#
# Test case category: EDGE (extra internal whitespace)
# ============================================================
def test_parse_score_line_double_space_after_colon():
    """'alice:  95' (double space) should still return score 95."""
    pass   # TODO: replace with a real assert statement


# ============================================================
# MISSING TEST — Write this one entirely from scratch.
#
# There is NO stub for this test. You must write the whole
# thing: function name, docstring, and assert statement(s).
#
# What to test:
#   parse_score_line() with a MINIMUM boundary score of 0.
#   A student who scored zero is still a valid entry.
#   The function should return ("diana", 0) for "diana: 0".
#
# Your test must:
#   1. Call parse_score_line() with a zero score.
#   2. Assert the name is correct.
#   3. Assert the score is the INTEGER 0 — not the string "0".
#   4. Assert that isinstance(score, int) is True.
#
# Why this matters:
#   Zero is a classic edge/boundary value.
#   Some buggy implementations treat 0 as falsy and skip it.
#   In Python: if score: will be False when score == 0,
#   which can cause a zero score to be silently ignored.
#   A unit test catches this before it reaches a grade book.
#
# Test case category: BOUNDARY + EDGE (zero as a valid score)
#
# After you write this test, make sure it PASSES with your
# fixed version of parse_score_line().
# ============================================================

# Write your test here:


# ============================================================
# HOW TO KNOW YOU ARE DONE:
#
# Run: python -m pytest test_week8.py -v
#
# You should see:
#   test_parse_score_line_typical                    PASSED
#   test_parse_score_line_returns_integer_score      PASSED
#   test_parse_score_line_leading_whitespace_on_name PASSED  ← stub 1
#   test_parse_score_line_trailing_whitespace_score  PASSED  ← stub 2
#   test_parse_score_line_double_space_after_colon   PASSED  ← stub 3
#   test_parse_score_line_zero_score                 PASSED  ← your test
#
# All 6 passing = Bug 4 is fixed + all tests written.

