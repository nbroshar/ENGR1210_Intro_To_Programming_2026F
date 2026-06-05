# bug_week7.py
# BUG OF THE WEEK - Week 7: Functions
#
# INSTRUCTIONS: This file has 4 bugs in it.
# Bug 1: Find with the console error message.
# Bug 2: Find with the VS Code Debugger.
# Bug 3: Find with the VS Code Debugger + test cases.
# Bug 4: Can ONLY be found by a thoughtful test case —
#         the one that the unit test file will catch automatically.
#
# ============================================================
# STANDARD DEBUGGING PROCESS (review):
#   STEP 1: Run — read error type and line number.
#   STEP 2: Fix ONE bug, save, run again.
#   STEP 3: Repeat until no crashes.
#   STEP 4: CHECK YOUR OUTPUT. Running != correct.
#
# VS CODE DEBUGGER (review):
#   Set breakpoint : click gray margin left of line number
#   Start          : F5  ->  Python File
#   Step Into      : F11  <- NEW THIS WEEK: follows execution
#                          INSIDE the function body
#   Step Over      : F10  (run current line, pause on next)
#   Continue       : F5
#   Stop           : Shift+F5
#   Variables panel: left sidebar while paused
#
# ============================================================
# NEW THIS WEEK: STEP INTO vs. STEP OVER
#
# Last week you used F10 (Step Over) to move line by line.
# Step Over treats a function call as ONE step — it runs the
# whole function and pauses on the next line after it returns.
#
# F11 (Step Into) follows execution INSIDE the function.
# This is essential for debugging functions — you can watch
# the parameter values at the moment the function receives
# them, and trace exactly what happens inside.
#
# Rule of thumb:
#   Use F10 when you trust the function and want to skip it.
#   Use F11 when the function IS the thing you are debugging.
#
# ============================================================
# NEW THIS WEEK: THE UNIT TEST FILE
#
# A second file — test_week7.py — runs automated tests
# against the functions in this file.
#
# To run the tests:
#   Open a terminal in VS Code (Ctrl+`)
#   Type: python -m pytest test_week7.py -v
#   Press Enter.
#
# Green  = test passed
# Red    = test failed — pytest tells you EXACTLY which
#          assertion failed and what the values were.
#
# Bug 4 in this file will PASS a visual check of the output.
# It will only be caught by one specific unit test.
# Run the tests, read the failure message, and trace back
# to the function to find and fix the bug.
#
# ============================================================
# NEW THIS WEEK: THE  if __name__ == "__main__"  GUARD
#
# Notice that all the demo calls (the print statements that
# show each function in action) now live at the BOTTOM of this
# file, inside a block that starts with:
#
#     if __name__ == "__main__":
#
# Here is why. test_week7.py needs to IMPORT this file to get
# at your functions. When Python imports a file, it runs every
# line in it from top to bottom. Without this guard, importing
# bug_week7.py would also run all the demo calls — including the
# one with Bug 1, which crashes. pytest would never even get to
# run your tests.
#
# The guard means: "only run the demo code when this file is
# run DIRECTLY (python bug_week7.py), NOT when it is imported."
#   - You run it directly  -> demos run, you see the bugs.
#   - pytest imports it     -> demos are skipped, tests run cleanly.
#
# This is the bridge between a standalone script and a reusable
# module. You'll use this same pattern in the in-class project.
# ============================================================


# ============================================================
# BUG 1 — Find with: console error message
#
# HINT: Read about positional arguments.
#       When you call a function with positional arguments,
#       Python assigns them LEFT TO RIGHT in the order they
#       appear in the function definition.
#       Count the parameters. Count the arguments.
#       Is there a mismatch?
#       (The buggy call is in the demo block at the bottom.)
# ============================================================
def format_student(first_name, last_name, student_id):
    """Return a formatted student label."""
    return f"{last_name.title()}, {first_name.title()}  (ID: {student_id})"


# ============================================================
# BUG 2 — Find with: VS Code Debugger using F11 (Step Into)
#
# format_schedule() is supposed to return a formatted string
# listing a student's courses. It runs without crashing but
# the returned value is always None, so nothing prints.
#
# DEBUGGER INSTRUCTIONS:
#   1. Set a breakpoint on: schedule = format_schedule(name, courses)
#   2. Press F5 to start.
#   3. Press F11 (Step Into) — you jump INSIDE format_schedule.
#   4. Watch the Variables panel: what is 'result' built up to?
#   5. Step Over each line inside the function.
#   6. When the function ends, check: what does it return?
#      Is there a return statement? Should there be?
#
# HINT: Read about return values.
#       A function that builds a value but never returns it
#       gives back None by default. Where is the return missing?
# ============================================================
def format_schedule(student_name, course_list):
    """Return a formatted schedule string for a student."""
    result = f"Schedule for {student_name.title()}:\n"
    for course in course_list:
        result += f"  - {course}\n"
    # BUG: no return statement — function silently returns None


