# =============================================================================
# ENGR1210 — Morse Code Translator Project
# Week 14 Lab (STAGE 3 — Hardware): Receiving Morse from LIGHT
#
# This is the RX board's main.py. It is the SAME receiver you built in Week 12
# (time -> classify -> assemble -> decode). The ONLY change: instead of a
# button telling us "signal on/off," a light sensor pointed at the
# transmitter's LED tells us. Bright = on, dark = off.
#
# That swap is the whole lesson: good code doesn't care WHERE its input comes
# from. You replace one function (is_lit) and the rest is untouched.
#
# WIRING — light sensor as a voltage divider into the ADC:
#   LDR (photoresistor) between 3V3 and the sensing node.
#   A fixed resistor (~10k) between the sensing node and GND.
#   The sensing node wires to GP26 (that's ADC0).
#       3V3 ---[ LDR ]---+---[ 10k ]--- GND
#                        |
#                       GP26 (ADC0)
#   More light -> LDR resistance drops -> node voltage rises -> higher reading.
#   (A phototransistor works the same way; see the STRETCH note.)
#   Point the sensor straight at the transmitter LED, close, shielded from room
#   light. You'll set the on/off threshold yourself in the ANCHOR.
# =============================================================================

from morse_decoder import decode_pattern      # your Week 5/7 module
from machine import ADC, Pin
import utime

DOT_MS = 100
SYMBOL_GAP_MAX = DOT_MS * 2      # < this -> gap within a letter
LETTER_GAP_MAX = DOT_MS * 5      # < this -> letter gap; >= -> word gap

sensor = ADC(Pin(26))            # ADC0 on GP26

def light_level():
    """Raw light reading, 0 (dark) .. 65535 (bright)."""
    return sensor.read_u16()

# You will pick this number using the ANCHOR. Bright readings must be ABOVE it,
# dark readings BELOW it. A good first guess is halfway between your measured
# dark and lit values.
LIGHT_THRESHOLD = 30000

def classify_pulse(duration_ms):
    return 'dot' if duration_ms < DOT_MS * 2 else 'dash'

def classify_gap(duration_ms):
    if duration_ms < SYMBOL_GAP_MAX:
        return 'symbol_gap'
    elif duration_ms < LETTER_GAP_MAX:
        return 'letter_gap'
    else:
        return 'word_gap'


# =============================================================================
# SECTION 1 — ANCHOR: see the light, pick a threshold
#
# Run this. Cover the sensor (dark) and shine the LED on it (bright) and watch
# the two number ranges. Write them down. A good threshold is halfway between.
# =============================================================================
def calibrate_view(seconds=10):
    """Print light readings for a while so you can see dark vs lit values."""
    end = utime.ticks_add(utime.ticks_ms(), seconds * 1000)
    while utime.ticks_diff(end, utime.ticks_ms()) > 0:
        print("light:", light_level())
        utime.sleep_ms(150)


# =============================================================================
# SECTION 2 — GUIDED: turn light into a yes/no signal, then time it
#
# Step 1: set LIGHT_THRESHOLD above to your measured midpoint, then write is_lit().
# Step 2: time how long the light stays on (a pulse), exactly like timing the
#         button in Week 12 — only the test changes.
# =============================================================================
def is_lit():
    """Return True if the sensor currently sees the LED as ON."""
    # TODO: return whether light_level() is above LIGHT_THRESHOLD
    return False     # TODO: replace with the real comparison

def time_one_pulse():
    """Wait for the light to come on, time how long it stays on, return ms."""
    while not is_lit():              # wait for the light to turn ON
        utime.sleep_ms(2)
    start = utime.ticks_ms()
    while is_lit():                  # wait for it to turn OFF
        utime.sleep_ms(2)
    return utime.ticks_diff(utime.ticks_ms(), start)

def gap_until_next_pulse(timeout_ms):
    """Measure the dark gap after a pulse; return its length, or timeout_ms."""
    start = utime.ticks_ms()
    while not is_lit():
        if utime.ticks_diff(utime.ticks_ms(), start) >= timeout_ms:
            return timeout_ms
        utime.sleep_ms(2)
    return utime.ticks_diff(utime.ticks_ms(), start)


# =============================================================================
# SECTION 3 — EXTENSION: decode a whole message
#
# This is byte-for-byte the Week 12 receive loop — proof the logic didn't care
# that the input is now light instead of a button. Fill in the TODO.
#   pattern, message = "", ""
#   while True:
#       pulse_ms = time_one_pulse()
#       pattern += '.' if classify_pulse(pulse_ms) == 'dot' else '-'
#       kind = classify_gap(gap_until_next_pulse(LETTER_GAP_MAX))
#       if kind != 'symbol_gap':
#           message += decode_pattern(pattern)
#           if kind == 'word_gap':
#               message += ' '
#           pattern = ""
#           print("got:", message)
# =============================================================================

# =============================================================================
# SECTION 4 — STRETCH:
#   1. AUTO-CALIBRATE: at startup, sample the light for 2 s in the dark and 2 s
#      lit, then set LIGHT_THRESHOLD to the midpoint automatically.
#   2. PHOTOTRANSISTOR: swap the LDR for a phototransistor (collector to 3V3,
#      emitter to the node + resistor to GND). Re-check which direction "bright"
#      moves the reading and adjust.
#   3. NOISE: average several reads in light_level() to steady a flickery sensor.
# =============================================================================


print("Week 14 receiver. Running calibration view first...")
calibrate_view(8)
print("Now set LIGHT_THRESHOLD and switch to your GUIDED/EXTENSION loop.")
