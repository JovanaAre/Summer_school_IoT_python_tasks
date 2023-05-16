import pytest
from python.Zadatak8.ioturedjaj import IOTUredjaj
from python.Zadatak9i10.upis import write_txt
from python.Zadatak9i10.citanje import read_txt
from python.Zadatak11.dekorator_uredjaj_jedinstven import upisi_uredjaj


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


def test_upisi_uredjaj(ioturedjaj1, ioturedjaj2):
    write_txt(ioturedjaj1, 'w')
    write_txt(ioturedjaj2, 'a')
    upisi_uredjaj("777231", "rtrk2")
    ioturedjaj_added = IOTUredjaj(777231, "rtrk2")
    content = read_txt()
    ioturedjaji_read = content.splitlines()
    assert str(ioturedjaji_read[0]) == str(ioturedjaj1) and str(ioturedjaji_read[1]) == str(ioturedjaj2) \
        and str(ioturedjaji_read[2]) == str(ioturedjaj_added)
