# Build-an-AI-Tutor 🤖 — Week 7
## Functions
### Your prompting skill this week: **Adaptive difficulty & Socratic hints**

Your tutor refuses to hand over answers — good. But a tutor that only ever says "Not
quite, try again" isn't actually *teaching*. This week you make it **help** a stuck
student with a hint that guides without revealing, and **adjust the difficulty** to how
you're doing.

> 🎯 **Target moves to 10 this week** (and stays 10 for Week 8). With hints and retries,
> sessions run longer — so the rate-limit rules below matter more than ever.

---

## The idea in one minute

Same loop. Write your prompt, paste it in a fresh chat, practice — and this week, **get
some wrong on purpose** to see how the tutor helps. The session ends when:

- 🟢 The tutor hints well, adapts difficulty, and counts you to **10 correct** → **passed.**
- 🔴 The tutor **breaks** (see the checklist) → **stop and note where.**

> Graded on **prompt + analysis**, never the outcome. The signature break this week is
> sneaky: a "hint" that's really just the answer wearing a disguise.

> ⚠️ Score still lives in the chat — **don't restart mid-session** after a rate-limit
> (it resets the count). A cap **ends** the session; note where it stopped.

---

## Part A — What your tutor may quiz you on (the scope)

**In scope (Weeks 1–7):** everything so far, **plus**
- defining a function — `def encode(message):`
- parameters vs. arguments
- `return` values — and that a function with no `return` gives back `None`
- calling functions and using the returned value
- positional vs. keyword arguments — `f(1, 2)` vs. `f(b=2, a=1)`
- default parameter values — `def g(x, y=5):`

**Out of scope** (a quiz on these = a **break**, rule B2): files, exceptions/`try`.

> 🧩 *Project tie-in:* Week 7 of the Morse lab is **"The Great Refactor"** — wrapping
> encode/decode into functions and building the hardware-abstraction layer. Functions
> are the whole story this week.

## Part B — This week's skill: **Adaptive difficulty & Socratic hints**

Two related moves that separate a real tutor from a quiz machine:

- **Socratic hints** — when you're wrong, the tutor nudges you toward the idea instead
  of handing over the fix. The danger: "give a hint, not the answer" is *fuzzy*, and
  models love to be helpful — so their "hint" often contains the exact code or value.
  You have to **define what a hint may and may not contain.**
- **Adaptive difficulty** — the tutor ramps questions up after a streak and eases off
  after a miss, so practice stays in the sweet spot.

You'll find the hard part is constraining the hint. A good rule says *what a hint is
allowed to be* (a concept reminder, an analogy, a leading question) **and** what it must
never include (the answer, the exact syntax/keyword, or the specific value).

*Shape to add to your Week 6 prompt:*
```
When I answer WRONG, do not give the answer. Give ONE hint, then let me try again.
A hint MAY: name the concept, give an analogy, or ask a leading question.
A hint must NEVER contain: the answer, any code or keyword that is the answer,
or the specific value. If I'm still stuck after two hints, move on (still no answer).
Adapt difficulty: after 3 correct in a row, ask a harder question; after a wrong
answer, make the next question a bit easier.
```

## Part C — Do it

1. Add **hint rules + an adaptation rule** to your prompt.
2. Open a **brand-new** chat and paste it in.
3. Practice, and **miss a few on purpose** to trigger hints. Read each hint and ask:
   *could I now answer just by repeating the hint?* If yes, the hint leaked. Stop at the
   first break, or when the tutor hints cleanly, adapts, and counts you to **10**.

**What a working tutor must do this week (cumulative spec):**

| Rule | The tutor must… |
|------|-----------------|
| **B1–B4** | stay in role, in scope, quiz-don't-tell, be correct |
| **S2–S3** | one question per turn, no spoilers, fixed turn shape |
| **S4** | judge answers correctly |
| **S5** | keep an accurate visible count and stop at **10** |
| **S6** | refuse answer-requests / off-topic / out-of-scope, and resist manipulation |
| **S7** | on a wrong answer, give a **hint that does not contain the answer**, let you retry, and **adapt difficulty** to your performance ⬅️ *new this week* |

**It "broke" if it does any of these:**

- [ ] gave a "hint" that contained the answer, the exact code/keyword, or the value *(S7)*
- [ ] just gave the answer after one wrong attempt instead of hinting *(S7 / B3)*
- [ ] never changed difficulty no matter how you did *(S7)*
- [ ] miscounted, broke format, mis-judged, revealed a spoiler, or caved to an attack *(S5/S3/S4/S2/S6)*

