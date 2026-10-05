import inspect

from debug import coolness_gauge, funko_pop_addiction_level, return_positive_negative_zero

TEST_SUITE_NAME = "Debug Tests"


def test_coolness_gauge():
    """coolness_gauge - returns the right message based on a number"""
    assert coolness_gauge(0) == "You need more fridges."
    assert coolness_gauge(1) == "You need more fridges."
    assert coolness_gauge(2) == "You need more fridges."
    assert coolness_gauge(3) == "You need more fridges."
    assert coolness_gauge(4) == "You are downright chilly!"
    assert coolness_gauge(5) == "You are downright chilly!"
    assert coolness_gauge(6) == "You are downright chilly!"


def test_funko_pop_addiction_level():
    """funko_pop_addiction_level - returns the right message based on a number"""
    assert funko_pop_addiction_level(0) == "No pops? Maybe try one."
    assert funko_pop_addiction_level(1) == "Only a few? Keep having fun!"
    assert funko_pop_addiction_level(10) == "Only a few? Keep having fun!"
    assert funko_pop_addiction_level(11) == "You have a problem."
    assert funko_pop_addiction_level(20) == "You have a problem."
    assert funko_pop_addiction_level(21) == "You need help!"
    assert funko_pop_addiction_level(30) == "You need help!"
    assert funko_pop_addiction_level(31) == "You need an intervention!!!"
    assert funko_pop_addiction_level(100) == "You need an intervention!!!"


def test_return_positive_negative_zero_nesting():
    """return_positive_negative_zero - does not nest conditional expressions"""
    source = inspect.getsource(return_positive_negative_zero)
    # A nested conditional expression puts two ` if ` on one line, which is
    # where this function became unreadable in the first place.
    for line in source.splitlines():
        assert line.count(" if ") <= 1


def test_return_positive_negative_zero():
    """return_positive_negative_zero - returns the right message based on a number"""
    assert return_positive_negative_zero(0) == "Zero"
    assert return_positive_negative_zero(1) == "Positive"
    assert return_positive_negative_zero(2) == "Positive"
    assert return_positive_negative_zero(-1) == "Negative"
    assert return_positive_negative_zero(-2) == "Negative"
