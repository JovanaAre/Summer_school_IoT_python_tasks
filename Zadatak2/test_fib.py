from python.Zadatak2.fib import fib_n
import pytest


testdata = [(5, [0, 1, 1, 2, 3]), (0, [])]


@pytest.mark.parametrize("n, expected_output", testdata)
def test_fib_n(n, expected_output):
    assert list(fib_n(n)) == expected_output
