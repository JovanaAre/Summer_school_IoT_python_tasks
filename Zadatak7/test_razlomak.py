import pytest
from python.Zadatak7.razlomci import Razlomak


@pytest.fixture
def default_razlomak():
    """
    Returns a Fraction instance whose denominator is equal to 1
    """
    return Razlomak(2)


@pytest.fixture
def razlomak():
    """
    Returns a Fraction instance whose numerator is equal to 1
    and denominator is equal to 2
    """
    return Razlomak(1, 2)


def test_default_initial_fraction(default_razlomak):
    assert str(default_razlomak) == "(2/1)"


def test_setting_initial_fraction(razlomak):
    assert str(razlomak) == "(1/2)"


def test_add(razlomak):
    assert str(razlomak+razlomak) == "(4/4)"


def test_mul(razlomak):
    assert str(razlomak*razlomak) == "(1/4)"
