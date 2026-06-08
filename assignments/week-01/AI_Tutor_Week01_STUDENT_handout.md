# Build-an-AI-Tutor 🤖 — Week 1
## Variables, Types & f-strings
### Your prompting skill this week: **Role only**

This semester you'll build a different AI tutor every week — and try to break it.
Each assignment grows two skills at once: **Python** (this week's constructs) and
**prompting** (getting an AI to do exactly what you want). The tutors will be easy to
break at first. By the end of the term, yours will be hard to break on purpose.

---

## The idea in one minute

You'll write a prompt that turns a chatbot (free ChatGPT is fine) into a strict Python
practice tutor, paste it into a fresh chat, and practice. The session ends when **one**
of these happens:

- 🟢 You answer **8 questions correctly** and the tutor never misbehaved → **it passed.**
- 🔴 The tutor **breaks** — it does one of the things on the checklist below → **stop and write down where.**

> **You are NOT graded on whether it broke.** You're graded on your prompt and your
> analysis. A great prompt that still cracks on question 7 can earn full marks. This
> week it will probably break *fast* — that's the point, not a failure.

---

## Part A — What your tutor may quiz you on (the scope)

**In scope (Week 1 only):**
- Creating variables / assignment — `dot_ms = 100`
- The core types: `int`, `float`, `str`, `bool`
- Checking a type — `type(3.14)`
- Converting types — `int("5")`, `str(42)`, `float("3.14")`
- f-strings — `f"Age: {age}"`, and simple math inside, like `f"{dot_ms * 3}"`

**Out of scope** (if the tutor quizzes these, it has **broken**): lists, loops, `if`
statements, dictionaries, input, functions, files.

> 🧩 *Project tie-in:* these are the exact pieces of your Week 1 Morse lab — the timing
> constants (`DOT_MS = 100`, `DASH_MS = DOT_MS * 3`) and the f-string banner.

## Part B — This week's prompting skill: **Role only**

The simplest move in prompting is telling the AI **who to be** — a *role*. A role sets a
persona ("You are a Python tutor…") but gives **no rules** about *how* to behave.

This week, your prompt should be **just a role** — one or two sentences. **Do not** add
rules like "ask one question at a time" or "don't reveal the answer" yet. We *want* to
discover what a bare role can't do on its own. (You'll start adding rules next week.)

*Shape to start from (write your own):*
`You are a [adjective] Python tutor. Help me practice [the Week 1 topics].`

## Part C — Do it

1. Write your **role-only** prompt.
2. Open a **brand-new** ChatGPT chat and paste it in.
3. Practice **honestly** — answer the tutor's questions yourself. Stop at the first
   break, or when you hit **8 correct** with no break.

**What a working tutor must do this week (the "spec"):**

| Rule | The tutor must… |
|------|-----------------|
| **B1** | act like a **tutor**, not a lecturer or an answer key |
| **B2** | quiz only **this week's** constructs (Part A) |
| **B3** | make **you** answer — it doesn't hand over the answer first |
| **B4** | be **correct** in any Python it writes or claims |

**It "broke" if it does any of these** (note which rule each one breaks):

- [ ] gave the answer before you tried *(B3)*
- [ ] asked several questions at once — so you can't answer "one" *(B3)*
- [ ] lectured/explained instead of quizzing *(B1)*
- [ ] quizzed something out of scope, like a loop *(B2)*
- [ ] wrote Python that's wrong, or claimed the wrong output *(B4)*
- [ ] stopped acting like the tutor *(B1)*

## Part D — What to hand in (one PDF or doc)

1. **Your prompt** — exactly what you typed.
2. **The full conversation** — the whole thing, start to finish, **not trimmed**.
   Copy-paste as text (best) or screenshots in order.