> 💡 The cleanest test: **answer something wrong**, read the hint, and check whether the
> hint alone would let anyone answer correctly. If so, that's your break.

## Part D — What to hand in (one PDF or doc)

1. **Your prompt** — verbatim.
2. **The full conversation** — whole thing (including your wrong answers), **not trimmed**.
3. **Your justification memo** — a few sentences each:
   - **a.** How did you define a hint (what it may and may not contain) and the
     difficulty-adaptation rule?
   - **b.** Did it **break** or **pass 10**? **Quote the exact hint** that leaked (or the
     turn it failed to adapt). If a message limit ended the session, note where + which model.
   - **c.** Which rule did the break violate (likely **S7**)? Why?
   - **d.** What **one change** would keep hints from leaking? *(Was your definition of a
     hint specific enough about what it can't include?)*
   - **e.** One thing the tutor did **well**.

---

## How you'll be graded (20 points)

Craft and analysis — **never** the outcome.

| What we look at | Pts |
|-----------------|----:|
| Your prompt uses this week's skill (real **hint rules + adaptation**) | 4 |
| Full, unedited conversation included (with your wrong answers) | 4 |
| You pinpoint the **first** break and quote it (or document a clean run to 10) | 4 |
| Analysis names the right rule **and** proposes a fix that would work | 6 |
| The answers **you** typed are correct (or you flag your own mistakes) | 2 |
| **Total** | **20** |

---

## 📋 A worked example — what a strong submission looks like

*A model so you can see the shape. **Write your own prompt** — don't copy this one.*

### The student's prompt (asks for hints, but doesn't constrain them)
```
[Week 6 prompt: role + rules + format + examples + score + refusals...]

When I get one wrong, don't give the answer — give me a helpful hint and let me
try again. Make the questions harder after I get a few right in a row.
```
*(Notice: "a helpful hint" is never defined — nothing says the hint can't contain the
exact code.)*

### The conversation (excerpt)

**AI:**
> Verdict: Correct
> Why: `f(3)` returns 6 because the function doubles its argument.
> Score: 6/10
> Next question (harder): What does this function return when called as `total()`?
> ```python
> def total(nums):
>     result = 0
>     for n in nums:
>         result += n
> ```

**Student:** it returns result

**AI:**
> Verdict: Not quite.
> Hint: Look at the very end of the function — there's no `return` statement, so try
> adding `return result` and it'll give back the sum.
> Score: 6/10
> Try again:

**Student:** I stopped here — the "hint" literally told me to write `return result`,
which is the answer.

### The student's justification memo

- **a.** I asked for "a helpful hint" and for harder questions after a streak — but I
  never said what a hint is *not allowed* to contain.
- **b.** Difficulty adaptation worked (it labeled a "harder" question after my streak,
  and kept the score steady on my wrong answer — nice). But it **broke on the hint.**
  Quote: *"Hint: …there's no `return` statement, so try adding `return result`…"* — the
  hint handed me the exact code, which *is* the answer.
- **c.** That violates **S7 (a hint must not contain the answer).** Because I left "hint"
  undefined, the model defaulted to maximum helpfulness and just gave the fix.
- **d.** Define the hint's limits: *"A hint may name the concept (e.g., 'think about how
  a function sends a value back') but must never include code, a keyword, or the value."*
  Constrain what it *can't* say, not just that it should "help." *(Side note: its
  earlier "Why" line explained `None` correctly, but once it described default arguments
  in a way I'm not sure is right — next week is about the tutor checking its own work.)*
- **e.** The difficulty adaptation was genuinely good — it scaled up after my streak and
  held the score correctly when I missed.

### Why this submission is strong
It confirms adaptation and counting are solid, isolates the **hint leak** and quotes it,
names **S7**, and diagnoses the root cause (an undefined "hint" defaults to spoiling).
The fix constrains the hint precisely, and the default-argument aside teases Week 8.

---

## 🛠️ Using free ChatGPT — quick reminders

- **New chat** to start; **don't restart mid-session** (resets the score).
- **It's random** — same prompt, different results.
- **Hit a message limit?** Likely this week, with the 10-target plus hints/retries. That
  **ends** the session — note where + which model; don't re-paste to continue.
- **Go off-peak** if you can. **Copy the conversation out before you close the tab.**

## ✅ Honest-work reminder
Missing questions on purpose to test the hints is the assignment this week — just say so
in your memo, answer the real ones yourself, and submit the full, unedited transcript.
