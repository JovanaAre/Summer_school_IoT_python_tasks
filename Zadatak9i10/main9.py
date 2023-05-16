from python.Zadatak8.ioturedjaj import IOTUredjaj
from python.Zadatak9i10.upis import write_txt
from python.Zadatak9i10.citanje import read_txt

ioturedjaj1 = IOTUredjaj(123456, "sdf43")
ioturedjaj2 = IOTUredjaj(222222, "jak96")
ioturedjaj3 = IOTUredjaj(111111, "ahk32")
ioturedjaj4 = IOTUredjaj(252525, "def11")

ioturedjaji = []
ioturedjaji.append(ioturedjaj1)
ioturedjaji.append(ioturedjaj2)
ioturedjaji.append(ioturedjaj3)
ioturedjaji.append(ioturedjaj4)

# Upis u fajl
for iot in ioturedjaji:
    if iot == ioturedjaji[0]:
        write_txt(iot, 'w')
    else:
        write_txt(iot, 'a')


# Citanje iz fajla
ioturedjaji_procitano = read_txt()
print(str(ioturedjaji_procitano))
