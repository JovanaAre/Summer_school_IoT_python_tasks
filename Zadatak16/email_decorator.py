# 16. Napraviti dekorator koji provjerava da li je email ispravan i
# koristiti ga prilikom izmjene i unosa novog korisnika.


import re
from python.Zadatak12.iotkorisnik import IOTKorisnik
import os


def validate_email(func):
    """
    Checks whether the email passed as the first argument is valid.
    If it is correct, it calls the function func passed as a parameter.
    If not, it throws the appropriate exception.

    :param func: the function that will be called
    """
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    def inner(*args, **kwargs):
        email_str = args[0]
        if re.search(regex, email_str):
            return func(*args, **kwargs)
        else:
            raise BaseException("Email %s is invalid" % email_str)

    return inner


@validate_email
def upisi_korisnika(email: str, lozinka: str, rola: int) -> None:
    """
    Adds the user with email email,
    password lozinka and role rola
    to the end of the text file with
    all users (korisnici_fajl.txt)


    :param email: email of the user being added
    :param lozinka: user password
    :param rola: user role
    :return: None
    """
    print("Korisnik se upisuje u fajl...")
    iotkorisnik = IOTKorisnik(email, lozinka, rola)
    with open(os.environ["FILE_PATH_2"], 'a') as f:
        f.write(str(iotkorisnik) + "\n")


@validate_email
def izmjeni_korisnika(email: str, lozinka: str, rola: int) -> None:
    """
    Modifies the user with email email,
    password lozinka and role rola
    (changes his role - rola)
    and writes it again to the appropriate place
    in the text file with all users (korisnici_fajl.txt)

    :param email: email of the user being modified
    :param lozinka: user password
    :param rola: user role
    :return: None
    """
    print("Izmjena korisnika...")
    iotkorisnik = IOTKorisnik(email, lozinka, rola)
    count = 0
    with open(os.environ["FILE_PATH_2"], 'r') as f:
        lines = f.readlines()
        for line in lines:
            if email not in line:
                count += 1
            else:
                lines[count] = str(iotkorisnik) + "\n"
                with open(os.environ["FILE_PATH_2"], 'w') as f:
                    f.writelines(lines)


# print(validate_email.__doc__)
# print(izmjeni_korisnika.__doc__)
# print(upisi_korisnika.__doc__)
