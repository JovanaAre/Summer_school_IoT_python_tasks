from python.Zadatak12.iotkorisnik import IOTKorisnik
from python.Zadatak13.upis_korisnika import write_txt
from python.Zadatak13.citanje_korisnika import read_txt


iotkorisnik1 = IOTKorisnik("python@gmail.com", "sdf43", 1)
iotkorisnik2 = IOTKorisnik("course@gmail.com", "sdf43241", 11)
iotkorisnik3 = IOTKorisnik("at@gmail.com", "asf21.", 3)
iotkorisnik4 = IOTKorisnik("rtrk@gmail.com", "123kl_", 7)

iotkorisnici = []
iotkorisnici.append(iotkorisnik1)
iotkorisnici.append(iotkorisnik2)
iotkorisnici.append(iotkorisnik3)
iotkorisnici.append(iotkorisnik4)

# Upis u fajl
for iot in iotkorisnici:
    if iot == iotkorisnici[0]:
        write_txt(iot, 'w')
    else:
        write_txt(iot, 'a')


# Citanje iz fajla
iotkorisnici_procitano = read_txt()
print(str(iotkorisnici_procitano))
