# hal_pico.py
# =============================================================================
# Hardware Abstraction Layer (HAL) — REAL HARDWARE version (MicroPython).
#
# This is the twin of hal_stub.py. It has the SAME function names, so the rest
# of the project doesn't change at all — you only change ONE import line:
#
#       import hal_stub as hw      # PC: prints "[LED] ON" / "[LED] OFF"
#       import hal_pico as hw      # Pico / Wokwi: blinks a REAL LED
#
# WHERE THIS RUNS:
#   - In the Wokwi simulator (wokwi.com) on a simulated Raspberry Pi Pico.
#   - On a physical Raspberry Pi Pico flashed with MicroPython.
#   The SAME file works in both places — only WHERE it runs changes.
#
# WHERE THIS DOES *NOT* RUN:
#   - Your laptop's normal Python (CPython). The "machine" and "utime"
#     modules below only exist in MicroPython on the Pico. If you import this
#     on your PC you'll get "ModuleNotFoundError: No module named 'machine'".
#     That error is the whole point of the HAL: PC code uses hal_stub,
#     hardware code uses hal_pico.
# =============================================================================

from machine import Pin
import utime
import sys

# Which pin drives the LED.
#   "LED"  -> the onboard LED. Works on the Pico, the Pico W, and in Wokwi,
#             with no wiring at all. (On a standard Pico this is GPIO 25.)
#   a number, e.g. 15 -> an EXTERNAL LED you wired to that GPIO through a
#             ~330 ohm resistor to ground. Use this for a breadboard LED.
LED_PIN = "LED"

_led = Pin(LED_PIN, Pin.OUT)


def set_led(on):
    """Turn the LED on (True) or off (False)."""
    _led.value(1 if on else 0)


def sleep_ms(milliseconds):
    """Pause for a number of milliseconds (real time on the Pico)."""
    utime.sleep_ms(milliseconds)


def set_led_timed(on, milliseconds):
    """Set the LED, then hold that state for the given time — one symbol step."""
    set_led(on)
    sleep_ms(milliseconds)


def get_board_info():
    """Identify which HAL is running. The PC stub returns a different string,
    so you can prove at a glance which layer is active."""
    return "Pi Pico (" + sys.platform + ", hal_pico)"
