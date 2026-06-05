# test_week7.py
# UNIT TESTS — Week 7
#
# FIRST TIME SETUP — run this ONE TIME in the VS Code terminal:
#   pip install pytest
#
#   Then to run tests:
#       python -m pytest test_week7.py -v
#
# Using 'python -m pytest' instead of just 'pytest' avoids
# the interpreter mismatch problem in VS Code.
#
# HOW TO RUN THESE TESTS:
#   Open the VS Code terminal (Ctrl+`)
#   Make sure you are in the same folder as bug_week7.py
#   Type: python -m pytest test_week7.py -v
#   Press Enter.
#
# READING THE OUTPUT:
#   PASSED  ← the function behaved correctly for this test
#   FAILED  ← the function returned something unexpected
#             pytest will show you:
#               - which test failed
#               - what value was expected (the 'assert' line)
#               - what value was actually returned
#
# YOUR JOB THIS WEEK:
#   Tests 1 and 2 are fully written — study them as examples.
#   Tests 3 and 4 are STUBBED — fill in the assert statements.
#   Test 5 is MISSING ENTIRELY — you must write it from scratch.
#
# A stub looks like this:
#   def test_something():
#       pass   # <-- replace 'pass' with a real assert statement
#
# An assert statement looks like this:
#   assert some_function(inputs) == expected_output
#
# ============================================================
# WHAT IS AN ASSERT STATEMENT?
#
# assert <condition>
#
# If the condition is True  → Python does nothing (test passes)
# If the condition is False → Python raises AssertionError (test fails)
#
# In a test function, you call the function under test with
# a known input and assert that the output equals what you expect.
#
# Example:
#   assert format_student("ada", "lovelace", "A001") == \
#          "Lovelace, Ada  (ID: A001)"
#
# ============================================================
# WHAT MAKES A GOOD TEST CASE? (running list)
#   first    — first item / lowest input
#   middle   — typical input in the middle
#   last     — last item / highest input
#   missing  — input not in the data
#   edge     — unusual but valid (empty string, zero, spaces)
#   boundary — exact value where behavior changes
#   empty    — empty list, empty string, zero quantity
#
# For each stubbed test below, think about which category
# of test case would be most valuable to write.
# ============================================================

# ============================================================
# IMPORTS — bringing in tools we need to run our tests
#
# At this point in the course we haven't covered imports in
# depth yet. For now, just know that the two following lines are required
# boilerplate to make the test file work. 
#
# Line 1: import pytest
#   pytest is a testing tool we installed with pip.
#   Importing it makes its testing machinery available
#   in this file. You won't call pytest directly in your
#   code — just having it imported is enough for the
#   'python -m pytest' command to find and run your tests.
#
# Line 2: from bug_week7 import ...
#   This pulls the specific functions you wrote in
#   bug_week7.py into this file so the tests can call them.
#   Think of it like this: bug_week7.py is the program
#   being tested, and test_week7.py is the test lab.
#   This line is the doorway between the two files.
#
#   If you add a new function to bug_week7.py that you
#   want to test, you need to add its name to this list.
# ============================================================
import pytest
from bug_week7 import format_student, format_schedule, apply_discount, build_roster
import pytest
from bug_week7 import format_student, format_schedule, apply_discount, build_roster


# ============================================================
# TESTS FOR format_student()
# Fully written — read these carefully as your model.
# ============================================================

def test_format_student_typical():
    """A typical student with first name, last name, and ID."""
    # This is the MIDDLE / happy-path test case.
    # It checks that the output is formatted correctly:
    # last name first, title-cased, with ID in parentheses.
    result = format_student("jordan", "smith", "S001")
    assert result == "Smith, Jordan  (ID: S001)"

def test_format_student_all_uppercase_input():
    """Names passed in ALL CAPS should still be title-cased."""
    # This is an EDGE test case — unusual but valid input.
    # .title() should handle it, but we verify that explicitly.
    result = format_student("JORDAN", "SMITH", "S002")
    assert result == "Smith, Jordan  (ID: S002)"


