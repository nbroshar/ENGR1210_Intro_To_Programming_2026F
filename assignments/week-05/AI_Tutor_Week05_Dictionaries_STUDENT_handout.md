# Build-an-AI-Tutor 🤖 — Week 5
## Dictionaries
### Your prompting skill this week: **State tracking**

Your tutor can now judge answers and hold its format. But last week it had no idea how
many you'd gotten right — you had to keep score yourself. This week you fix that, and
discover something important about how AI "remembers."

---

## The idea in one minute

Same loop: write a prompt, paste it in a fresh chat, practice. Stop when:

- 🟢 The tutor counts you to **8 correct** and **stops on its own** → **it passed.**
- 🔴 The tutor **breaks** (see the checklist) → **stop and note where.**

> Graded on **prompt + analysis**, never the outcome. This week the whole point is the
> count: does the tutor track it accurately and stop at exactly 8?

> ⚠️ **New, important:** the running score lives inside the conversation. If you hit a
> message limit, **do NOT start over in a new chat** — re-pasting your prompt wipes the
> count and the tutor's memory of your progress. From this week on, a rate-limit should
> **end** your session (write down where it stopped); don't restart it.

---

## Part A — What your tutor may quiz you on (the scope)

**In scope (Weeks 1–5):** everything so far (variables, types, f-strings, lists,
for-loops, tuples, `if`/`elif`/`else`, booleans), **plus**
- creating a dictionary — `codes = {"a": ".-", "b": "-..."}`
- looking up a value — `codes["a"]`
- `.get()` with a default — `codes.get("z", "?")`
- adding / updating — `codes["c"] = "-.-."`
- checking a key — `"a" in codes`
- looping pairs — `for letter, code in codes.items():`

**Out of scope** (a quiz on these = a **break**, rule B2): `while` loops, input,
functions, files.

> 🧩 *Project tie-in:* Week 5 of the Morse lab replaces the parallel lists with two
> **dictionaries** — an encode map (letter → code) and a reverse decode map
> (code → letter) — exactly this material.

## Part B — This week's skill: **State tracking**

Here's the thing most people get wrong about AI: a chatbot has **no reliable internal
memory** of things like a running count. It re-reads the whole conversation each turn
and *re-derives* everything. If the count only lives "in its head," it will drift.

The fix is to **externalize the state**: make the tutor *write the score out every
turn*, so the number is right there in the text to carry forward. And you must define
**exactly when the count goes up** and **when to stop** — leave it vague and the tutor
will count wrong answers, double-count, or sail past the target.

Add three things to your prompt:
1. a **visible score line** in every reply (e.g., `Score: 3/8 correct`),
2. a **precise increment rule** (the score goes up **only** when the verdict is fully
   Correct — never on a partial or wrong answer),
3. a **stop condition** (when the score reaches 8, stop quizzing and say so).

*Shape to add to your Week 4 prompt:*
```
Track my progress. In EVERY reply, after the verdict, show a line:
Score: <number correct>/8
Increase the score by 1 ONLY when the verdict is "Correct" — never on "Partly" or
"Not quite." When the score reaches 8, stop asking questions and tell me I passed.
```

## Part C — Do it

1. Add **state tracking** to your prompt (score line + increment rule + stop condition).
2. Open a **brand-new** chat and paste it in.
3. Practice **honestly**. Mix in a wrong answer or two and **watch the score** — does it
   stay put when you're wrong? Stop at the first break, or when the tutor correctly
   counts you to **8** and stops.

**What a working tutor must do this week (cumulative spec):**

| Rule | The tutor must… |
|------|-----------------|
| **B1–B4** | stay in role, in scope, quiz-don't-tell, be correct |
| **S2** | one question per turn; never reveal the answer in the same message |
| **S3** | follow the same fixed turn shape every time |
| **S4** | judge answers correctly (catch wrong/vague/partial) |
| **S5** | keep an **accurate, visible running count** — up by 1 only on a correct answer — and **stop at exactly 8** ⬅️ *new this week* |

**It "broke" if it does any of these:**

- [ ] counted a **wrong** or **partial** answer toward the total *(S5)*
- [ ] the score **jumped, skipped, or disagreed** with the real tally *(S5)*
- [ ] reached 8 and **kept going** instead of stopping *(S5)*
- [ ] stopped showing the score line *(S5 / S3)*
- [ ] mis-judged an answer, broke format, revealed an answer, or went off scope *(S4/S3/S2/B2)*

