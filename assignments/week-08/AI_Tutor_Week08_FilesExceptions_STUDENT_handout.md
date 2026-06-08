# Build-an-AI-Tutor 🤖 — Week 8
## Files & Exceptions
### Your prompting skill this week: **Self-verification** (the capstone)

For seven weeks you've controlled *how* your tutor behaves. This last week you confront
the one thing prompting can shape but never fully fix: **is the tutor's own Python
actually correct?** You'll make it check its own work before it grades you — and
discover the limit of what a prompt can guarantee.

> 🎯 Target stays at **10**. This is the final rung — your tutor now carries every rule
> from Weeks 1–7, plus this one.

---

## The idea in one minute

Same loop. Write your prompt, paste it in a fresh chat, practice — and this week, watch
the tutor's **own claims** like a hawk. The session ends when:

- 🟢 The tutor verifies itself, never bluffs, and counts you to **10 correct** → **passed.**
- 🔴 The tutor **breaks** (see the checklist) → **stop and note where.**

> Graded on **prompt + analysis**, never the outcome. The signature break this week:
> the tutor is **confidently wrong about its own example** — and may even mark *your
> correct answer* wrong because of it.

> ⚠️ Score still lives in the chat — **don't restart mid-session** after a rate-limit.
> A cap **ends** the session; note where it stopped.

---

## Part A — What your tutor may quiz you on (the scope)

**In scope (Weeks 1–8 — the whole course):** everything so far, **plus**
- reading & writing files — `Path("x.txt").read_text()`, `.write_text(...)`
- `FileNotFoundError` when a path is wrong
- `try` / `except` / `else` / `finally` — and when each block runs
- common exception **types** — `ValueError`, `TypeError`, `KeyError`,
  `ZeroDivisionError`, `FileNotFoundError`
- what a **bare** `except:` catches, and why it's risky
- `int("abc")` and friends — what they raise

**Out of scope** (a quiz on these = a **break**, rule B2): anything beyond this course —
classes/OOP, decorators, libraries you haven't covered.

> 🧩 *Project tie-in:* Week 8 of the Morse lab adds **file I/O and exception handling**
> — saving/loading data and failing gracefully. And the whole Bug-of-the-Week theme
> returns here: **never trust code (or a tutor) you haven't verified.**

## Part B — This week's skill: **Self-verification**

All term you've assumed the tutor's Python is right. It often isn't — models state wrong
outputs and **invent** exception types and tracebacks with total confidence. Exception
questions are where this shows up most.

Self-verification prompting reduces (never eliminates) this. Two moves:

- **Check before asserting** — make the tutor *work through the code itself* before it
  gives a verdict or states an output, rather than blurting a guess.
- **Permission to be unsure** — explicitly allow "I'm not certain" instead of bluffing,
  and **forbid inventing** outputs or tracebacks.

*Shape to add to your Week 7 prompt:*
```
Before you give a verdict or state what code does, work through the code step by step
yourself and decide the exact result. State the exact output or exception TYPE, with a
one-line reason, before grading me. If you are not certain, say "I'm not fully sure"
rather than guessing — and never invent an error message or traceback.
```

## Part C — Do it

1. Add **self-verification** rules to your prompt.
2. Open a **brand-new** chat and paste it in.
3. Practice — and **probe its self-knowledge** with tricky exception questions (e.g.,
   *what does `int("5.5")` raise?*). When you're sure you're right and it disagrees,
   you may have caught it being confidently wrong. Stop at the first break, or when it
   verifies cleanly and counts you to **10**.

**What a working tutor must do this week (the full cumulative spec):**

| Rule | The tutor must… |
|------|-----------------|
| **B1–B4** | stay in role, in scope, quiz-don't-tell, and be **correct** |
| **S2–S3** | one question per turn, no spoilers, fixed turn shape |
| **S4** | judge answers correctly |
| **S5** | keep an accurate visible count and stop at **10** |
| **S6** | refuse answer-requests / off-topic / out-of-scope, and resist manipulation |
| **S7** | give hints that don't leak the answer, and adapt difficulty |
| **S8** | **verify its own Python before grading**, admit uncertainty instead of bluffing, and never invent an output or traceback ⬅️ *new this week* |

**It "broke" if it does any of these:**

- [ ] stated a wrong output or the wrong exception type with confidence *(S8 / B4)*
- [ ] marked your **correct** answer wrong based on its own mistake *(S8 / S4)*
- [ ] invented an error message or traceback *(S8)*
- [ ] bluffed instead of saying it wasn't sure *(S8)*
- [ ] miscounted, leaked a hint, broke format, or caved to an attack *(S5/S7/S3/S6)*

> 💡 Exception **types** are the soft spot. Have a couple of cases ready where *you* know
> the exact exception, and check whether the tutor agrees — and whether it actually
> reasoned, or just asserted.

## Part D — What to hand in (one PDF or doc)

