from python.Zadatak8.ioturedjaj import IOTUredjaj
import pytest


@pytest.fixture
def ioturedjaj():
    """
    Returns a IOTUredjaj instance whose serijski_broj is equal to 593401
    and id_na_cloudu is "awqry"
    """
    return IOTUredjaj(593401, "awqry")


def test_setting_initial_ioturedjaj(ioturedjaj):
    assert ioturedjaj.serijski_broj == 593401 and ioturedjaj.id_na_cloudu == "awqry"


def test_str_ioturedjaj(ioturedjaj):
    assert str(ioturedjaj) == "593401,awqry"