# ============================================================
# TESTS FOR apply_discount()
# Fully written — study the boundary and middle cases.
# ============================================================

def test_apply_discount_typical():
    """20% off $100 should return $80.00."""
    # MIDDLE test case — a common, expected use.
    # NOTE: once Bug 3 is fixed, this should pass.
    # Before the fix, it accidentally passes anyway —
    # that is exactly what makes Bug 3 so sneaky.
    result = apply_discount(100.00, 20)
    assert result == 80.00

def test_apply_discount_no_discount():
    """0% discount should return the original price unchanged."""
    # BOUNDARY test case — the lower edge of discount range.
    result = apply_discount(50.00, 0)
    assert result == 50.00


# ============================================================
# STUB 1 — Your turn: test apply_discount() with a non-$100 price
#
# The bug in apply_discount() hides when price == 100
# because subtracting 20 from 100 gives 80 — which LOOKS like
# 20% off. Try a price where the math clearly breaks.
#
# Hint: what is 20% off $50.00?
#       What does the BUGGY function actually return for that?
#       Write an assert that catches the difference.
#
# Test case category this covers: MIDDLE (different price point)
# ============================================================
def test_apply_discount_non_hundred_price():
    """20% off $50.00 should return $40.00."""
    pass   # TODO: replace this with a real assert statement


# ============================================================
# STUB 2 — Your turn: test apply_discount() at 100% off
#
# What should happen when discount_percent = 100?
# The result should be $0.00.
# Write an assert that verifies this.
#
# Test case category this covers: BOUNDARY (maximum discount)
# ============================================================
def test_apply_discount_full_discount():
    """100% discount should return $0.00."""
    pass   # TODO: replace this with a real assert statement


# ============================================================
# STUB 3 — Your turn: test format_schedule() returns a string
#
# format_schedule() has a missing return statement (Bug 2).
# Even after you fix it, write a test that would have caught
# the bug automatically — so that if someone removes the
# return statement again in the future, the test fails.
#
# Think about: what should the returned value contain?
# You can use Python's 'in' operator in an assert:
#   assert "something" in result
#
# Test case category this covers: MIDDLE (typical schedule)
# ============================================================
def test_format_schedule_returns_string():
    """format_schedule should return a non-None string."""
    pass   # TODO: replace this with a real assert statement


# ============================================================
# MISSING TEST — Write this one entirely from scratch.
#
# There is NO stub for this test. You must write the whole
# thing: the function name, the docstring, and the assert.
#
# What to test: build_roster() called TWICE with no student list.
#
# This is the mutable default argument bug (Bug 4).
# The key insight: if you call build_roster("Python") and then
# call build_roster("Circuits"), the second call should NOT
# contain any data from the first call.
#
# Your test must:
#   1. Call build_roster() once with just a course name.
#   2. Call build_roster() again with a DIFFERENT course name.
#   3. Assert that the second result does NOT contain any
#      leftover data from the first call.
#
# GUIDANCE:
#   - Name your test function starting with test_
#   - Write a docstring explaining what it checks
#   - Think about what category of test case this is
#     (hint: it requires TWO calls — it's testing STATE
#     between calls, which is a new category: STATEFUL)
#   - After you fix Bug 4 in bug_week7.py, your test
#     should go from FAILED to PASSED.
# ============================================================

# Write your test here:


# ============================================================
# HOW TO KNOW YOU ARE DONE:
#
# Run: python -m pytest test_week7.py -v
#
# You should see:
#   test_format_student_typical              PASSED
#   test_format_student_all_uppercase_input  PASSED
#   test_apply_discount_typical              PASSED
#   test_apply_discount_no_discount          PASSED
#   test_apply_discount_non_hundred_price    PASSED   ← your stub
#   test_apply_discount_full_discount        PASSED   ← your stub
#   test_format_schedule_returns_string      PASSED   ← your stub
#   test_build_roster_no_state_bleed         PASSED   ← your new test
#
# All 8 tests passing = all 4 bugs fixed + all tests written.
# ============================================================