from python.Zadatak3.palindrome import palindrome
import pytest


testdata = [("ana", True), ("rtrk", False)]


@pytest.mark.parametrize("string, expected_output", testdata)
def test_palindrome(string, expected_output):
    assert palindrome(string) == expected_output
