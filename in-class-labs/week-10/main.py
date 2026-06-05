# main.py
# =============================================================================
# THE HARDWARE ENTRY POINT.
#
# A Raspberry Pi Pico (and the Wokwi simulator) automatically runs a file
# named main.py when it powers on. So this is the "front door" of the project
# on hardware — the equivalent of the  if __name__ == "__main__":  demo block
# you ran on your PC.
#
# Notice the ONLY hardware-specific thing here is the import line. Everything
# else is the same encode logic you wrote and refactored into modules.
# =============================================================================

import hal_pico as hw                      # <-- the swap. On PC this was hal_stub.
from morse_encoder import encode_message

# Timing (same constants as the PC labs)
DOT_MS        = 100
DASH_MS       = DOT_MS * 3
SYMBOL_GAP_MS = DOT_MS * 1
LETTER_GAP_MS = DOT_MS * 3
WORD_GAP_MS   = DOT_MS * 7


def transmit_pattern(pattern):
    """Blink one letter's pattern, then hold a letter gap."""
    for symbol in pattern:
        if symbol == '.':
            hw.set_led_timed(True, DOT_MS)
            hw.set_led_timed(False, SYMBOL_GAP_MS)
        elif symbol == '-':
            hw.set_led_timed(True, DASH_MS)
            hw.set_led_timed(False, SYMBOL_GAP_MS)
    hw.set_led_timed(False, LETTER_GAP_MS)


def transmit_message(text):
    """Blink a whole message: patterns for letters, silence for word gaps."""
    for item in encode_message(text):
        if item == ' ':
            hw.set_led_timed(False, WORD_GAP_MS)
        else:
            transmit_pattern(item)


print("Board:", hw.get_board_info())
while True:
    print("Transmitting: SOS")
    transmit_message("SOS")
    hw.sleep_ms(1500)        # pause, then repeat forever
