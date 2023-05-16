import pytest
from python.Zadatak12.iotkorisnik import IOTKorisnik
from python.Zadatak13.upis_korisnika import write_txt
from python.Zadatak13.citanje_korisnika import read_txt
from python.Zadatak16.email_decorator import izmjeni_korisnika
from python.lozinka import verify_password


@pytest.fixture
def iotkorisnik1():
    """
      Returns a IOTKorisnik instance whose email is "pythonexample@gmail.com",
      password is "python123" and rola is equal to 1
      """
    return IOTKorisnik("pythonexample@gmail.com", "pythex121", 1)


@pytest.fixture
def iotkorisnik2():
    """
      Returns a IOTKorisnik instance whose email is "pythoncourse@gmail.com",
      password is "python0232" and rola is equal to 23
      """
    return IOTKorisnik("pythoncourse@gmail.com", "python0232", 23)


def test_izmjeni_korisnika(iotkorisnik1, iotkorisnik2):
    write_txt(iotkorisnik1, 'w')
    write_txt(iotkorisnik2, 'a')
    izmjeni_korisnika("pythoncourse@gmail.com", "python0232", 12)
    iotkorisnik_modified = IOTKorisnik("pythoncourse@gmail.com", "python0232", 12)
    content = read_txt()
    tmp = content.splitlines()
    iotkorisnik1_read = tmp[0].split(',')
    iotkorisnik2_read = tmp[1].split(',')
    is_password_valid1 = verify_password(iotkorisnik1.lozinka, iotkorisnik1_read[1])
    is_password_valid2 = verify_password(iotkorisnik_modified.lozinka, iotkorisnik2_read[1])
    assert iotkorisnik1_read[0] == iotkorisnik1.email and iotkorisnik1_read[2] == str(iotkorisnik1.rola) \
           and is_password_valid1 and iotkorisnik2_read[0] == iotkorisnik_modified.email \
           and iotkorisnik2_read[2] == str(iotkorisnik_modified.rola) and is_password_valid2
