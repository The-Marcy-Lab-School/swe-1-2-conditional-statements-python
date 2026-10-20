import inspect

from modify import get_weather_report, send_message

TEST_SUITE_NAME = "Modify Tests"


def printed_lines(capsys):
    return [line for line in capsys.readouterr().out.splitlines() if line.strip()]


def test_send_message_uses_guard_clauses():
    """send_message - uses guard clauses"""
    source = inspect.getsource(send_message)
    assert "return" in source
    assert "if" in source
    # A guard clause returns early, so there is no longer an else to fall into
    assert "else" not in source
    assert "elif" not in source

    # Guard clauses keep the function flat: the def line, the if lines one
    # level in, and the returns inside them two levels in. Nothing deeper.
    indents = [len(line) - len(line.lstrip()) for line in source.splitlines() if line.strip()]
    assert max(indents) <= 8


def test_send_message_output():
    """send_message - returns the right message for each check"""
    assert send_message("ada", "grace", "hi!") == "ada -> grace: hi!"
    assert send_message("", "grace", "hi!") == "You must be logged in."
    assert send_message(None, "grace", "hi!") == "You must be logged in."
    assert send_message("ada", "", "hi!") == "Choose someone to message."
    assert send_message("ada", "grace", "") == "Message cannot be empty."

    # 280 characters is the limit, so 280 is sent and 281 is too long
    assert send_message("ada", "grace", "a" * 280) == f"ada -> grace: {'a' * 280}"
    assert send_message("ada", "grace", "a" * 281) == "Message is too long."


def test_send_message_check_order():
    """send_message - checks happen in the original order"""
    assert send_message("", "", "") == "You must be logged in."
    assert send_message("ada", "", "") == "Choose someone to message."
    assert send_message("ada", "", "a" * 281) == "Choose someone to message."
    assert send_message("ada", "grace", "") == "Message cannot be empty."


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

    get_weather_report(50)
    assert printed_lines(capsys) == ["It's a bit chilly.", sign_off]
