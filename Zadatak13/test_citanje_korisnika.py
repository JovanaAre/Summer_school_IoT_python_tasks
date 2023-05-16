from python.Zadatak12.iotkorisnik import IOTKorisnik
from python.Zadatak13.citanje_korisnika import read_txt
from python.Zadatak13.upis_korisnika import write_txt
from python.lozinka import verify_password


def test_read_txt():
    iotkorisnik1 = IOTKorisnik("pytest@gmail.com", "sdf43", 1)
    iotkorisnik2 = IOTKorisnik("example@gmail.com", "acx43241", 11)
    write_txt(iotkorisnik1, 'w')
    write_txt(iotkorisnik2, 'a')
    content = read_txt()
    tmp = content.splitlines()
    iotkorisnik1_read = tmp[0].split(',')
    iotkorisnik2_read = tmp[1].split(',')
    is_password_valid1 = verify_password(iotkorisnik1.lozinka, iotkorisnik1_read[1])
    is_password_valid2 = verify_password(iotkorisnik2.lozinka, iotkorisnik2_read[1])
    assert iotkorisnik1_read[0] == iotkorisnik1.email and iotkorisnik1_read[2] == str(iotkorisnik1.rola)\
        and is_password_valid1 and iotkorisnik2_read[0] == iotkorisnik2.email\
        and iotkorisnik2_read[2] == str(iotkorisnik2.rola) and is_password_valid2
