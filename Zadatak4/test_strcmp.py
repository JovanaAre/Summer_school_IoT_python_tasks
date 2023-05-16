from python.Zadatak4.strcmp import strcmp
import pytest


testdata = [("rtrk", "rtrk", 0), ("rtrk1", "rtrk", -1), ("rtrk", "rtrk1", 1)]


@pytest.mark.parametrize("string1, string2, expected_output", testdata)
def test_strcmp(string1, string2, expected_output):
    assert strcmp(string1, string2) == expected_output
