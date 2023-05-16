import pytest
from python.Zadatak12.iotkorisnik import IOTKorisnik
from python.Zadatak13.upis_korisnika import write_txt
from python.Zadatak13.citanje_korisnika import read_txt
from python.Zadatak16.email_decorator import upisi_korisnika
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


def test_upisi_korisnika(iotkorisnik1, iotkorisnik2):
    write_txt(iotkorisnik1, 'w')
    write_txt(iotkorisnik2, 'a')
    upisi_korisnika("rtrkcourse@gmail.com", "23rtrk12", 19)
    iotkorisnik_added = IOTKorisnik("rtrkcourse@gmail.com", "23rtrk12", 19)
    content = read_txt()
    tmp = content.splitlines()
    iotkorisnik1_read = tmp[0].split(',')
    iotkorisnik2_read = tmp[1].split(',')
    iotkorisnik3_read = tmp[2].split(',')
    is_password_valid1 = verify_password(iotkorisnik1.lozinka, iotkorisnik1_read[1])
    is_password_valid2 = verify_password(iotkorisnik2.lozinka, iotkorisnik2_read[1])
    is_password_valid3 = verify_password(iotkorisnik_added.lozinka, iotkorisnik3_read[1])
    assert iotkorisnik1_read[0] == iotkorisnik1.email and iotkorisnik1_read[2] == str(iotkorisnik1.rola) \
        and is_password_valid1 and iotkorisnik2_read[0] == iotkorisnik2.email \
        and iotkorisnik2_read[2] == str(iotkorisnik2.rola) and is_password_valid2 \
        and iotkorisnik3_read[0] == iotkorisnik_added.email \
        and iotkorisnik3_read[2] == str(iotkorisnik_added.rola) and is_password_valid3
