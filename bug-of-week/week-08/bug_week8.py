# bug_week8.py
# BUG OF THE WEEK - Week 8: Files and Exceptions
# Chapter 10 - Python Crash Course, 3rd Edition
#
# INSTRUCTIONS: This file has 4 bugs in it.
# Bug 1: Find with the console error message.
# Bug 2: Find with the VS Code Debugger (F11 Step Into).
# Bug 3: Find with the debugger + test cases — a dangerous
#         exception-handling bug that swallows real errors.
# Bug 4: Can ONLY be found by a thoughtful test case —
#         the unit test file will catch it automatically.
#
# ============================================================
# DATA FILES NEEDED:
#   Download courses.txt and scores.json from the course portal
#   and place them in the SAME FOLDER as this script.
#   Do NOT rename them — the code references them by exact name.
#
# Your week-08 folder should look like this:
#   week-08/
#   ├── bug_week8.py
#   ├── test_week8.py
#   ├── courses.txt
#   └── scores.json
# ============================================================
#
# ============================================================
# STANDARD DEBUGGING PROCESS (review):
#   STEP 1: Run — read error type and line number.
#   STEP 2: Fix ONE bug, save, run again.
#   STEP 3: Repeat until no crashes.
#   STEP 4: CHECK YOUR OUTPUT. Running ≠ correct.
#
# VS CODE DEBUGGER (review):
#   Set breakpoint : click gray margin left of line number
#   Start          : F5  →  Python File
#   Step Into      : F11  (follow execution inside a function)
#   Step Over      : F10  (run current line, pause on next)
#   Continue       : F5
#   Stop           : Shift+F5
#   Variables panel: left sidebar while paused
#
# ============================================================
# NEW THIS WEEK: EXCEPTIONS AND try/except
#
# An EXCEPTION is Python's way of signaling that something
# went wrong at runtime — a file wasn't found, a value was
# the wrong type, a division by zero occurred, etc.
#
# WITHOUT try/except: the exception crashes the program and
# prints a traceback. This is what you've seen all semester.
#
# WITH try/except: you catch the exception, handle it
# gracefully, and let the program continue — or at least
# fail with a useful message instead of a raw traceback.
#
# Basic structure (p. 185-189):
#
#   try:
#       # code that might raise an exception
#   except SomeSpecificError:
#       # what to do if that error occurs
#   else:
#       # runs only if no exception was raised
#   finally:
#       # ALWAYS runs, exception or not
#
# THE GOLDEN RULE OF EXCEPTION HANDLING:
#   ALWAYS catch the MOST SPECIFIC exception you can.
#   NEVER use a bare 'except:' with no exception type.
#   A bare except catches EVERYTHING — including errors
#   you didn't intend to catch, hiding bugs permanently.
#   This is Bug 3 this week. It is one of the most
#   dangerous patterns in all of Python.
#
# ============================================================
# IMPORTS — pre-approved boilerplate, covered in Ch. 10
# (We'll do a full import deep-dive in a later week.)
# pathlib.Path  — handles file paths across Windows/Mac/Linux
# json          — reads and writes JSON-formatted data files
# ============================================================

from pathlib import Path
import json


# ============================================================
# BUG 1 — Find with: console error message (FileNotFoundError)
#
# read_course_list() tries to open courses.txt, but something
# about the path is wrong. The file exists — but Python can't
# find it. Read the error message carefully.
#
# HINT: Read about file paths (p. 176-178).
#       Path('courses.txt') looks in the CURRENT WORKING
#       DIRECTORY — the folder VS Code opened your terminal in.
#       The error message will tell you exactly what path
#       Python is looking at.
#       Check: is the terminal open in the right folder?
#       In VS Code: Terminal menu → New Terminal opens in
#       the workspace root. If your file is in a subfolder,
#       you need to either cd into that folder or use a
#       relative path like Path('week-08/courses.txt').
#
#       The bug here is a WRONG PATH in the Path() call —
#       fix the path string to match where courses.txt lives.
# ============================================================
def read_course_list():
    """Read and return course names from courses.txt."""
    path = Path('wrong_folder/courses.txt')   # BUG: wrong path
    contents = path.read_text()
    return contents.splitlines()

print("--- Course List ---")
courses = read_course_list()
for course in courses:
    print(f"  {course}")


# ============================================================
# BUG 2 — Find with: VS Code Debugger (F11 Step Into)
#
# load_scores() reads scores.json and returns a dictionary.
# It runs without crashing, but the returned value is always
# an empty dictionary {} instead of the real scores.
#
# DEBUGGER INSTRUCTIONS:
#   1. Set a breakpoint on: scores = load_scores()
#   2. Press F5, then F11 to Step Into load_scores().
#   3. Watch the Variables panel as you Step Over each line.
#   4. What does 'contents' contain after read_text()?
#   5. What does json.loads() return?
#   6. When the function ends, what value does it return?
#      Is 'data' ever assigned? Or is the return happening
#      before the data is actually read?
#
# HINT: Read about working with JSON (p. 197-199) and
#       return values (Ch. 8, p. 143-145).
#       The function returns too early — before the file
#       has been read. A misplaced return statement inside
#       a function sends execution back immediately,
#       skipping everything after it.
# ============================================================
def load_scores():
    """Load and return the scores dictionary from scores.json."""
    data = {}
    return data          # BUG: returns immediately — before
                         # reading the file. Everything below
                         # is unreachable dead code.
    path     = Path('scores.json')
    contents = path.read_text()
    data     = json.loads(contents)
    return data

