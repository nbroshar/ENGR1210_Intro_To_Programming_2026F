# test_week15.py
# UNIT TESTS — Week 15: Guard Clauses & Validation
#
# HOW TO RUN:
#   python -m pytest test_week15.py -v
#
# Both files must be in the SAME FOLDER.
#
# ============================================================
# NEW THIS WEEK: TESTING THAT BAD INPUT IS REJECTED
#
# Until now, every test checked that a function RETURNS the right
# value. This week you also test that a function RAISES the right
# error when given bad input. pytest gives you a tool for that:
#
#   with pytest.raises(ValueError):
#       grade_percentage(10, 0)
#
# Read it as: "the code inside this block is EXPECTED to raise a
# ValueError." The test PASSES if a ValueError is raised, and
# FAILS if either nothing is raised (the function returned
# garbage instead) or a different error type comes out.
#
# This is the EXCEPTION test-case category from Week 8, finally
# put to work: an input that SHOULD trigger an error.
#
# RUNNING TEST CASE CATEGORIES:
#   first | middle | last | missing | edge | boundary | empty
#   | stateful | exception | PATH | consistency
# ============================================================

import pytest
from bug_week15 import grade_percentage


# ============================================================
# WORKED TESTS — fully written.
# ============================================================

def test_valid_input_returns_percentage():
    """A normal call returns the correct percentage."""
    # MIDDLE / happy path. 45 out of 50 is 90%.
    assert grade_percentage(45, 50) == 90.0

def test_zero_possible_raises():
    """Zero possible points is invalid and must raise ValueError."""
    # EXCEPTION case. Before you add guards, this FAILS — the
    # function raises ZeroDivisionError (the wrong type) instead
    # of a clean ValueError. After your guard, it passes.
    with pytest.raises(ValueError):
        grade_percentage(45, 0)


# ============================================================
# STUB 1 — Your turn: earned points cannot exceed possible
#
# grade_percentage(60, 50) breaks the contract — you can't earn
# 60 points out of 50. Without a guard, the function silently
# returns 120.0. With your guard, it should raise ValueError.
#
# Write a test using  with pytest.raises(ValueError):  that
# expects grade_percentage(60, 50) to raise. Before your guard,
# this FAILS with "DID NOT RAISE" (the silent-nonsense smell
# caught red-handed). After your guard, it passes.
#
# Test case category: EXCEPTION
# ============================================================
def test_earned_exceeds_possible_raises():
    """Earning more than possible is invalid and must raise ValueError."""
    pass   # TODO: replace with a real pytest.raises block


# ============================================================
# STUB 2 — Your turn: earned points cannot be negative
#
# grade_percentage(-5, 50) is also invalid. Write a test that
# expects it to raise ValueError. (Without a guard it returns
# -10.0, another piece of silent nonsense.)
#
# Test case category: EXCEPTION
# ============================================================
def test_negative_earned_raises():
    """Negative earned points is invalid and must raise ValueError."""
    pass   # TODO: replace with a real pytest.raises block


# ============================================================
# MISSING TEST — Write this one entirely from scratch.
#
# There is NO stub. Write the whole thing: function name,
# docstring, and assert(s).
#
# What to test: the VALID boundaries that must NOT raise. Adding
# guards is only half-right if it also rejects good input. Two
# edge values are perfectly valid and should return real numbers:
#
#   grade_percentage(50, 50)  -> 100.0   (a perfect score is allowed)
#   grade_percentage(0, 50)   -> 0.0     (a zero is allowed)
#
# Your test must assert BOTH of these return the correct value
# (and therefore do NOT raise). This guards against guard clauses
# that are too aggressive — e.g., one that wrongly rejects a
# perfect score because it used > instead of >=.
#
# Category: BOUNDARY (valid edges that must still work).
# ============================================================

# Write your test here:


# ============================================================
# HOW TO KNOW YOU ARE DONE:
#
#   python -m pytest test_week15.py -v   -> all PASS
#
# All green means: valid input still returns the right numbers,
# every kind of bad input is rejected with a clear ValueError,
# and the valid boundaries (0% and 100%) still work.
# ============================================================
