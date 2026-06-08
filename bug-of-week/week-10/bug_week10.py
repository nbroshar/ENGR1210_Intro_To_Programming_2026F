# bug_week10.py
# QUALITY CHECK OF THE WEEK - Week 10: Test Coverage
#
# A NOTE ON THIS WEEK'S FORMAT:
# For nine weeks you hunted a fixed number of bugs. This week is
# different. There is only ONE bug in this file — and it is
# hiding in a branch your starter tests never run. Your job is
# not to read the code until you spot it. Your job is to learn a
# TOOL that points a flashlight at every line your tests forgot,
# then write the test that drags the bug into the light.
#
# ============================================================
# THE THIRD QUESTION, MEASURED
#
# Last week you learned that a passing test only proves ONE path
# works. You counted branches by hand and tried to test each one.
# That works for a 5-line function. It does NOT scale.
#
# This week you meet the tool professionals use instead:
#
#     pytest-cov  — runs your tests, then reports exactly which
#                   lines of your code were NEVER executed.
#
# Lines your tests never run are lines you have never actually
# checked. Bugs live there safely, because no test ever looks.
# ============================================================
#
# ============================================================
# ONE-TIME SETUP (run once in the VS Code terminal):
#
#     pip install pytest-cov
#
# Verify it installed:
#
#     python -m pytest --help    (you should see a "coverage" group)
#
# ============================================================
# THE TWO COMMANDS YOU WILL USE THIS WEEK
#
# 1) TERMINAL REPORT — fast, shows missing line numbers:
#
#     python -m pytest test_week10.py --cov=bug_week10 --cov-report=term-missing
#
#    Read the "Missing" column. It lists the exact line numbers
#    that NO test ever ran. Example of what you'll see:
#
#        Name            Stmts   Miss  Cover   Missing
#        ---------------------------------------------
#        bug_week10.py       8      2    75%   <line>, <line>
#
#    75% means one quarter of your code was never tested.
#    The two numbers under "Missing" are the lines to go test.
#
# 2) HTML REPORT — visual, opens in your browser:
#
#     python -m pytest test_week10.py --cov=bug_week10 --cov-report=html
#
#    This creates a folder called  htmlcov/.  Open htmlcov/index.html
#    in your browser, click bug_week10.py, and you will SEE every
#    line color-coded:
#        GREEN = a test ran this line
#        RED   = no test ever ran this line   <-- go look here
#
# ============================================================
# THE PROGRAM: a store membership discount
#
# get_discount() returns the discount RATE (as a decimal) for a
# shopper based on their membership level and age:
#
#     Gold member, senior (65 or older) ... 30% off  (0.30)
#     Gold member, under 65 .............. 20% off  (0.20)
#     Silver member ...................... 10% off  (0.10)
#     No / other membership .............. 0% off   (0.00)
#
# It runs. It returns a number. The two tests in test_week10.py
# both PASS. Everything looks green and finished.
# It is not finished.
# ============================================================
def get_discount(membership, age):
    """Return the discount rate (0.00-1.00) for a shopper."""
    if membership == "Gold":
        if age >= 65:
            return 0.35          # the senior-Gold branch
        else:
            return 0.20          # the under-65 Gold branch
    elif membership == "Silver":
        return 0.10              # the Silver branch
    else:
        return 0.00              # the non-member branch


# ============================================================
# YOUR WORKFLOW THIS WEEK (follow in order):
#
#   STEP 1: Run the starter tests with coverage:
#       python -m pytest test_week10.py --cov=bug_week10 --cov-report=term-missing
#       All tests pass. But what is the coverage percentage?
#       Which line numbers show up under "Missing"?
#
#   STEP 2: Open the code and find those exact lines. Each one
#       is a branch (a possible behavior) that NO test has ever
#       checked. There are two of them here.
#
#   STEP 3: In test_week10.py, fill in the two stubbed tests so
#       that each missing branch gets run by a test. Re-run the
#       coverage command. Watch the percentage climb toward 100%
#       and the "Missing" column shrink.
#
#   STEP 4: One of those two newly-tested branches will FAIL when
#       you test it — because it contains the bug. The coverage
#       tool did not find the bug for you. It found the PLACE you
#       had never looked. YOUR test, run against that place,
#       found the bug.
#
#   STEP 5: Fix the bug. Re-run. Goal: all tests pass AND 100%
#       coverage. Green code AND a green report.
#
# HINT (only read if stuck on the bug): re-read the discount
#       rules at the top. A Gold senior should get 30% off.
#       What does the senior-Gold branch actually return?
# ============================================================


# ============================================================
# DEMO BLOCK — runs ONLY when you run this file directly.
# (The __main__ guard, so the test file can import get_discount.)
# Notice the demo only ever tries ONE shopper. That is the trap:
# a quick demo that looks fine can leave most of your code
# completely unexercised.
#
# The "# pragma: no cover" below tells the coverage tool to skip
# this demo block. It only runs when you launch the file directly
# (never under pytest), so flagging it as "untested" would be
# misleading. That keeps the Missing column focused on the
# branches that actually matter — the ones inside the function.
# ============================================================
if __name__ == "__main__":   # pragma: no cover
    print("--- Discount Demo ---")
    rate = get_discount("Gold", 40)
    print(f"  Gold member, age 40 -> {rate:.0%} off")
    # We never demo a senior, or a Silver member, or a non-member.
    # If a bug lived in one of those paths, this demo would never
    # reveal it. Coverage is how you find out what you skipped.


# ============================================================
# REFLECTION QUESTIONS (discuss with your partner):
#
#   1. The starter tests both PASSED, yet coverage was only 75%.
#      In your own words, what is the difference between "my
#      tests pass" and "my code is tested"? Why is it dangerous
#      to confuse the two?
#
#   2. Coverage told you WHERE you had not looked, but it did
#      NOT tell you the senior discount was wrong — your new test
#      did that. So what is coverage actually good for, and what
#      is it NOT able to do? (Hint: 100% coverage does not mean
#      zero bugs. Why not?)
#
#   3. Recall the example from the tools handout: a get_discount
#      with Gold/Silver/senior branches where one test gave 50%
#      coverage. Map that story onto what you saw this week.
#      Which branches were the "Silver members and seniors" that
#      went untested?
#
#   4. Looking ahead: this function has only 4 branches and was
#      already easy to leave half-tested. Next week you'll meet a
#      tool (radon) that grades how many branches a function has.
#      Why would a function with MANY branches be even more
#      likely to hide an untested path?
# ============================================================