print("\n--- Student Scores ---")
scores = load_scores()
if scores:
    for name, score in scores.items():
        print(f"  {name.title()}: {score}")
else:
    print("  No scores loaded.")


# ============================================================
# BUG 3 — Find with: Debugger + test cases
#          THE MOST DANGEROUS BUG THIS WEEK
#
# save_score() is supposed to add a new student score to
# scores.json. It has exception handling — but the exception
# handling is BROKEN in a way that silently swallows errors.
#
# Step 1: Run the program as-is. It prints "Score saved!"
#         for every call — even bad ones. Does that seem right?
#
# Step 2: Design these test cases by temporarily changing the
#         call at the bottom of this section:
#
#   | Test Case             | name      | score | Expected      | Actual |
#   |-----------------------|-----------|-------|---------------|--------|
#   | A: Normal save        | "eve"     | 88    | Score saved!  |        |
#   | B: Score is a STRING  | "frank"   | "A+"  | Error message |        |
#   | C: Name is empty str  | ""        | 75    | Error message |        |
#   | D: Score is negative  | "grace"   | -5    | Should save?  |        |
#
# Step 3: Use the debugger on Test Case B:
#   1. Set a breakpoint on: try:
#   2. Press F5 and F11 to Step Into save_score().
#   3. Step through the try block. Does json.dumps() raise
#      an error when score is "A+"?
#   4. Does the except block catch it? What does it print?
#   5. What SHOULD happen vs. what DOES happen?
#
# HINT: Read about the dangers of broad exception handling
#       (p. 192-194). A bare 'except:' catches everything —
#       including KeyboardInterrupt (Ctrl+C), SystemExit,
#       and errors you never intended to handle.
#       What specific exception should be caught here instead?
#       And what bug in the success/error logic means the
#       wrong message always prints regardless?
# ============================================================
def save_score(student_name, score):
    """Add a new score to scores.json."""
    try:
        path     = Path('scores.json')
        contents = path.read_text()
        data     = json.loads(contents)
        data[student_name] = score
        path.write_text(json.dumps(data))
    except:                           # BUG 1: bare except — catches everything
        print("  Error: could not save score.")
    print("  Score saved!")           # BUG 2: outside the else — always prints
                                      # even when the except block ran

print("\n--- Saving New Score ---")
save_score("eve", 88)


# ============================================================
# BUG 4 — Find with: UNIT TESTS (test_week8.py catches this)
#
# parse_score_line() takes a single line from a text report
# formatted as "name: score" and returns a tuple (name, score)
# where score is an integer.
#
# Examples of valid input:
#   "alice: 95"    →  ("alice", 95)
#   "bob: 82"      →  ("bob", 82)
#
# The function looks correct and handles most inputs fine.
# But one specific category of input exposes a silent bug
# that the unit tests will catch. Run the tests, read the
# failure message, then come back and find it.
#
# Run: python -m pytest test_week8.py -v
#
# HINT: Think about WHITESPACE edge cases (p. 179-180).
#       What happens when the input line has extra spaces?
#       "alice:  95"   (two spaces after the colon)
#       " alice: 95"   (leading space before the name)
#       "alice: 95 "   (trailing space after the score)
#       The fix is a single string method you learned in Ch. 2.
# ============================================================
def parse_score_line(line):
    """
    Parse a 'name: score' line and return (name, score) tuple.
    Score is returned as an integer.
    """
    parts = line.split(':')
    name  = parts[0]          # BUG: no .strip() — leading/trailing
    score = int(parts[1])     # whitespace causes wrong name or
    return (name, score)      # ValueError on score conversion

print("\n--- Score Line Parser ---")
result = parse_score_line("alice: 95")
print(f"  Parsed: name='{result[0]}', score={result[1]}")


# ============================================================
# REFLECTION QUESTIONS (discuss with your partner):
#
#   1. Bug 1 — File paths:
#      Path('courses.txt') works when the terminal is in the
#      right folder, but breaks otherwise. What does this tell
#      you about the relationship between your terminal's
#      working directory and your Python script?
#      How would you make a path that works from ANYWHERE,
#      regardless of where the terminal is opened?
#      (Hint: look up Path(__file__).parent in the docs.)
#
#   2. Bug 2 — Dead code:
#      The lines after the misplaced return statement are
#      called "unreachable code" or "dead code." VS Code
#      actually dims dead code in the editor — did you notice?
#      Why is dead code dangerous even if it doesn't crash
#      the program?
#
#   3. Bug 3 — Bare except:
#      A bare except: is sometimes called "Pokemon exception
#      handling" — it catches them all. Why is this always
#      wrong? Give a concrete example of a bug that a bare
#      except would permanently hide in a real program.
#      What is the correct pattern to use instead?
#
#   4. Bug 4 — Whitespace:
#      "alice: 95" and " alice: 95" look almost identical to
#      a human but are completely different to Python.
#      Real data files (CSVs, logs, exports from other
#      programs) are FULL of inconsistent whitespace.
#      Why should .strip() be considered a defensive habit
#      any time you parse data from an external source?
# ============================================================