# ============================================================
# BUG 3 — Find with: VS Code Debugger + test cases
#
# apply_discount() is supposed to apply a percentage discount
# to a price and return the discounted price.
# It runs, returns a number, and looks right — until you
# test specific inputs carefully.
#
# DEBUGGER INSTRUCTIONS:
#   1. Set a breakpoint on: result = apply_discount(price, discount)
#   2. Press F11 to Step Into the function.
#   3. In the Variables panel, watch 'price' and 'discount_percent'.
#   4. Step Over the calculation line. What is 'discounted'?
#   5. Try these test cases by changing the call in the demo block:
#
#   | Test Case        | price  | discount | Expected  | Actual | Pass? |
#   |------------------|--------|----------|-----------|--------|-------|
#   | A: 10% off $100  | 100.00 |   10     | $90.00    |        |       |
#   | B: 0% (no disc.) | 100.00 |    0     | $100.00   |        |       |
#   | C: 100% off      | 100.00 |  100     | $0.00     |        |       |
#   | D: 20% off $50   |  50.00 |   20     | $40.00    |        |       |
#   | E: BOUNDARY 1%   | 100.00 |    1     | $99.00    |        |       |
#
# NOTE: cases A, B, C, and E all use $100, where subtracting the
#       percent happens to look right. Case D ($50) is the one that
#       exposes the bug — that's the lesson about choosing inputs.
#
# HINT: Read about passing arguments and calculations.
#       The discount is passed as a whole number (e.g. 20 for 20%).
#       How do you convert that to a decimal for multiplication?
#       Check the math inside the function very carefully.
# ============================================================
def apply_discount(price, discount_percent):
    """Return price after applying a percentage discount."""
    # BUG: discount_percent is not converted to a decimal.
    # Subtracting 20 from 100.00 gives 80.00 — which LOOKS right
    # for a 20% discount on $100. But try $50 with 20% off...
    discounted = price - discount_percent
    return round(discounted, 2)


# ============================================================
# BUG 4 — Find with: UNIT TESTS (test_week7.py catches this)
#
# build_roster() takes a course name (and, optionally, a list of
# students) and returns a dictionary with the course as the key
# and the list of students as the value.
#
# This function looks correct. The demo call below prints
# something reasonable. A casual test passes.
#
# But the unit test file will catch a specific failure case.
# Run: python -m pytest test_week7.py -v
# Read the red failure message carefully.
# It will tell you EXACTLY which assertion failed and what
# the actual vs. expected values were.
# Then come back here and find the bug.
#
# HINT: Read about default parameter values
#       and think about mutable default arguments.
#       What happens to a list that is defined as a default
#       parameter value — is it created fresh each call,
#       or is it the SAME list object every time?
#       Try calling build_roster() twice with no student list
#       and watch what happens to the result.
# ============================================================
def build_roster(course_name, students=[]):
    """Return a roster dictionary for a course."""
    # BUG: mutable default argument — the [] is created ONCE
    # when Python loads the function definition, not fresh
    # each time the function is called. Students added in one
    # call bleed into all future calls that use the default.
    students.append("(enrolled)")    # simulates adding a marker
    return {course_name: students}


# ============================================================
# DEMO BLOCK — runs ONLY when you run this file directly.
# (See "THE __main__ GUARD" note at the top of the file.)
# This is where the bugs show up when you press F5 / Run.
# ============================================================
if __name__ == "__main__":

    # --- Bug 1 demo: too few arguments — student_id is missing ---
    print("--- Student Label ---")
    label = format_student("jordan", "smith")
    print(label)

    # --- Bug 2 demo: schedule prints as None (no return) ---
    print("\n--- Course Schedule ---")
    name    = "maria"
    courses = ["Python", "Circuits", "Technical Writing"]
    schedule = format_schedule(name, courses)
    print(schedule)

    # --- Bug 3 demo: change the numbers to run the test cases ---
    print("\n--- Discount Calculator ---")
    result = apply_discount(100.00, 20)
    print(f"20% off $100.00 -> ${result}")

    # --- Bug 4 demo: "(enrolled)" leaks from one call into the next ---
    print("\n--- Course Roster ---")
    roster1 = build_roster("Python")
    print(roster1)
    roster2 = build_roster("Circuits")
    print(roster2)   # surprise: "(enrolled)" appears twice


# ============================================================
# REFLECTION QUESTIONS (discuss with your partner):
#
#   1. Bug 2: A function with no return statement returns None.
#      Why is this particularly dangerous compared to a crash?
#      Give an example of how None silently breaking a program
#      could cause a much bigger problem downstream.
#
#   2. Bug 3: apply_discount(100.00, 20) gives $80 — which
#      looks correct for 20% off $100. But apply_discount(50.00, 20)
#      gives $30 — which is wrong ($40 is correct).
#      What kind of test case category (from our running list)
#      was needed to expose this? Why did the "obvious" test
#      case of $100 accidentally hide the bug?
#
#   3. Bug 4: The mutable default argument bug is one of the
#      most famous Python gotchas. In your own words, explain
#      WHY using [] as a default parameter is dangerous.
#      What is the standard Python fix for this pattern?
#      (Hint: the fix uses None as the default plus an if
#      statement at the top of the function.)
#
#   4. The __main__ guard: why could the unit tests NOT run
#      before we added "if __name__ == '__main__':" around the
#      demo calls? What does this tell you about what happens
#      when Python imports a file?
# ============================================================
