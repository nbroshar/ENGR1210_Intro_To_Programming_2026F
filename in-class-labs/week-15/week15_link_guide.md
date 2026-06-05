# Week 15 — Two-Board Link: Wiring & Bring-Up Guide

Two Picos. One sends, one receives. The message travels on **light**; the
"are we both ready?" coordination travels on **wires**. Keeping data and
control on separate channels is exactly how real links are built.

```
        WIRELESS DATA (light)
   TX LED  ) ) ) ) ) ) ) ) >  RX light sensor
   [Pico A]                    [Pico B]
   SR out GP16 --------------> SR in  GP16     (sender says "sending")
   RR in  GP17 <-------------- RR out GP17     (receiver says "ready")
   GND  <===========================>  GND     (REQUIRED shared ground)
```

## Parts & wiring

**The data channel (wireless):**
- TX board: the LED `hal_pico` already drives (onboard, or an external LED on a
  GPIO). Point it at the receiver's sensor, close, and shield from room light.
- RX board: the light sensor from Week 14 — LDR + 10k divider into GP26 (ADC0).

**The control channel (3 wires between the boards):**
| Signal | Driven by | Read by | TX pin | RX pin |
|--------|-----------|---------|--------|--------|
| SR (sending)  | TX | RX | GP16 (out) | GP16 (in) |
| RR (ready)    | RX | TX | GP17 (in)  | GP17 (out) |
| GND (common)  | —  | —  | any GND    | any GND |

> The shared GND wire is not optional. Two boards with separate grounds have no
> common reference, so a "high" on one means nothing to the other. Tie their
> grounds together first, every time.

Both read pins use an internal **pull-down**, so a disconnected wire reads 0
(= "not ready" / "not sending") — the safe default.

## The handshake (what the wires are saying)

```
  RX: RR = 1  ("I'm ready")
  TX: sees RR=1  ->  SR = 1  ("I'm sending")  ->  blinks START + message + END
  RX: sees SR=1  ->  reads the light, rebuilds the frame, checks START/END
  RX: RR = 0  ("got it / busy")  ->  prints message  ->  RR = 1  ("ready again")
  TX: sees RR go 0 then 1  ->  that's the ACK  ->  sends the next frame
```

## Bring it up in this order (don't skip)

1. **Grounds first.** Wire TX GND to RX GND.
2. **Handshake wires only (the ANCHOR step in both programs).** Comment out the
   optical send/receive; just drive/read SR and RR and print them. Confirm the
   sender only acts after the receiver asserts RR, and the receiver sees SR go
   high. If this doesn't work, it's the wires or the ground — fix it before
   adding light.
3. **Add the light (GUIDED).** Calibrate the sensor threshold (Week 14), aim the
   LED, then run the real `transmit_frame` / `receive_frame`. Send a short
   message like "SOS".
4. **ACK + errors (EXTENSION).** Turn on the RR-drop ACK on both sides; block
   the light mid-message and confirm the receiver reports a frame error instead
   of garbage.

## Common gotchas
- No shared GND -> nothing works, intermittently. (Check this first, always.)
- Sensor sees room light -> everything reads "lit." Shield it; re-calibrate.
- Taps/blinks too even -> dots and dashes blur. Keep dash clearly ~3x a dot.
- Receiver started too late and missed START -> the sender's 300 ms pause after
  SR helps; if needed, increase it.
