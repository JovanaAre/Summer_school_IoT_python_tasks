from python.Zadatak1.quad_equation import quad_equation
import pytest


testdata = [(1, 5, 6, (-2+0j, -3+0j)), (1, 4, 8, (-2+2j, -2-2j))]


@pytest.mark.parametrize("a, b , c, expected_output", testdata)
def test_quad_equation(a, b, c, expected_output):
    assert quad_equation(a, b, c) == expected_output