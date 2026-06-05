# bug_week5.py
# BUG OF THE WEEK - Week 5: Dictionaries
#
# INSTRUCTIONS: This file has 4 bugs in it.
# Bug 1: Find with the standard run (console error message).
# Bug 2: Find with the VS Code Debugger.
# Bug 3: Find with the VS Code Debugger.
# Bug 4: Can ONLY be found by running a thoughtful set of TEST CASES.
#         The program will run cleanly and look correct —
#         until you try the right input.
#
# ============================================================
# STANDARD DEBUGGING PROCESS (review):
#
#   STEP 1: Run — read error type and line number.
#   STEP 2: Fix ONE bug, save, run again.
#   STEP 3: Repeat until no crashes.
#   STEP 4: CHECK YOUR OUTPUT. Running ≠ correct.
#
# VS CODE DEBUGGER (review from Week 4):
#   Set breakpoint : click gray margin left of line number
#   Start          : F5  →  Python File
#   Step Over      : F10  (run one line, pause on next)
#   Continue       : F5   (run to next breakpoint)
#   Stop           : Shift+F5
#   Variables panel: left sidebar — watch variable values live
#
# ============================================================
# NEW THIS WEEK: THINKING IN TEST CASES
#
# A TEST CASE is one specific input you run your program
# against to check whether the output is correct.
#
# One input is NEVER enough. Good programmers think:
#   "What are all the DIFFERENT SITUATIONS my code might face?"
#
# For any lookup or search, classic test case categories are:
#
#   FIRST  — the very first item / lowest boundary
#   MIDDLE — a typical item somewhere in the middle
#   LAST   — the very last item / highest boundary
#   MISSING — something that is NOT in the data at all
#   EDGE   — unusual but valid input (empty string, zero,
#             uppercase vs lowercase, duplicate values...)
#
# Bug 4 in this file passes a casual glance — and even passes
# two or three test cases. Only a COMPLETE set of test cases
# (first, middle, last, missing) reveals the flaw.
#
# THIS IS THE POINT: professional bugs hide exactly here.
# Unit tests automate this process. For now,
# practice running test cases MANUALLY and writing down
# what you expected vs. what you got.
# ============================================================


# ============================================================
# THE PROGRAM: a simple course grade book
#
# We have a dictionary of students and their final grades (0-100).
# The code below tries to:
#   1. Look up a student's grade
#   2. Loop through all students and print their grades
#   3. Check whether a student is on the honor roll (>= 90)
#   4. Find the student with the highest grade
# ============================================================

grade_book = {
    "alice":   95,
    "bob":     82,
    "carlos":  90,
    "diana":   78,
    "eve":     95,
}


# ============================================================
# BUG 1 — Find with: console error message (KeyError)
#
# HINT: Read about accessing dictionary values.
#       A KeyError means you asked for a key that does not
#       exist in the dictionary. Look carefully at the key
#       being used here vs. the keys stored in grade_book.
#       Python dictionary keys are case-sensitive.
# ============================================================
print("--- Grade Lookup ---")
student = "Alice"
print(f"{student}'s grade: {grade_book[student]}")


# ============================================================
# BUG 2 — Find with: VS Code Debugger
#
# The loop below is supposed to print every student's grade
# formatted as: "alice: 95"
# But something is wrong — one student's grade prints
# incorrectly. Reading the code might not show it immediately.
#
# DEBUGGER INSTRUCTIONS:
#   1. Set a breakpoint on the line: for name, grade in grade_book.items():
#   2. Press F5 to start the debugger.
#   3. Press F10 to Step Over once — check: what are 'name' and 'grade'?
#   4. Keep stepping. On which student does 'grade' have the wrong value?
#   5. Now look at grade_book — do you see the problem?
#
# HINT: Read about looping through key-value pairs.
#       Check every entry in grade_book carefully.
#       One value was entered as a string instead of an integer.
# ============================================================
print("\n--- All Grades ---")
for name, grade in grade_book.items():
    print(f"  {name}: {grade}")


