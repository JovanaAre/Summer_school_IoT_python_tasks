from python.Zadatak8.ioturedjaj import IOTUredjaj
from python.Zadatak9i10.citanje import read_txt
from python.Zadatak9i10.upis import write_txt


def test_read_txt():
    ioturedjaj1 = IOTUredjaj(989852, "sdf43")
    ioturedjaj2 = IOTUredjaj(781325, "jaklx")
    write_txt(ioturedjaj1, 'w')
    write_txt(ioturedjaj2, 'a')
    content = read_txt()
    ioturedjaji_read = content.splitlines()
    assert str(ioturedjaji_read[0]) == str(ioturedjaj1) and str(ioturedjaji_read[1]) == str(ioturedjaj2)
