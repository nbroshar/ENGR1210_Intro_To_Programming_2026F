# Hardware Bring-Up — From Stub to Emulator to Real Pico

This session happens right after the Week 7 refactor, once the project has a
**HAL** (`hal_stub.py`). The HAL is what makes hardware possible: the rest of
the code never talks to a pin directly, so we can change *where the LED lives*
by changing **one import line**.

You will climb three rungs. The code you run is nearly identical on all three —
that is the whole lesson.

```
Rung 1: STUB        import hal_stub as hw     runs on your PC (prints)
Rung 2: EMULATOR    import hal_pico as hw     runs in Wokwi (simulated LED)
Rung 3: REAL PICO   import hal_pico as hw     runs on a physical board (real LED)
```

Files in this folder:
- `main.py`            — the entry point the Pico/Wokwi runs automatically
- `hal_stub.py`        — PC version of the HAL (prints)
- `hal_pico.py`        — Pico/Wokwi version of the HAL (real pin)
- `morse_codebook.py`, `morse_encoder.py`, `morse_decoder.py` — your modules
- `diagram.json`       — the Wokwi board description


## Rung 1 — Stub (you've already done this)

On your PC, the "LED" is a printed line. Confirm the logic still works:

```
# in main.py, temporarily use the stub:
import hal_stub as hw
```
Run it. You'll see `[LED] ON ... OFF ...` lines spelling out S-O-S. No board,
no emulator — just proof the logic is correct. Real engineers always get the
logic right against a stub first. Then switch the line back to `hal_pico`.


## Rung 2 — Emulator (Wokwi, no hardware needed)

1. Go to **https://wokwi.com** and start a new **MicroPython on Raspberry Pi
   Pico** project (wokwi.com/projects/new/micropython-pi-pico).
2. Wokwi gives you a `main.py` and a `diagram.json`. Replace BOTH with the ones
   in this folder, then **add the rest of the `.py` files** (`hal_pico.py`,
   `morse_codebook.py`, `morse_encoder.py`) using the file menu (the green "+"/
   file tab). Wokwi copies every file into the Pico's flash, so your imports
   work exactly like on your PC.
3. Press the green **Play** button. The Pico's onboard LED blinks `...---...`
   and the console prints the board info + "Transmitting: SOS".
4. The LED is driven by `Pin("LED")`, which is the onboard LED — no wiring
   required. (Want a bigger, more obvious LED? Add a `wokwi-led` part and a
   resistor to a GPIO pin, then set `LED_PIN = 15` in `hal_pico.py`.)

> Same `hal_pico.py` you'll use on the real board. The emulator is just a
> safe, free place to run it first — which is how professionals catch bugs
> before touching hardware.


## Rung 3 — Real Raspberry Pi Pico

**One-time setup: put MicroPython on the board**
1. Hold the **BOOTSEL** button on the Pico while plugging it into USB. It
   mounts as a USB drive called `RPI-RP2`.
2. Download the MicroPython UF2 for the Pico from raspberrypi.com (or export
   the UF2 from Wokwi), and drag it onto that drive. The Pico reboots running
   MicroPython.

**Copy your files onto the board** (either tool works):
- **Thonny** (easiest): Tools -> Options -> Interpreter -> MicroPython
  (Raspberry Pi Pico). Open each file and "Save as -> Raspberry Pi Pico." Save
  the entry file as `main.py`. Reset the board and `main.py` runs on power-up.
- **mpremote** (command line): `pip install mpremote`, then from this folder:
  ```
  mpremote connect auto cp hal_pico.py morse_codebook.py morse_encoder.py main.py :
  mpremote connect auto reset
  ```

The onboard LED now blinks `...---...` for real. If you wired an external LED
(GPIO 15 + ~330 ohm resistor to ground), set `LED_PIN = 15` in `hal_pico.py`
and that one blinks instead.


## What to make students notice

- The **only** difference between PC, emulator, and hardware is the line
  `import hal_stub as hw` vs `import hal_pico as hw`. That's abstraction doing
  its job.
- `hal_pico.py` is **identical** in Wokwi and on the real board. The code
  doesn't know or care which one it's on — it just calls `set_led()`.
- Importing `hal_pico` on a PC fails with "No module named 'machine'." That's
  not a bug; it's the boundary between PC code and hardware code made visible.
