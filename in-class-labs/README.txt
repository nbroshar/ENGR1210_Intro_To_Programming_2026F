ENGR1210 — Morse Code Translator Course
Standalone-first lab sequence + Bug of the Week + Hardware bring-up
==============================================================================

HOW THE COURSE IS STRUCTURED
------------------------------------------------------------------------------
Weeks 1-6 build the translator as ONE standalone script, using only that
week's Python lesson -- no functions, no imports, and
the "LED" is just a print() line. Week 7 is "The Great Refactor": students
turn that working script into functions and modules, and meet the Hardware
Abstraction Layer (HAL). Week 8 adds files and exceptions and wires everything
together. The protocol week is the capstone -- a sender/receiver handshake.

THE FULL 16-WEEK ARC IS IN  ->  COURSE_MAP.md  (read that first; it's the master
plan). In short, the project climbs a three-stage ladder over the semester:
  STAGE 1  Weeks 1-9    Build the SIMULATED translator (learn Python + debugging)
  STAGE 2  Weeks 10-12  Bring it up in the WOKWI emulator
  STAGE 3  Weeks 13-16  Bring it up on REAL HARDWARE (the last month)
Weeks 1-8 are unchanged and still mirror the Bug-of-the-Week concepts. Weeks
9-16 are the protocol capstone, then the emulator and hardware stages.

Each week also has a "Bug of the Week" file (bug_weekN.py): a short program
with 4 planted bugs that teaches a debugging method (read the error, fix one
thing, rerun), escalating from console errors to the debugger to unit tests.

THE HARDWARE LADDER (the HAL makes this possible)
------------------------------------------------------------------------------
Once the HAL exists (Week 7), the same code runs three ways, changing ONE line:
  Rung 1  STUB      import hal_stub as hw   -> PC, prints "[LED] ON/OFF"
  Rung 2  EMULATOR  import hal_pico as hw   -> Wokwi simulated Pico (no board)
  Rung 3  REAL      import hal_pico as hw   -> a physical Raspberry Pi Pico

Once the HAL exists (Week 7), do the bring-up in Stage 2: week-10 runs the
project in Wokwi (Rung 2), and week-13 runs the same project on a real Pico
(Rung 3). Stage 1 stays on the PC stub.

WHAT'S IN EACH FOLDER
------------------------------------------------------------------------------
  week-01 .. week-06   weekN_lab.py        (the in-class lab)

  week-07              week7_lab.py        (a WORKING monolith students take
                                            APART, step by step)
                       hal_stub.py, hal_pico.py   (the HAL pair -- provided;
                                            hardware code is not "extracted")
                       bug_week7.py, test_week7.py
                       --> Students CREATE morse_codebook.py, morse_encoder.py,
                           and morse_decoder.py during the lab by cutting code
                           out of week7_lab.py. 

  week-08              week8_lab.py
                       morse_codebook.py, morse_encoder.py, morse_decoder.py,
                       hal_stub.py, hal_pico.py    (so the lab runs out of box)
                       

  week-09              protocol_lab.py  -- the sender/receiver handshake
                       capstone (Stage 1, still simulated).
                       morse_codebook.py, morse_encoder.py, morse_decoder.py,
                       hal_stub.py, hal_pico.py

  --- STAGE 2 (Wokwi emulator) -------------------------------------------------
  week-10              The bring-up project, run on Wokwi (Rung 2). A self-
                       contained Pico project: blink_test.py, main.py,
                       diagram.json, hal_stub/hal_pico, the morse_* modules,
                       hardware_bringup.md, and START_HERE.txt. (The SAME folder
                       is reused as week-13 for Rung 3 on a real board.)

  week-11              week11_lab.py  -- send a message on a button press.
                       hal_pico + morse_encoder + morse_codebook + diagram.json.
                       In Wokwi, the lab file is your main.py. Add the button in
                       the editor (wiring is in the lab header).

  week-12              week12_lab.py  -- RECEIVE by timing a button: the full
                       time -> classify -> assemble -> decode pipeline.
                       morse_decoder + morse_codebook + diagram.json.

  --- STAGE 3 (real hardware) --------------------------------------------------
  week-13              The SAME bring-up project as week-10, now on a REAL Pico
                       (Rung 3): flash MicroPython, run blink_test.py, then
                       main.py. START_HERE.txt says exactly what to do.

  week-14              week14_lab.py  -- optical receiver: a light sensor (LDR
                       into GP26/ADC0) replaces the button; SAME decode logic.
                       morse_decoder + morse_codebook.

  week-15              week15_tx.py + week15_rx.py  -- the two-board link.
                       Data is WIRELESS (LED -> light sensor); the SR/RR
                       handshake is WIRED (+ shared GND). Read week15_link_guide.md
                       FIRST -- it has the wiring table and bring-up order.
                       Includes all modules + hal_pico for both boards.

  week-16              week16_capstone.md  -- integration, a 9-test plan (incl.
                       error injection), a single-board loopback fallback, the
                       demo checklist, and acceptance criteria.

  course-materials     engr1210_python_cheatsheet.pdf   (one-page reference)

  

NOTES
------------------------------------------------------------------------------
- The module + HAL files repeat in week-08, week-09, and the bring-up/hardware
  because Python (and the Pico) imports a module from the same folder as the
  running script. Normally students carry forward the versions THEY built in
  Week 7; known-good copies are included so a rough Week 7 never blocks later
  work.

- hal_pico.py uses MicroPython's machine/utime modules, which exist ONLY on the
  Pico (and in Wokwi). Importing it on a PC raises "No module named 'machine'"
  -- that error IS the PC/hardware boundary the HAL draws. PC code uses
  hal_stub; hardware code uses hal_pico.

- The Stage 2/3 labs (weeks 10-16) are MicroPython. Their pure logic (encode,
  decode, classify, framing) is verified on a PC, and the files are syntax-
  checked, but pins/ADC/light/wiring can only be confirmed by running them in
  Wokwi or on a real Pico. Treat the first Wokwi run as the real test.

RUNNING
------------------------------------------------------------------------------
  Labs and bug files (PC):  open the folder in VS Code and press F5.
  Unit tests:               in that folder, run  python -m pytest test_week7.py -v
  Hardware:                 follow week-10/hardware_bringup.md (Wokwi),
                            then week-13 on a real Pico
==============================================================================
