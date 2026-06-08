# bug_week11.py
# QUALITY CHECK OF THE WEEK - Week 11: Code Complexity
#
# A NOTE ON THIS WEEK'S FORMAT — READ THIS FIRST:
# There is NO bug in this file. The function below is correct.
# Run it, test it, and it will behave exactly as the rules say.
#
# So what is the "quality check"? The function is correct and
# AWFUL. It is a tangled nest of conditions that is painful to
# read, painful to test, and dangerous to change. This week you
# learn a tool that puts a NUMBER and a LETTER GRADE on exactly
# how tangled a function is — and you build the safety net that
# will let you fix it next week without breaking it.
#
# ============================================================
# WHAT IS CYCLOMATIC COMPLEXITY?
#
# Cyclomatic complexity counts the number of independent PATHS
# through a function — basically, "how many different ways can
# this code run?" Every if, elif, for, while, and every 'and' /
# 'or' adds one more path.
#
# A function with complexity 3 has 3 ways to run — easy to hold
# in your head, easy to test (you need ~3 tests). A function
# with complexity 14 has FOURTEEN ways to run. No human reliably
# keeps 14 paths straight, and you'd need ~14 tests to be sure
# every path works. High complexity is where bugs hide and where
# "small" changes break things three branches away.
#
# ============================================================
# THE TOOL: radon
#
# ONE-TIME SETUP (in the VS Code terminal):
#     pip install radon
#
# RUN IT:
#     radon cc bug_week11.py -s
#
#   "cc" = cyclomatic complexity.  "-s" = show the numeric score.
#
# You will see something like this:
#
#     bug_week11.py
#         F 94:0 final_status - C (14)
#
# HOW TO READ THAT LINE — this trips everyone up at first:
#     F          <- the BLOCK TYPE: F = function (M = method,
#                   C = class). This is NOT a grade!
#     65:0       <- the line and column where the block starts
#     final_status   <- the name of the block
#     - C (14)   <- the GRADE (C) and the raw score (14).
#                   THIS letter is the grade you care about.
#
# So "F ... - C (14)" means: a Function, graded C, score 14.
#
# RADON'S GRADING SCALE (memorize the shape, not the numbers):
#     score  1-5   -> A   simple, low risk
#     score  6-10  -> B   well structured, stable
#     score 11-20  -> C   slightly complex  <-- this function
#     score 21-30  -> D   more than moderately complex
#     score 31-40  -> E   complex, alarming
#     score  41+   -> F   error-prone, unstable
#
# Add  -a  to also print the average for the whole file:
#     radon cc bug_week11.py -s -a
#
# ============================================================
# THE PROGRAM: a student final-status calculator
#
# final_status() decides a student's end-of-term status from
# four inputs. The rules it implements are:
#
#   score >= 90:
#       attendance >= 90:
#           0 missing assignments ......... "Honors"
#           1-2 missing ................... "Pass with distinction"
#           3+ missing .................... "Pass"
#       attendance 75-89:
#           0-2 missing ................... "Pass"
#           3+ missing .................... "Conditional"
#       attendance < 75 ............ ...... "Conditional"
#   score 70-89:
#       attendance >= 75 AND <=3 missing .. "Pass"
#       has an extension AND <=5 missing .. "Conditional"
#       otherwise ..................... ... "Fail"
#   score 60-69:
#       has an extension .................. "Conditional"
#       otherwise ......................... "Fail"
#   score < 60 ............................ "Fail"
#
# The code below implements those rules correctly. It is just
# very hard to verify that by looking — which is the whole point.
# ============================================================
def final_status(score, attendance, missing, has_extension):
    """Return a student's end-of-term status. (Correct, but complex.)"""
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
# YOUR WORKFLOW THIS WEEK (follow in order):
#
#   STEP 1: MEASURE.
#       Run:  radon cc bug_week11.py -s
#       Write down the grade and the score for final_status.
#
#   STEP 2: UNDERSTAND.
#       In one sentence, explain what the score means in plain
#       English. ("This function has ___ independent paths.")
#
#   STEP 3: LOCK IT DOWN (this is the real work).
#       Open test_week11.py and write a test for each path of
#       the function. These are called CHARACTERIZATION TESTS:
#       tests that pin down what the code does RIGHT NOW. Because
#       the code is already correct, every test should PASS.
#
#   STEP 4: CONNECT IT TO LAST WEEK.
#       Run your tests with coverage:
#         python -m pytest test_week11.py --cov=bug_week11 --cov-report=term-missing
#       Keep adding path tests until coverage hits 100%. Now
#       compare: how many tests did 100% coverage take? How does
#       that number compare to radon's complexity score? (They
#       should be close — that is not a coincidence.)
#
#   STEP 5: HAND OFF.
#       Next week you will REFACTOR this function to earn an A
#       from radon — without changing a single one of its
#       outputs. Your passing test suite is the safety net that
#       proves you didn't break anything. That is why you write
#       the tests BEFORE you touch the code.
#
# There is nothing to "fix" this week. A correct, well-tested,
# F-for-effort tangle is still bad code. Quality is a separate
# axis from correctness — that is the entire lesson.
# ============================================================


# ============================================================
# DEMO BLOCK — runs ONLY when you run this file directly.
# ============================================================
if __name__ == "__main__":   # pragma: no cover
    print("--- Final Status Demo ---")
    cases = [
        (95, 95, 0, False),
        (95, 95, 1, False),
        (95, 80, 4, False),
        (75, 80, 2, False),
        (75, 50, 4, True),
        (65, 50, 0, True),
        (40, 90, 0, False),
    ]
    for c in cases:
        print(f"  score={c[0]} att={c[1]} missing={c[2]} ext={c[3]} -> {final_status(*c)}")


# ============================================================
# REFLECTION QUESTIONS (discuss with your partner):
#
#   1. This function passed every test you wrote AND was 100%
#      correct. Radon still graded it C. In your own words, what
#      is the difference between code being CORRECT and code
#      being GOOD? Can you think of a real piece of software
#      where "correct but unmaintainable" would be a serious
#      problem?
#
#   2. You needed roughly as many tests as the complexity score
#      to cover every path. What does that tell you about the
#      relationship between how complex a function is and how
#      expensive it is to test it properly?
#
#   3. radon labels the function with an "F" prefix that means
#      "function", not the grade F. Why is it important to read
#      a tool's output carefully rather than reacting to the
#      first letter you see? (Have you ever misread an error
#      message earlier this semester for a similar reason?)
#
#   4. Looking ahead: next week you'll break this one big
#      function into several small ones, each graded A. Before
#      you do, predict: will the TOTAL amount of code go up or
#      down? Will it become easier or harder to test each piece?
#      Write your prediction now and check it next week.
# ============================================================
