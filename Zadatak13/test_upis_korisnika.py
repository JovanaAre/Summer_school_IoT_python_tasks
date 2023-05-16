import pytest
import os
from python.Zadatak12.iotkorisnik import IOTKorisnik
from python.Zadatak13.upis_korisnika import write_txt
from python.lozinka import verify_password


@pytest.fixture
def iotkorisnik():
    """
    Returns a IOTKorisnik instance whose email is "pythoncourse@gmail.com",
    password is "python123" and rola is equal to 1
    """
    return IOTKorisnik("pythoncourse@gmail.com", "python123", 1)


def test_write_txt(iotkorisnik):
    write_txt(iotkorisnik, 'w')
    with open(os.environ["FILE_PATH_2"], 'r') as f:
        content = f.read()
    tmp1 = content.rstrip()
    tmp = tmp1.split(',')
    is_password_valid = verify_password(iotkorisnik.lozinka, tmp[1])
    assert tmp[0] == iotkorisnik.email and tmp[2] == str(iotkorisnik.rola) and is_password_valid
