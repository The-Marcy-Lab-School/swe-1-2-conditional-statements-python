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

Clone your repository in `development/mod-1` and then `cd` into it. Set up your virtual environment and make a draft branch before you start.

```sh
git clone [your_repo]
cd [your_repo]
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
git checkout -b draft
```

Run `pytest` to test the entire assignment, or `pytest -k measure_rain` for one question.
Every push runs the tests on GitHub and reports your score in the **Actions**.
75% of tests passing counts as complete. Submit at that point even if it is
not perfect. Treat submitting as a checkpoint rather than a finish line, and
come back to improve it.

When you are done working on this assignment, turn off your virtual environment by running:

```sh
deactivate
```

## Before You Start

This assignment has three sections:

1. From Scratch
2. Debug
3. Modify

Every question here is a function that takes parameters and returns a value,
and two functions need a parameter with a default value. Those are not the new
material. If functions still feel shaky, take time to study them, because fighting the
syntax and practicing a new skill is twice as hard.

Most of these questions **return** a value rather than printing one. Printing
shows a human something; returning hands the value back to your code. A
function that prints where the test expects a return will fail every time,
and the failure message will look confusing. **Two questions do print, and they say so**.

## From Scratch

Write your solutions in `src/from_scratch.py`.

### Question 1: `measure_rain`

Write a function `measure_rain` that takes a single argument, a number
`inches`. It should return a message depending on the number of inches:

- 6 or more inches — `"flood"`
- less than 6 inches — `"rainy"`
- less than 4 inches — `"average"`
- less than 2 inches — `"dry"`
- 0 inches — `"drought"`

Hint: be careful about the order that you write your conditions!

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

### Question 3: `describe_cart`

Write a function `describe_cart` that takes a list `items` and a string
`owner` that defaults to `"Your"`. It should return a sentence describing
the cart.

```python
describe_cart([])
# "Your cart is empty."
describe_cart([], "Ada's")
# "Ada's cart is empty."
describe_cart(["apple"])
# "Your cart has 1 item."
describe_cart(["apple", "pear"])
# "Your cart has 2 items."
describe_cart(["a", "b", "c"], "Ada's")
# "Ada's cart has 3 items."
```

Pay attention to the pluralization of "item". One item is an `item`, and anything else is `items`.

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

Hint: `None` and `""` are both falsy. How can you tell if a value is one or the other?

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

Rewrite `wildly_biased_review` so it uses a single `if` statement but achieves the same result.

Hint: what is a **guard clause**?

### Question 7: `get_weather_report`

The `get_weather_report` function is incomplete. It doesn't handle temperatures
between 32 and 70. Give that range a branch of its own that sets the message
to `"It's a bit chilly."`

However, you will notice that the function is very repetitive: it invokes
`print(weather_report)` and `print("And that's your report!")` in every conditional
branch.

Refactor the function so that those two statements each appear once in the entire
program but still has the same functionality.

Hint: Make each of those lines appear **once**. The branches should decide what the
message _is_, not do the printing.

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

Someone got _real_ clever here and chained conditional expressions together.
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
mood strikes you, try your hand at `measure_rain_match` and `rounder_match` in
`src/bonus_match.py`. The first is the question above again. The second is new:
`rounder_match(num, nearest)` takes a number and one of `"up"`, `"down"` or
`"honest"`, and rounds accordingly. Read its tests for the exact behavior.

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
