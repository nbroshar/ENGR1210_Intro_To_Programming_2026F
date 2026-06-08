# test_week10.py
# UNIT TESTS — Week 10: Test Coverage
#
# HOW TO RUN (plain, no coverage):
#   python -m pytest test_week10.py -v
#
# HOW TO RUN WITH COVERAGE (the point of this week):
#   python -m pytest test_week10.py --cov=bug_week10 --cov-report=term-missing
#   python -m pytest test_week10.py --cov=bug_week10 --cov-report=html
#
# (One-time setup if you haven't: pip install pytest-cov)
#
# Both files must be in the SAME FOLDER.
#
# ============================================================
# WHAT MAKES THIS WEEK DIFFERENT
#
# The two tests below PASS. If you stopped here, you'd think the
# discount function was done. Run them WITH coverage and you'll
# discover that two whole branches of get_discount() have never
# been run by any test — not even once. Your job is to close
# that gap, and in doing so, expose the bug hiding in it.
#
# RUNNING TEST CASE CATEGORIES:
#   first | middle | last | missing | edge | boundary | empty
#   | stateful | exception | PATH (one test per branch)
# ============================================================

import pytest
from bug_week10 import get_discount


# ============================================================
# STARTER TESTS — fully written. They PASS. They are also
# INCOMPLETE. Run them with --cov-report=term-missing and read
# the "Missing" column before you write anything.
# ============================================================

def test_gold_under_65():
    """A Gold member under 65 gets 20% off."""
    # This walks the Gold -> (age < 65) path. One branch covered.
    assert get_discount("Gold", 40) == 0.20

def test_non_member():
    """A shopper with no recognized membership gets 0% off."""
    # This walks the 'else' (non-member) path. Two branches now
    # covered... but the function has FOUR. Which two are missing?
    assert get_discount("Bronze", 30) == 0.00


# ============================================================
# STUB 1 — Your turn: cover the SILVER branch
#
# Run the coverage report. One of the "Missing" lines is the
# Silver return. Write a test that calls get_discount with a
# Silver membership and asserts the rate is 0.10.
#
# Expected: this branch is correct, so once you test it, it
# PASSES — and your coverage goes up. (Not every untested line
# hides a bug. But you can't know that until you test it.)
#
# Test case category: PATH (the Silver branch)
# ============================================================
def test_silver_member():
    """A Silver member gets 10% off."""
    pass   # TODO: replace with a real assert statement


# ============================================================
# STUB 2 — Your turn: cover the SENIOR GOLD branch
#
# The other "Missing" line is the senior-Gold return. Write a
# test for a Gold member who is 70 years old. Per the rules at
# the top of bug_week10.py, a Gold senior should get 30% off,
# so assert the rate is 0.30.
#
# Expected: this test FAILS at first. That failure IS the bug —
# the branch you never tested was returning the wrong number.
# Read the pytest failure message: it shows you what the
# function returned vs. what you expected. Then go fix the bug
# in bug_week10.py and re-run.
#
# Test case category: PATH (the senior-Gold branch — the one
#                     with the bug)
# ============================================================
def test_gold_senior():
    """A Gold member aged 70 should get 30% off."""
    pass   # TODO: replace with a real assert statement


# ============================================================
# MISSING TEST — Write this one entirely from scratch.
#
# There is NO stub. Write the whole thing: function name,
# docstring, and assert.
#
# What to test: the BOUNDARY between "Gold under 65" and "Gold
# senior". The rule says senior is "65 OR OLDER", so a Gold
# member who is exactly 65 should get the senior rate: 0.30.
#
# This is the value most likely to be wrong, and it is the kind
# of test coverage alone can't tell you to write — you have to
# think about the boundary yourself. (Coverage would count age
# 70 and age 65 as the "same" branch, so 100% coverage would
# NOT guarantee you tested the boundary. This is the limit of
# the tool, and the reason human test design still matters.)
#
# Your test must:
#   1. Call get_discount("Gold", 65).
#   2. Assert the result is 0.30.
#
# Category: BOUNDARY + PATH.
# ============================================================

# Write your test here:


# ============================================================
# HOW TO KNOW YOU ARE DONE:
#
# Run: python -m pytest test_week10.py --cov=bug_week10 --cov-report=term-missing -v
#
# You should see all 5 tests PASSED and:
#
#     Name            Stmts   Miss  Cover   Missing
#     ---------------------------------------------
#     bug_week10.py       8      0   100%
#
# All 5 passing + 100% coverage = bug fixed AND every branch
# tested. Green code AND a green report.
# ============================================================
