import pytest
import os
from python.Zadatak8.ioturedjaj import IOTUredjaj
from python.Zadatak9i10.upis import write_txt


@pytest.fixture
def ioturedjaj():
    """
    Returns a IOTUredjaj instance whose serijski_broj is equal to 254139
    and id_na_cloudu is "jkanw"
    """
    return IOTUredjaj(254139, "jkanw")


def test_write_txt(ioturedjaj):
    write_txt(str(ioturedjaj), 'w')
    with open(os.environ["FILE_PATH_1"], 'r') as f:
        content = f.read()
    ioturedjaj_write = content.rstrip()
    assert str(ioturedjaj) == ioturedjaj_write