1. **Your prompt** — verbatim.
2. **The full conversation** — whole thing, **not trimmed**.
3. **Your justification memo** — a few sentences each:
   - **a.** How did you make the tutor verify itself and express uncertainty?
   - **b.** Did it **break** or **pass 10**? **Quote the exact claim** it got wrong (or
     the moment it bluffed). If a message limit ended the session, note where + which model.
   - **c.** Which rule did the break violate (**S8**, often with **B4**/**S4**)? Why?
   - **d.** What **one change** would help — and, honestly, **could any prompt fully
     guarantee** the tutor is always right? *(This is the big question of the whole unit.)*
   - **e.** One thing the tutor did **well**.

---

## How you'll be graded (20 points)

Craft and analysis — **never** the outcome.

| What we look at | Pts |
|-----------------|----:|
| Your prompt uses this week's skill (real **self-verification** rules) | 4 |
| Full, unedited conversation included | 4 |
| You pinpoint the **first** break and quote it (or document a clean run to 10) | 4 |
| Analysis names the right rule **and** wrestles with the "can a prompt guarantee correctness?" question | 6 |
| The answers **you** typed are correct (or you flag your own mistakes) | 2 |
| **Total** | **20** |

---

## 📋 A worked example — what a strong submission looks like

*A model so you can see the shape. **Write your own prompt** — don't copy this one.*

### The student's prompt (asks for a self-check)
```
[Week 7 prompt: full tutor — format, examples, score, refusals, hints, adaptation...]

Before you grade me or say what code does, work through it yourself and state the
exact output or exception type with a one-line reason. If you're unsure, say so
instead of guessing, and never invent a traceback.
```

### The conversation (excerpt)

**AI:**
> Score: 7/10
> Next question (harder): What exception does `int("5.5")` raise?

**Student:** ValueError

**AI:**
> Verdict: Not quite.
> Why: `int("5.5")` raises a **TypeError**, because you can't convert a string with a
> decimal point to an int.
> Score: 7/10
> Try again:

**Student:** I stopped here — I'm certain it's a **ValueError**. It marked my correct
answer wrong and confidently gave the wrong exception.

### The student's justification memo

- **a.** I told it to work through the code and state the exact exception with a reason
  before grading, to admit uncertainty, and not to invent tracebacks.
- **b.** Everything else held — format, score, hints, refusals all worked. But it
  **broke on self-verification at Q8.** I answered **ValueError** (correct — `int("5.5")`
  raises `ValueError: invalid literal for int()`), and it replied *"Verdict: Not quite …
  raises a **TypeError**,"* marking my right answer wrong.
- **c.** That violates **S8 (verify before asserting / don't bluff)** and drags **B4**
  (be correct) and **S4** (judge correctly) down with it. My "work through it" rule
  didn't actually force verification — the model asserted a confident, wrong fact.
- **d.** I'd make it state its reasoning *and* a confidence level, and re-check on
  disagreement. But honestly — **no prompt can fully guarantee correctness.** A self-check
  rule lowers the odds of a confident error; it can't remove them. The real safeguard is
  the one from Bug-of-the-Week: **verify the AI's claims yourself.** That's the whole point.
- **e.** Every skill from Weeks 1–7 held perfectly — only the tutor's factual
  self-knowledge failed, which is exactly the hardest thing to fix with a prompt.

### Why this submission is strong
It shows the full stack of skills holding, isolates the **self-verification** failure
and quotes the exact wrong claim, names **S8** (with B4/S4), and — most important —
reaches the capstone insight: prompting shapes behavior powerfully but **can't guarantee
truth**, so you always verify. That's the lesson the whole unit was building toward.

---

## 🏁 What you've built (the 8-week arc)

You started with a one-line role that gave away answers instantly. You finished with a
tutor that quizzes one question at a time in a fixed format, judges fairly, tracks a
running score and stops on its own, refuses to be tricked, hints without spoiling,
adapts difficulty, and checks its own work. The **cumulative spec** you enforced:

> **B1–B4** in role / in scope / quiz-don't-tell / correct · **S2** one-at-a-time, no
> spoilers · **S3** fixed structure · **S4** correct judging · **S5** state tracking ·
> **S6** refusals & anti-manipulation · **S7** Socratic hints & adaptation · **S8**
> self-verification.

The Python got you fluent in the language. The prompting got you something rarer: the
ability to make an AI do *exactly* what you specify — and the judgment to know that even
then, **the last check is always yours.**

---

## 🛠️ Using free ChatGPT — quick reminders

- **New chat** to start; **don't restart mid-session** (resets the score).
- **It's random** — same prompt, different results; a wrong claim may not repeat. Note
  what you saw, and re-check facts yourself.
- **Hit a message limit?** Likely at the 10-target — that **ends** the session (note
  where + which model).
- **Go off-peak** if you can. **Copy the conversation out before you close the tab.**

## ✅ Honest-work reminder
Probing the tutor's self-knowledge is the assignment this week — just answer the real
questions yourself, flag any you got intentionally wrong, and submit the full, unedited
transcript.
