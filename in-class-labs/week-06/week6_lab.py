# =============================================================================
# ENGR1210 — Morse Code Translator Project
# Week 6 Lab: User Input and while Loops
# Chapter 7 — Python Crash Course, 3rd Edition
#
# Standalone script — the LAST week before "The Great Refactor."
# Still no functions and no imports. New tools: input() and while loops.
# This week your translator becomes INTERACTIVE, and you start turning
# measured signal durations back into dots, dashes, and gaps.
#
# NOTE: this file asks for keyboard input, so RUN it (F5) and type at the
# prompts. Type 'quit' to leave the loop.
# =============================================================================

# --- Carried forward: build both lookup dictionaries from the codebook -------
CODEBOOK = [
    ('A', '.-'),   ('B', '-...'), ('C', '-.-.'), ('D', '-..'),  ('E', '.'),
    ('F', '..-.'), ('G', '--.'),  ('H', '....'), ('I', '..'),   ('J', '.---'),
    ('K', '-.-'),  ('L', '.-..'), ('M', '--'),   ('N', '-.'),   ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),  ('S', '...'),  ('T', '-'),
    ('U', '..-'),  ('V', '...-'), ('W', '.--'),  ('X', '-..-'), ('Y', '-.--'),
    ('Z', '--..'),
]
ENCODE_MAP = {letter: pattern for (letter, pattern) in CODEBOOK}

DOT_MS = 100   # base unit, carried forward (boundaries are multiples of it)


# =============================================================================
# SECTION 1 — ANCHOR
# =============================================================================
print("=" * 52)
print("SECTION 1: ANCHOR — An Interactive Encoder")
print("=" * 52)
print("Type a message to encode. Type 'quit' to stop.\n")

# A while loop repeats as long as its condition stays True. We use a
# 'sentinel' value ('quit') to decide when to stop. (Week 7: this whole
# loop body becomes a clean function call.)
while True:
    text = input("Message> ")
    if text.lower() == 'quit':
        print("Goodbye!")
        break                      # leave the while loop

    encoded = []
    for character in text.upper():
        if character == ' ':
            encoded.append(' ')
        else:
            encoded.append(ENCODE_MAP.get(character, '?'))
    print(f"  Morse: {' '.join(encoded)}\n")

# -- ANCHOR QUESTIONS ------------------------------------------------------
# Q1. What is the 'sentinel' value here, and what would happen if we forgot
#     the break? (Careful — that's an infinite loop. Use Ctrl+C to escape.)
# Q2. Why do we check text.lower() == 'quit' instead of text == 'quit'?
# Q3. input() always returns a string. Why does that matter the moment you
#     ask the user for a NUMBER (see the GUIDED section)?


# =============================================================================
# SECTION 2 — GUIDED
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 2: GUIDED — Classify Received Signal Durations")
print("=" * 52)

# The RECEIVER measures how long the light was ON or OFF, in milliseconds,
# and must decide what each measurement means. The boundaries are multiples
# of DOT_MS:
#     ON  pulse:   shorter than DOT_MS*2 (200ms) = dot,  otherwise dash
#     OFF gap:     shorter than DOT_MS*2 = symbol gap (within a letter)
#                  shorter than DOT_MS*5 (500ms) = letter gap
#                  DOT_MS*5 or longer = word gap
#
# (Week 7: these become classify_pulse() and classify_gap().)

pulse_durations = [55, 105, 180, 240, 300]   # measured ON times (ms)
gap_durations   = [90, 150, 320, 480, 700]   # measured OFF times (ms)

print("\nPulse (LED ON) classification:")
for duration in pulse_durations:
    # TODO: if duration < DOT_MS * 2 -> 'dot', else -> 'dash'. Print it.
    kind = ""    # TODO: use an if/else to set kind
    print(f"  {duration:4}ms -> {kind}")

print("\nGap (LED OFF) classification:")
for duration in gap_durations:
    # TODO: use if / elif / else with the two boundaries above to set 'kind'
    #       to 'symbol_gap', 'letter_gap', or 'word_gap'. Print it.
    kind = ""    # TODO
    print(f"  {duration:4}ms -> {kind}")


# =============================================================================
# SECTION 3 — EXTENSION
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 3: EXTENSION — A Menu-Driven Translator")
print("=" * 52)

# Build a small menu that loops until the user chooses to quit:
#     1) Encode text -> Morse
#     2) Count how many letters are in the codebook
#     3) Quit
#
# Use a while loop with input() and an if/elif/else on the menu choice.
# Re-show the menu after each action. (Encoding code can be copied from
# the ANCHOR — copying it AGAIN is a hint about why functions exist...)

# TODO: implement the menu loop here
#   while True:
#       print the menu
#       choice = input("Choose 1-3> ")
#       if choice == '1': ...
#       elif choice == '2': ...
#       elif choice == '3': break
#       else: print an "invalid choice" message


# =============================================================================
# SECTION 4 — STRETCH
# =============================================================================
print("\n" + "=" * 52)
print("SECTION 4: STRETCH — Robust Numeric Input")
print("=" * 52)

# Ask the user "How many times should I repeat the message?" and keep
# asking until they enter a valid whole number greater than 0.
#   - input() returns a string; you'll need int() to convert it.
#   - A bad entry like "five" will crash int(). For now, guard it by
#     checking the string with .isdigit() BEFORE converting.
#   - Once you have a valid count, encode a fixed message and print its
#     Morse that many times.
#
# Reflect in a comment: this is a "validation loop." Why is it safer to
# keep asking than to trust the first thing the user types?

# TODO: implement the validation loop here


# =============================================================================
# CHECKLIST
#   [ ] ANCHOR:    typed messages; 'quit' exits cleanly; answered Q1-Q3
#   [ ] GUIDED:    pulses classify as dot/dash; gaps as symbol/letter/word
#   [ ] EXTENSION: menu loop runs until you choose Quit
#   [ ] STRETCH:   (optional) numeric input is validated before use
#   [ ] I noticed how many times I copy-pasted the encoding loop
#
# LOOKING AHEAD — Week 7: THE GREAT REFACTOR
#   You now have a WORKING translator — but the same encoding loop is
#   copy-pasted in several places, and everything lives in one giant file.
#   Next week you learn FUNCTIONS. You'll wrap each piece of logic in a
#   function, split the project into MODULES (separate .py files), and meet
#   the hardware layer that finally turns "[LED]" print lines into a real
#   blinking LED you can run on a Pi Pico. Keep ALL your week 1-6 files.
# =============================================================================
