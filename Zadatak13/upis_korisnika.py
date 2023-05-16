import os
from python.Zadatak12.iotkorisnik import IOTKorisnik


# Dodavanje Korisnika u tekstualni fajl
def write_txt(iotkorisnik: IOTKorisnik, mode_upisa: str):
    """
    Writes the IOT user to a text file
    with all users (korisnici_fajl.txt)

    :param iotkorisnik: IOTKorisnik object
    :param mode_upisa: write mode ('a' - append, 'w' - write)
    :return: None
    """
    with open(os.environ["FILE_PATH_2"], mode_upisa) as f:
        f.write(str(iotkorisnik) + "\n")


# print(write_txt.__doc__)
