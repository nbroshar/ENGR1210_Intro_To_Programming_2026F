# blink_test.py
# =============================================================================
# SMOKE TEST — run this FIRST, before anything else on the board.
#
# It does the simplest possible thing: blink the onboard LED once per second
# and print a count to the console. Its ONLY job is to answer one question:
#
#       "Is my board (or Wokwi) and its MicroPython actually working?"
#
# If the LED blinks AND you see numbers appear in the console, then the board,
# the firmware, and your file upload all work -- move on to main.py.
#
# If it does NOT blink, fix THAT first. Do not try to debug the translator on
# top of a board that isn't running. Bringing a board up with a blink test
# before any real code is what every embedded engineer does on day one.
#
# This file imports NO project modules on purpose: if it fails, you KNOW the
# problem is the board/firmware/upload, not your translator code.
# =============================================================================

from machine import Pin
import utime

# Onboard LED — works on the Pico, the Pico W, and in Wokwi with no wiring.
# For an external LED on a breadboard, use its GPIO number, e.g. Pin(15, Pin.OUT).
led = Pin("LED", Pin.OUT)

count = 0
while True:
    led.value(1)            # LED on
    utime.sleep_ms(500)
    led.value(0)            # LED off
    utime.sleep_ms(500)
    count += 1
    print("blink", count)   # proof of life in the console
