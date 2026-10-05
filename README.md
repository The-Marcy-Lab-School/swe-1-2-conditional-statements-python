# Conditional Statements

Practice branching with `if` / `elif` / `else`, guard clauses, and conditional
expressions.

**Practicing:** conditionals, branch order, truthy and falsy, guard clauses

- [AI Use on This Assignment](#ai-use-on-this-assignment)
- [Setup](#setup)
- [Before You Start](#before-you-start)
- [From Scratch](#from-scratch)
  - [Question 1: `measure_rain`](#question-1-measure_rain)
  - [Question 2: `happy_birthday_pet`](#question-2-happy_birthday_pet)
  - [Question 3: `describe_cart`](#question-3-describe_cart)
  - [Question 4: `greet_by_nickname`](#question-4-greet_by_nickname)
  - [Question 5: `label_temperature`](#question-5-label_temperature)
- [Modify](#modify)
  - [Question 6: `wildly_biased_review`](#question-6-wildly_biased_review)
  - [Question 7: `get_weather_report`](#question-7-get_weather_report)
- [Debug](#debug)
  - [Question 8: `coolness_gauge`](#question-8-coolness_gauge)
  - [Question 9: `funko_pop_addiction_level`](#question-9-funko_pop_addiction_level)
  - [Question 10: `return_positive_negative_zero`](#question-10-return_positive_negative_zero)
- [Bonus: match statements](#bonus-match-statements)
- [Submitting](#submitting)
- [Good luck!](#good-luck)

## AI Use on This Assignment

Use whichever mode matches where you are with this material. Both are fine,
and most people move between them as a concept clicks.

**Tutor mode.** The AI explains, questions, quizzes, and critiques, and you
write every line you submit. For this assignment that means asking it why one
branch runs instead of another, or having it quiz you on which values are
falsy until you can list them from memory. Ask it a hundred questions — that
is the whole point. What you do not do is ask it for the function. Paste this
at the start of a chat and it will hold for the rest of the conversation:

> You are acting as a tutor. Your job is to explain what this coding question
> is asking, clarify confusing wording, and highlight the relevant concepts I
> need to know — but do not provide the full solution or code that directly
> answers the question. Instead, rephrase the problem in simpler terms,
> identify what is being tested, and suggest what steps or thought processes
> might help. Ask me guiding questions to make sure I am thinking critically.
> Do not write the final function, algorithm, or code implementation.

**Implementer mode.** You write a specification first, the AI writes code from
it, and then you verify that code line by line. For this assignment your spec
has to list every branch and the exact value it returns, including the one
that catches everything else. If what comes back does more than you asked for,
reject it — over-delivery is a defect, and catching it is part of the job.

You own every line either way, and you will be asked to explain it.

## Setup

Work in `development/mod-1`. Make a draft branch before you start.

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
git checkout -b draft
```

Run `pytest` for everything, or `pytest -k measure_rain` for one question.
Every push runs the tests on GitHub and reports your score in the **Actions**
tab.

75% of tests passing counts as complete. Submit at that point even if it is
not perfect. Treat submitting as a checkpoint rather than a finish line, and
come back to improve it.

## Before You Start

Every question here is a function that takes parameters and returns a value,
and two of them need a parameter with a default value. Those are not the new
material. Shore them up first if either feels shaky, because fighting the
syntax and the branching at the same time is twice the work.

Most of these questions **return** a value rather than printing one. Printing
shows a human something; returning hands the value back to your code. A
function that prints where the test expects a return will fail every time,
and the failure message will look confusing.

Two questions do print, and they say so.

**Order decides everything.** Python checks the branches of an `if` / `elif`
chain from the top and stops at the first one that is true. A branch placed
after a broader one that already matches can never run, no matter what you
pass in. Two questions here turn on exactly that.

Python also treats some values as **falsy**, meaning they act like `False` in
a condition: `0`, `0.0`, `""`, `None`, and every empty collection. Everything
else is **truthy**. That is what lets `if not items:` stand in for "the list
is empty".

## From Scratch

Write your solutions in `src/from_scratch.py`.

### Question 1: `measure_rain`

Write a function `measure_rain` that takes a single argument, a number
`inches`. It should return a message depending on the number of inches:

- 0 inches — `"drought"`
- less than 2 inches — `"dry"`
- less than 4 inches — `"average"`
- less than 6 inches — `"rainy"`
- 6 or more inches — `"flood"`

Hint: every band after the first is "less than" something, so a value that
belongs in a later band also satisfies the earlier tests. Which order keeps
that from happening?

### Question 2: `happy_birthday_pet`

Write a function `happy_birthday_pet` that takes two arguments, a string
`breed` and a number `age`. It should return a message in these situations:

- `"snake"`, any age — `"Hiss hiss!"`
- `"cat"`, less than 5 — `"Mew mew!"`
- `"cat"`, 5 or more — `"Meow meow!"`
- `"dog"`, less than 5 — `"Arf arf!"`
- `"dog"`, 5 to less than 10 — `"Woof woof!"`
- `"dog"`, 10 or more — `"Boof!"`
- anything else — `"Happy birthday!"`

Two things decide the answer here, the breed and the age, and only the dog
needs all three age bands.

### Question 3: `describe_cart`

Write a function `describe_cart` that takes a list `items` and a string
`owner` that defaults to `"Your"`. It should return a sentence describing
the cart.

```python
describe_cart([])
# "Your cart is empty."
describe_cart(["apple"])
# "Your cart has 1 item."
describe_cart(["apple", "pear"])
# "Your cart has 2 items."
describe_cart(["a", "b", "c"], "Ada's")
# "Ada's cart has 3 items."
```

Watch the last word. One item is an `item`, and anything else is `items`.

Recall: `owner` needs a default value, because the tests call this with only a
list. An f-string is the tidiest way to build the sentence.

### Question 4: `greet_by_nickname`

Write a function `greet_by_nickname` that takes a string `name` and a string
`nickname` that defaults to `None`. It should return a greeting.

```python
greet_by_nickname("Ada")
# "Hello, Ada!"
greet_by_nickname("Ada", "Ace")
# "Hello, Ace!"
greet_by_nickname("Ada", "")
# "Hello!"
```

Read those three carefully. Leaving the nickname out and passing an empty
nickname give different answers, so the function has to tell "nobody gave me
one" apart from "somebody gave me an empty one".

Hint: `None` and `""` are both falsy, so `if not nickname:` cannot separate
them. What test asks specifically whether a value is `None`?

### Question 5: `label_temperature`

Write a function `label_temperature` that takes a number `celsius` and returns
`"warm"` when it is 20 or above and `"cold"` otherwise.

```python
label_temperature(20)
# "warm"
label_temperature(19)
# "cold"
```

Write it as a **conditional expression**, which chooses between two values on
one line. The test checks that the body is a single `return`.

```python
color = "green" if light_is_on else "red"
```

## Modify

### Question 6: `wildly_biased_review`

Rewrite `wildly_biased_review` so it uses a guard clause. Keep the behavior
exactly the same.

A **guard clause** is an `if` statement that returns before the rest of the
code gets to execute. Used well, it saves you from writing `else` or `elif`
at all. Here, handle the boring case first and `return`, so the NYC case runs
without an `else` wrapped around it. The tests check the `else` is gone.

### Question 7: `get_weather_report`

Refactor `get_weather_report` so it stops repeating itself. It builds a
`weather_report` string, prints it, then prints `"And that's your report!"` —
and it does both of those in every single branch.

Make each of those lines appear **once**. The branches should decide what the
message *is*, not do the printing.

Running it with a temperature between 32 and 70 prints nothing at all right
now, which is a second thing the tests will have an opinion about.

## Debug

### Question 8: `coolness_gauge`

`coolness_gauge` uses a conditional expression and gets the wrong answer for
every number it is given. Read the tests to see which message goes with which
number.

More than the two messages needs to change.

### Question 9: `funko_pop_addiction_level`

Oh man. `funko_pop_addiction_level` takes a number of Funko Pops and returns a
message of support, or concern. However, no matter what you pass it, it only
ever returns the first two messages.

Work out why the later branches can never be reached. Putting them in a
working order brings most of the messages back, and the tests will show you
which boundary is still missing after that.

> Not sure what a Funko Pop is? Just google it.

### Question 10: `return_positive_negative_zero`

Someone got *real* clever here and chained conditional expressions together.
The comparisons are inverted, so `return_positive_negative_zero(5)` hands back
`"Negative"`. Chaining the inline `if`s also makes the mistake easy to miss,
because a reader has to hold all three conditions in their head at once to work
out which value comes back for a given number.

Fix the logic, and unnest it. The tests check that no single line contains
more than one inline `if`.

## Bonus: match statements

Not scored. Do them anyway.

You may already have come across the
[match statement](https://www.w3schools.com/python/python_match.asp), which
Python added in 3.10 as an alternative to a long `if`/`elif` chain. If the
mood strikes you, try your hand at the match versions of `measure_rain_match`
and `rounder_match` in `src/bonus_match.py`.

To test your code, open `tests/test_bonus_match.py` and remove the
`@pytest.mark.skip` line above each test.

[This is a good article on `match`](https://realpython.com/structural-pattern-matching/)
to check out.

`match` is at its best comparing one value against fixed options, so one of
these two will suit it far better than the other. Notice which. HmmmmMMMMmmm?

## Submitting

```sh
git add -A
git commit -m "your message"
git push
```

Pushing runs the tests on GitHub. Check the **Actions** tab for your score,
then open a pull request to your instructor for feedback.

## Good luck!

Branching is most of what programs do. Once the order of your conditions stops
surprising you, a lot of bugs stop happening. You got this!
