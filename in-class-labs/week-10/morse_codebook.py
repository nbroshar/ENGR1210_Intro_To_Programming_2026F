# morse_codebook.py
# =============================================================================
# Week 7 — your FIRST module.
#
# A "module" is just a .py file you can import into another file. This one
# holds nothing but DATA: the codebook and the two lookup dictionaries you
# built in Weeks 2-5. Pulling the data out into its own file means every
# other part of the project can share ONE copy of it.
#
# A module that only defines data and functions (no input(), no demo prints)
# is safe to import: importing it just makes its names available.
# =============================================================================

# The codebook as (letter, pattern) tuples — letters and digits.
CODEBOOK = [
    ('A', '.-'),   ('B', '-...'), ('C', '-.-.'), ('D', '-..'),  ('E', '.'),
    ('F', '..-.'), ('G', '--.'),  ('H', '....'), ('I', '..'),   ('J', '.---'),
    ('K', '-.-'),  ('L', '.-..'), ('M', '--'),   ('N', '-.'),   ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),  ('S', '...'),  ('T', '-'),
    ('U', '..-'),  ('V', '...-'), ('W', '.--'),  ('X', '-..-'), ('Y', '-.--'),
    ('Z', '--..'),
    ('0', '-----'),('1', '.----'),('2', '..---'),('3', '...--'),('4', '....-'),
    ('5', '.....'),('6', '-....'),('7', '--...'),('8', '---..'),('9', '----.'),
]

# Built once, here, from the codebook — the same comprehensions from Week 5.
ENCODE_MAP = {letter: pattern for (letter, pattern) in CODEBOOK}
DECODE_MAP = {pattern: letter for (letter, pattern) in ENCODE_MAP.items()}
