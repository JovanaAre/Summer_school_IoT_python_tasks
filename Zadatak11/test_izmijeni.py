import pytest
from python.Zadatak8.ioturedjaj import IOTUredjaj
from python.Zadatak9i10.upis import write_txt
from python.Zadatak9i10.citanje import read_txt
from python.Zadatak11.dekorator_uredjaj_jedinstven import izmjeni_uredjaj


@pytest.fixture
def ioturedjaj1():
    """
    Returns a IOTUredjaj instance whose serijski_broj is equal to 123456
    and id_na_cloudu is "jkanw"
    """
    return IOTUredjaj(123456, "jkanw")


@pytest.fixture
def ioturedjaj2():
    """
    Returns a IOTUredjaj instance whose serijski_broj is equal to 254139
    and id_na_cloudu is "wqrzx"
    """
    return IOTUredjaj(254139, "wqrzx")


def test_izmjeni_uredjaj(ioturedjaj1, ioturedjaj2):
    write_txt(ioturedjaj1, 'w')
    write_txt(ioturedjaj2, 'a')
    izmjeni_uredjaj("123456", "rtrk1")
    ioturedjaj_modified = IOTUredjaj(123456, "rtrk1")
    content = read_txt()
    ioturedjaji_read = content.splitlines()
    assert str(ioturedjaji_read[0]) == str(ioturedjaj_modified) and str(ioturedjaji_read[1]) == str(ioturedjaj2)