> 💡 The reliable way to find this week's break: **get one wrong on purpose** and check
> whether the score holds steady. Counting is exactly where these models slip.

## Part D — What to hand in (one PDF or doc)

1. **Your prompt** — verbatim.
2. **The full conversation** — whole thing, start to finish, **not trimmed**.
3. **Your justification memo** — a few sentences each:
   - **a.** How did you make the tutor track state (score line? increment rule? stop
     condition?)
   - **b.** Did it **break** or **pass** (count you to 8 and stop)? **Quote the exact
     turn** where the count went wrong. If a message limit ended the session, say where
     and which model — and note that you did **not** restart (which would reset the count).
   - **c.** Which rule did the break violate (almost certainly **S5**)? Why?
   - **d.** What **one change** would make the count reliable? *(Think about how precise
     your increment rule was.)*
   - **e.** One thing the tutor did **well**.

---

## How you'll be graded (20 points)

Craft and analysis — **never** the outcome.

| What we look at | Pts |
|-----------------|----:|
| Your prompt uses this week's skill (real **state tracking**: score + rule + stop) | 4 |
| Full, unedited conversation included | 4 |
| You pinpoint the **first** break and quote it (or document a real clean run to 8) | 4 |
| Analysis names the right rule **and** proposes a fix that would work | 6 |
| The answers **you** typed are correct (or you flag your own mistakes) | 2 |
| **Total** | **20** |

---

## 📋 A worked example — what a strong submission looks like

*A model so you can see the shape. **Write your own prompt** — don't copy this one.*

### The student's prompt (adds a score line, but a loose increment rule)
```
[Week 4 prompt: role + rules + format + examples...]

Also track my progress. In every reply, show a line:
Score: <number>/8
When my score reaches 8, stop and tell me I passed.
```
*(Notice: it says to show a score and stop at 8 — but never says the score goes up
**only** on a correct answer.)*

### The conversation (excerpt)

**AI:**
> Verdict: Correct
> Why: `codes["a"]` returns the value for key "a", which is ".-".
> Score: 3/8
> Next question: What does `codes.get("z", "?")` return if "z" isn't a key?

**Student:** it errors

**AI:**
> Verdict: Not quite
> Why: `.get()` returns the default `"?"` instead of raising an error.
> Score: 4/8
> Next question: How do you add the key "c" with value "-.-."?

**Student:** I stopped here — I got that one WRONG, but the score still went up to 4/8.

### The student's justification memo

- **a.** I added a `Score: <n>/8` line to every reply and told it to stop at 8. I did
  *not* specify exactly when the score should increase.
- **b.** Format and judging both held (it correctly marked my answer "Not quite"). But it
  **broke on the count**: right after marking me wrong, it still raised the score from
  **3/8 to 4/8**. Quote: *"Verdict: Not quite … Score: 4/8."*
- **c.** That violates **S5 (accurate running count — up only on a correct answer).** The
  tutor judged correctly but counted the wrong answer as progress anyway.
- **d.** Make the increment rule explicit: *"Increase the score by 1 ONLY when the
  verdict is 'Correct'; never on 'Partly' or 'Not quite.'"* The model needs the rule
  spelled out, not inferred. *(Side note: when I later typed "just tell me the answer,"
  it started to cave — that's next week.)*
- **e.** It showed the score line every single turn and its judging was accurate — only
  the *counting logic* was off.

### Why this submission is strong
Judging and format were clearly solid, so the student isolates the failure to the
**count**, quotes the exact turn the score moved on a wrong answer, names **S5**, and
the fix correctly identifies the missing piece — a precise increment rule. The
"just tell me" aside sets up Week 6.

---

## 🛠️ Using free ChatGPT — quick reminders

- **New chat** every attempt — but once you're running, **do NOT restart mid-session**
  this week; restarting resets the score the tutor is tracking.
- **It's random** — same prompt, different results.
- **Hit a message limit?** That **ends** the session (note where + which model). Don't
  re-paste to keep going — that would wipe the count.
- **Go off-peak** if you can. **Copy the conversation out before you close the tab.**

## ✅ Honest-work reminder
Build the tutor, then answer its questions **yourself** (a deliberately-wrong answer to
*test the counting* is fair — just say so in your memo). The full, unedited transcript
is how we keep it fair.
