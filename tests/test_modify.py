import inspect
import random

from modify import get_weather_report, wildly_biased_review

TEST_SUITE_NAME = "Modify Tests"


def printed_lines(capsys):
    return [line for line in capsys.readouterr().out.splitlines() if line.strip()]


def test_wildly_biased_review_uses_a_guard_clause():
    """wildly_biased_review - uses a guard clause"""
    source = inspect.getsource(wildly_biased_review)
    assert "return" in source
    assert "if" in source
    # A guard clause returns early, so there is no longer an else to fall into
    assert "else" not in source


def test_wildly_biased_review_output(capsys):
    """wildly_biased_review - prints the right message based on location"""
    wildly_biased_review("NYC")
    assert printed_lines(capsys) == [
        "THE GREATEST CITY IN THE WORLD",
        "THE CITY THAT NEVER SLEEPS",
        "WOW WHAT A CITY",
    ]

    wildly_biased_review("LA")
    assert printed_lines(capsys) == ["Yea that place is cool I guess"]

    wildly_biased_review(f"place_{random.random()}")
    assert printed_lines(capsys) == ["Yea that place is cool I guess"]


def test_get_weather_report(capsys):
    """get_weather_report - minimizes repetition"""
    source = inspect.getsource(get_weather_report)

    # The message should be built once and printed once, not printed in
    # every branch.
    assert source.count("print(weather_report)") == 1
    assert source.count('print("And that\'s your report!")') == 1

    cold = "Wow, it's cold out."
    nice = "It's really nice!"
    hot_gross = "It's hot and gross out."
    sign_off = "And that's your report!"

    get_weather_report(100)
    assert printed_lines(capsys) == [hot_gross, sign_off]

    get_weather_report(80)
    assert printed_lines(capsys) == [nice, sign_off]

    get_weather_report(20)
    assert printed_lines(capsys) == [cold, sign_off]
