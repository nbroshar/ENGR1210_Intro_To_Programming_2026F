# morse_encoder.py
# =============================================================================
# The encoding half of the project, refactored out of your Week 1-6 script
# (Week 7 stretch). It imports the shared data and exposes two functions.
# =============================================================================
from morse_codebook import ENCODE_MAP


def encode_char(character):
    """Return the Morse pattern for a single character, or '?' if unknown."""
    return ENCODE_MAP.get(character.upper(), '?')


def encode_message(message):
    """Return a list of Morse patterns for a message string.

    Spaces become ' ' (a word gap); unknown characters become '?'.
    """
    encoded = []
    for character in message.upper():
        if character == ' ':
            encoded.append(' ')
        else:
            encoded.append(ENCODE_MAP.get(character, '?'))
    return encoded