# ============================================================
# BUG 3 — Find with: VS Code Debugger
#
# The honor roll check should print the name of every student
# whose grade is >= 90. But one student who qualifies is
# being left off. No error message — just wrong output.
#
# DEBUGGER INSTRUCTIONS:
#   1. Fix the grade_book first (Bug 2) so values are correct.
#   2. Set a breakpoint on: for name, grade in grade_book.items():
#      (the honor roll loop below)
#   3. Step Over each iteration. Watch 'grade' in the Variables panel.
#   4. When grade = 90, does the if condition evaluate to True or False?
#   5. Should a grade of exactly 90 make the honor roll?
#
# HINT: Read about comparison operators in if statements.
#       Is the boundary condition correct for "90 or above"?
# ============================================================
print("\n--- Honor Roll (grade >= 90) ---")
for name, grade in grade_book.items():
    if grade > 90:
        print(f"  {name.title()} made the honor roll!")


# ============================================================
# BUG 4 — Find with: TEST CASES  ← NEW THIS WEEK
#
# This code claims to find the student with the highest grade.
# Run it — it produces output with no crash and no obvious error.
# It even gives the RIGHT answer for MOST inputs.
#
# But there is a subtle logic error that only appears under
# specific conditions. You must design test cases to find it.
#
# STEP 1: Run the program as-is. Note the output.
#
# STEP 2: Design and run these test cases by temporarily
#         CHANGING grade_book to match each scenario,
#         then running the program and checking the output:
#
#   Test Case A (MIDDLE wins):
#       Current grade_book — who should win? Does it?
#
#   Test Case B (FIRST entry wins):
#       grade_book = {"alice": 99, "bob": 82, "carlos": 70}
#       Expected: alice    Actual: ?
#
#   Test Case C (LAST entry wins):
#       grade_book = {"alice": 70, "bob": 82, "carlos": 99}
#       Expected: carlos   Actual: ?
#
#   Test Case D (TIE — two students share the highest grade):
#       grade_book = {"alice": 95, "bob": 95, "carlos": 70}
#       Expected: both alice and bob (or at least one of them)
#       Actual: ?
#
#   Test Case E (only ONE student):
#       grade_book = {"alice": 88}
#       Expected: alice    Actual: ?
#
# STEP 3: Record what each test case revealed.
#         Which test case exposes the bug?
#
# HINT: Watch what 'top_student' and 'top_grade' are initialized
#       to before the loop starts. What happens in Test Case B
#       if the actual top student is the FIRST one the loop sees?
#       Step through it with the debugger on Test Case B to watch
#       the variables change — or not change — each iteration.
# ============================================================
print("\n--- Top Student ---")
top_student = ""
top_grade = 100          # <-- this is the bug; think about why

for name, grade in grade_book.items():
    if grade > top_grade:
        top_student = name
        top_grade = grade

if top_student:
    print(f"  Top student: {top_student.title()} with a {top_grade}")
else:
    print("  No top student found.")


# ============================================================
# TEST CASE LOG — fill this in as you work
# (This is the beginning of professional testing discipline)
#
#   | Test Case | grade_book used         | Expected output     | Actual output | Pass/Fail |
#   |-----------|-------------------------|---------------------|---------------|-----------|
#   | A: Middle |  current grade_book     |                     |               |           |
#   | B: First  |  alice=99,bob=82,c=70   |  alice              |               |           |
#   | C: Last   |  alice=70,bob=82,c=99   |  carlos             |               |           |
#   | D: Tie    |  alice=95,bob=95,c=70   |  alice or bob       |               |           |
#   | E: One    |  alice=88               |  alice              |               |           |
#
# REFLECTION QUESTIONS (discuss with your partner):
#
#   1. Which test case (A, B, C, D, or E) exposed the bug?
#      WHY does that specific case reveal it when others don't?
#
#   2. What is wrong with initializing top_grade = 100?
#      What should it be initialized to instead, and why?
#      (Hint: think about what value guarantees every real
#      grade will beat it on the first comparison.)
#
#   3. What are the five test case CATEGORIES introduced today
#      (first, last, middle, missing, edge)?
#      For each category, describe a real-world scenario where
#      a bug would ONLY show up in that category.
#
#   4. We ran these test cases MANUALLY this week.
#      What would be the advantage of writing code that runs
#      them AUTOMATICALLY every time you change your program?
#      (This is exactly what Chapter 11 unit tests do.)
# ============================================================