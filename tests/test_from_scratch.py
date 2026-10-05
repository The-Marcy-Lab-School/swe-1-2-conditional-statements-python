from from_scratch import (
    describe_cart,
    greet_by_nickname,
    happy_birthday_pet,
    label_temperature,
    measure_rain,
)


def test_measure_rain():
    """measure_rain - returns a message for each rainfall band"""
    assert measure_rain(0) == "drought"
    assert measure_rain(1) == "dry"
    assert measure_rain(1.9) == "dry"
    assert measure_rain(2) == "average"
    assert measure_rain(3.5) == "average"
    assert measure_rain(4) == "rainy"
    assert measure_rain(5.9) == "rainy"
    assert measure_rain(6) == "flood"
    assert measure_rain(100) == "flood"


def test_happy_birthday_pet():
    """happy_birthday_pet - returns a message for the breed and age"""
    assert happy_birthday_pet("snake", 1) == "Hiss hiss!"
    assert happy_birthday_pet("snake", 40) == "Hiss hiss!"
    assert happy_birthday_pet("cat", 4) == "Mew mew!"
    assert happy_birthday_pet("cat", 5) == "Meow meow!"
    assert happy_birthday_pet("dog", 4) == "Arf arf!"
    assert happy_birthday_pet("dog", 5) == "Woof woof!"
    assert happy_birthday_pet("dog", 9) == "Woof woof!"
    assert happy_birthday_pet("dog", 10) == "Boof!"
    assert happy_birthday_pet("ferret", 2) == "Happy birthday!"


def test_describe_cart_empty():
    """describe_cart - reports an empty cart"""
    assert describe_cart([]) == "Your cart is empty."
    assert describe_cart([], "Ada's") == "Ada's cart is empty."


def test_describe_cart_with_items():
    """describe_cart - counts the items it was given"""
    assert describe_cart(["apple"]) == "Your cart has 1 item."
    assert describe_cart(["apple", "pear"]) == "Your cart has 2 items."
    assert describe_cart(["a", "b", "c"], "Ada's") == "Ada's cart has 3 items."


def test_greet_by_nickname_no_nickname():
    """greet_by_nickname - falls back to the name when no nickname is given"""
    assert greet_by_nickname("Ada") == "Hello, Ada!"


def test_greet_by_nickname_empty_nickname():
    """greet_by_nickname - an empty nickname is a choice, not a missing value"""
    assert greet_by_nickname("Ada", "") == "Hello!"
    assert greet_by_nickname("Ada", "Ace") == "Hello, Ace!"


def test_label_temperature():
    """label_temperature - returns one of two labels"""
    assert label_temperature(21) == "warm"
    assert label_temperature(20) == "warm"
    assert label_temperature(19) == "cold"
    assert label_temperature(-5) == "cold"


def test_label_temperature_is_one_expression():
    """label_temperature - is written as a conditional expression"""
    import inspect

    body = [
        line.strip()
        for line in inspect.getsource(label_temperature).splitlines()[1:]
        if line.strip() and not line.strip().startswith("#")
    ]
    assert len(body) == 1, "Write this as a single return statement."
    assert body[0].startswith("return"), "The one line should be a return."
    assert " if " in body[0] and " else " in body[0]
