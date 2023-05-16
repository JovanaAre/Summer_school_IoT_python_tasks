# 11. Napisati dekorator funkciju koja provjerava da li je uredjaj
# jedinstven, da li postoji. Primjer dekoratora koji prihvata parameter je dat
# u materijalima primjer_dekoratora_sa_parametrima.py


from python.Zadatak8.ioturedjaj import IOTUredjaj
import os


# Dekorator 1
def sn_exists(func):
	"""
	Reads all devices from a text file uredjaji_fajl.txt
	and checks if the serial number passed as the first argument exists in the file.
	If it does not exist, it throws the appropriate exception.
	If there is, it calls the function func
	passed as a parameter.

	:param func: the function that will be called
	"""
	with open(os.environ["FILE_PATH_1"], 'r') as f:
		lines = f.readlines()
	all_sns = []
	for line in lines:
		tmp = line[:6]
		all_sns.append(tmp)

	def inner(*args, **kwargs):
		sn = args[0]
		if sn in all_sns:
			return func(*args, **kwargs)
		else:
			raise BaseException("Ne postoji %s" % sn)
	return inner


# Dekorator 2
def no_sn(func):
	"""
	Reads all devices from a text file uredjaji_fajl.txt
	and checks if the serial number passed as the first argument exists in the file.
	If it does not exist, it calls the function func passed as a parameter.
	If there is, it throws the appropriate exception.

	:param func: the function that will be called
	"""
	with open(os.environ["FILE_PATH_1"], 'r') as f:
		lines = f.readlines()
	all_sns = []
	len(lines)
	for line in lines:
		tmp = line[:6]
		all_sns.append(tmp)

	def inner(*args, **kwargs):
		sn = args[0]
		if sn in all_sns:
			raise BaseException("Serijski broj %s postoji" % sn)
		else:
			return func(*args, **kwargs)

	return inner


@no_sn
def upisi_uredjaj(sn: str, device_id: str) -> None:
	"""
	Adds the device with serial number sn and identifier on the cloud device_id
	to the end of the text file with all devices (uredjaji_fajl.txt)


	:param sn: the serial number of the device being added
	:param device_id: device identifier on the cloud (id_na_cloudu)
	:return: None
	"""
	print("Uredjaj sa odgovarajucim serijskim brojem se upisuje u fajl...")
	ioturedjaj = IOTUredjaj(int(sn), device_id)
	with open(os.environ["FILE_PATH_1"], 'a') as f:
		f.write(str(ioturedjaj) + "\n")


@sn_exists
def izmjeni_uredjaj(sn: str, device_id: str) -> None:
	"""
	Modifies the device with the serial number sn
	(changes its identifier on the cloud - id_na_cloudu)
	and writes it again to the appropriate place
	in the text file with all devices (uredjaji_fajl.txt)

	:param sn: the serial number of the device being modified
	:param device_id: new device identifier on the cloud (id_na_cloudu)
	:return: None
	"""
	print("Uredjaj sa odgovarajucim serijskim brojem se mijenja...")
	ioturedjaj = IOTUredjaj(int(sn), device_id)
	count = 0
	with open(os.environ["FILE_PATH_1"], 'r') as f:
		lines = f.readlines()
		for line in lines:
			if sn not in line:
				count += 1
			else:
				lines[count] = str(ioturedjaj) + "\n"
				with open(os.environ["FILE_PATH_1"], 'w') as f:
					f.writelines(lines)


# print(sn_exists.__doc__)
# print(no_sn.__doc__)
# print(izmjeni_uredjaj.__doc__)
# print(upisi_uredjaj.__doc__)
