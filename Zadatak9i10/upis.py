# 9. Napisati funkciju koja upisuje Uredjaj u tekstualni fajl.
# Lokacija fajla je data u environment varijablama.

import os


from python.Zadatak8.ioturedjaj import IOTUredjaj


# Dodavanje Uredjaja u tekstualni fajl
def write_txt(ioturedjaj: IOTUredjaj, mode_upisa: str):
    """
    Writes the IOT device to a text file
    with all devices (uredjaji_fajl.txt)

    :param ioturedjaj: IOTUredjaj object
    :param mode_upisa: write mode ('a' - append, 'w' - write)
    :return: None
    """
    with open(os.environ["FILE_PATH_1"], mode_upisa) as f:
        f.write(str(ioturedjaj) + "\n")


# print(write_txt.__doc__)
