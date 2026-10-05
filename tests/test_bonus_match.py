import pytest
from bonus_match import measure_rain_match, rounder_match

TEST_SUITE_NAME = "Bonus Tests"

# Bonus questions do not count towards your score. Do them anyway.
SCORED = False


@pytest.mark.skip(reason="Remove this line when you are ready to test")
def test_measure_rain_match():
    """measure_rain_match - returns the right message based on rain amount"""
    assert measure_rain_match(0) == "drought"
    assert measure_rain_match(1) == "dry"
    assert measure_rain_match(2) == "average"
    assert measure_rain_match(3) == "average"
    assert measure_rain_match(4) == "rainy"
    assert measure_rain_match(5) == "rainy"
    assert measure_rain_match(6) == "flood"
    assert measure_rain_match(7) == "flood"
    assert measure_rain_match(10) == "flood"


@pytest.mark.skip(reason="Remove this line when you are ready to test")
def test_rounder_match():
    """rounder_match - returns the right number based on rounding setting"""
    assert rounder_match(1.0, "up") == 1
    assert rounder_match(1.1, "up") == 2
    assert rounder_match(3.9, "up") == 4
    assert rounder_match(1.9, "down") == 1
    assert rounder_match(5.0, "down") == 5
    assert rounder_match(5.1, "down") == 5
    assert rounder_match(1.9, "honest") == 2
    assert rounder_match(1.5, "honest") == 2
    assert rounder_match(1.4, "honest") == 1
    assert rounder_match(1.0, "honest") == 1
