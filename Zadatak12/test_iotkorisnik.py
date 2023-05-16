from python.Zadatak12.iotkorisnik import IOTKorisnik
import pytest


@pytest.fixture
def iotkorisnik():
    """
    Returns a IOTKorisnik instance whose email is "pytest.example@gmail.com",
    password is "pyex147" (hashed) and rola is equal to 21
    """
    return IOTKorisnik("pytest.example@gmail.com", "pyex147", 21)


def test_setting_initial_ioturedjaj(iotkorisnik):
    assert iotkorisnik.email == "pytest.example@gmail.com" and iotkorisnik.lozinka == "pyex147" \
        and iotkorisnik.rola == 21