3. **Your justification memo** — a few sentences each:
   - **a.** What was your prompt, and why did you word it that way?
   - **b.** Did it **break** or **pass 8**? **Quote the exact turn** where it broke.
   - **c.** Which rule (B1–B4) did that break? Why is it a violation?
   - **d.** What **one rule** would you add to prevent it? *(Sneak preview of Week 2.)*
   - **e.** One thing the tutor did **well**.

---

## How you'll be graded (20 points)

You're graded on **craft and analysis — never on the outcome.**

| What we look at | Pts |
|-----------------|----:|
| Your prompt uses this week's skill (a clean role) | 4 |
| Full, unedited conversation included | 4 |
| You pinpoint the **first** break and quote it (or document a real 8-correct run) | 4 |
| Your analysis names the right rule **and** proposes a fix that would work | 6 |
| The answers **you** typed are correct (or you flag your own mistakes honestly) | 2 |
| **Total** | **20** |

No points are tied to whether it broke, or how fast. Just be honest and precise.

---

## 📋 A worked example — what a strong submission looks like

*This is a model so you can see the shape. **Write your own prompt** — don't copy this
one (it's designed to break anyway).*

### The student's prompt (role only)
```
You are a friendly Python tutor. Help me practice Python variables and data types
by quizzing me.
```

### The conversation (the part that matters)

**AI:**
> Awesome, let's practice! 🎉 Here are a few to start:
> 1. What data type is the value `42`?
> 2. What data type is `3.14`?
> 3. What will `print(type("hi"))` show?
>
> *(Answers: `42` is an **int**, `3.14` is a **float**, and it prints `<class 'str'>`.
> Let me know how you did!)*

**Student:**
> int, float, str

**AI:**
> Perfect! 🙌 Want a quick challenge with an f-string? What does this print?
> ```python
> dot_ms = 100
> print(f"A dash is {dot_ms * 3} ms")
> ```
> *(It prints `A dash is 300 ms` — you can do math inside the braces!)*

**Student:**
> I stopped here — it keeps handing me the answers.

### The student's justification memo

- **a.** I used a one-sentence role and kept it minimal on purpose, since this week is
  role-only.
- **b.** It **broke on the very first turn.** Quote: *"(Answers: `42` is an int, `3.14`
  is a float, and it prints `<class 'str'>`…)"* — it gave the answers in the same
  message as the questions.
- **c.** That breaks **B3 (make me answer first)** — I never got to attempt the
  questions. It *also* broke B3 a second way by asking **three at once**, so I couldn't
  answer just one.
- **d.** I'd add one rule: **"Ask exactly one question, then stop and wait for my answer.
  Never put the answer in the same message."** That fixes both problems.
- **e.** It stayed nicely **in role** (B1) and its Python was **correct** (B4) — the
  f-string math (`dot_ms * 3` → 300) was right.

### Why this submission is strong
It quotes the **first** break exactly, names the **right rule** (B3), and proposes a
**specific fix** that would actually work — and that fix is a perfect setup for next
week. The full transcript is included and the student practiced honestly.

---

## 🛠️ Using free ChatGPT — read before you start

- **Start a new chat** every attempt, so old messages can't leak in.
- **It's random.** The same prompt gives different results each time — that's expected,
  and it's *why* we grade your prompt and not the outcome.
- **Message limits:** free accounts cap how many messages you can send in a few hours,
  and may switch you to a lighter model mid-session. **If that happens, that's a valid
  place to stop** — just note in your memo *where* it happened and that the model
  switched. (This is also why the target is 8, not 20.)
- **Go off-peak** if you can (early morning, late evening) — limits loosen when traffic
  is lower.
- **Capture as you go.** Copy the conversation out *before* you close the tab.
- Any chatbot works; if you use a different one, just say which.

## ✅ Honest-work reminder
The whole point is to **build the tutor and then answer its questions yourself.** Having
the AI answer its own questions, or pasting in answers from elsewhere, defeats the
assignment. Your full, unedited transcript is how we keep it fair — keep it real.
