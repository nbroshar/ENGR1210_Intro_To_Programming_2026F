# bug_week3.py
# BUG OF THE WEEK: Working with Lists
#
# INSTRUCTIONS: This file has 4 bugs in it.
# Follow the SAME structured debugging process from Weeks 1 and 2.
#
# ============================================================
# HOW TO DEBUG IN A STRUCTURED WAY (review from Week 1):
#
#   STEP 1: Run the program and READ the error message carefully.
#           - What LINE number does it point to?
#           - What TYPE of error is it? (IndentationError, TypeError,
#             SyntaxError, or a logic error with no crash at all?)
#
#   STEP 2: Go to that line and look for the problem.
#           - Fix ONE bug at a time — don't change anything else!
#
#   STEP 3: Fix that ONE bug, then SAVE and RUN again.
#
#   STEP 4: Repeat Steps 1-3 until the program runs cleanly.
#
#   NEW THIS WEEK: You may see an IndentationError.
#           - IndentationError → Python is strict about indentation
#             inside a for loop. Every line inside the loop MUST be
#             indented consistently (use 4 spaces or Tab, not both).
# ============================================================

# --- OUR LIST OF PLANETS ---
# This line is correct — no bug here.
planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn"]

# ============================================================
# BUG 1
# BUG HINT: Read about for loop syntax carefully.
#           Every line that belongs INSIDE the loop must be indented.
#           Every line OUTSIDE the loop must NOT be indented.
#           Which print statement below is in the wrong place?
# ============================================================
print("--- All Planets ---")
for planet in planets:
    print(planet.title())
print("  (part of our solar system)")   # <-- should this be inside or outside?

# ============================================================
# BUG 2
# BUG HINT: Read about the range() function.
#           range(1, 6) produces: 1, 2, 3, 4, 5
#           Does it include the stop value, or stop just before it?
#           The goal here is to print numbers 1 through 5 inclusive.
#           Is the range below producing the right numbers?
# ============================================================
print("\n--- Counting Planets (inner solar system) ---")
for number in range(1, 4):
    print(number)

# ============================================================
# BUG 3
# BUG HINT: Read about numerical list functions.
#           min(), max(), and sum() are built-in functions.
#           What is the correct syntax for calling a function?
#           Compare how you call a function vs. a list method.
# ============================================================
scores = [88, 95, 70, 100, 83]
print("\n--- Test Score Stats ---")
print("Lowest: " + str(scores.min()))
print("Highest: " + str(scores.max()))
print("Total points: " + str(scores.sum()))

# ============================================================
# BUG 4
# BUG HINT: Read about list comprehensions.
#           The syntax is: [expression for item in list]
#           Look carefully at the line below — something is
#           wrong with the structure of the comprehension.
#           Hint: where does the 'for' keyword belong?
# ============================================================
print("\n--- Squared Numbers ---")
squares = [number**2 for number in range(1, 6) if number > 10]
for square in squares:
    print(square)

# ============================================================
# REFLECTION QUESTIONS (discuss with your partner):
#   1. Bug 1: How does Python use indentation differently from
#      languages that use curly braces { }? What are the
#      advantages and disadvantages of Python's approach?
#   2. Bug 3: What is the difference between a METHOD (like
#      list.append()) and a FUNCTION (like min(), max(), sum())?
#      Why can't you call min() as scores.min()?
#   3. Bug 4: After fixing the syntax, does the list comprehension
#      produce output? If not, WHY — and what does that tell you
#      about where logic errors can hide in comprehensions?
# ============================================================