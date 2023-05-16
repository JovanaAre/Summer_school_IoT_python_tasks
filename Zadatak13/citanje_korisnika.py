# 13. Napisati funkcije koja upisuju i čitaju iz fajla korisnike,
# isto odvojeno zarezima, a lozinka mora biti enkodirana.
# Primjer u fajlu lozinka.py


import os


def read_txt() -> str:
    """
    Reads all IOT users from the text file with users (korisnici_fajl.txt)
    and returns the read string

    :param: None
    :return: read string containing all read users
    """
    with open(os.environ["FILE_PATH_2"], 'r') as f:
        iotkorisnici = f.read()
    return iotkorisnici


# print(read_txt.__doc__)
