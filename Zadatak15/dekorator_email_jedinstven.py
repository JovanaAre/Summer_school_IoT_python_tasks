# 15. Iskoristiti ili napraviti dekorator koji provjerava da li je email
# jedinstven.


from python.Zadatak12.iotkorisnik import IOTKorisnik
import os


# Dekorator 1
def email_exists(func):
	"""
	Reads all users from a text file korisnici_fajl.txt
	and checks if the email passed as the first argument exists in the file.
	If it does not exist, it throws the appropriate exception.
	If there is, it calls the function func
	passed as a parameter.

	:param func: the function that will be called
	"""
	with open(os.environ["FILE_PATH_2"], 'r') as f:
		lines = f.readlines()
	all_emails = []
	for line in lines:
		tmp_line = line.split(',')
		all_emails.append(tmp_line[0])

	def inner(*args, **kwargs):
		email = args[0]
		if email in all_emails:
			return func(*args, **kwargs)
		else:
			raise BaseException("Ne postoji email: %s" % email)
	return inner


# Dekorator 2
def no_email(func):
	"""
	Reads all users from a text file korisnici_fajl.txt
	and checks if the email passed as the first argument exists in the file.
	If it does not exist, it calls the function func passed as a parameter.
	If there is, it throws the appropriate exception.

	:param func: the function that will be called
	"""
	with open(os.environ["FILE_PATH_2"], 'r') as f:
		lines = f.readlines()
	all_emails = []
	for line in lines:
		tmp_line = line.split(',')
		all_emails.append(tmp_line[0])

	def inner(*args, **kwargs):
		email = args[0]
		if email in all_emails:
			raise BaseException("Email %s postoji" % email)
		else:
			return func(*args, **kwargs)

	return inner


@email_exists
def izmjeni_korisnika(user_email: str, user_password: str, rola: int) -> None:
	"""
	Modifies the user with email user_email,
	password user_password and role rola
	(changes his role - rola)
	and writes it again to the appropriate place
	in the text file with all users (korisnici_fajl.txt)

	:param user_email: email of the user being modified
	:param user_password: user password
	:param rola: user role
	:return: None
	"""
	print("Izmjena korisnika...")
	iotkorisnik = IOTKorisnik(user_email, user_password, rola)
	count = 0
	with open(os.environ["FILE_PATH_2"], 'r') as f:
		lines = f.readlines()
		for line in lines:
			if user_email not in line:
				count += 1
			else:
				lines[count] = str(iotkorisnik) + "\n"
				with open(os.environ["FILE_PATH_2"], 'w') as f:
					f.writelines(lines)


@no_email
def upisi_korisnika(user_email: str, user_password: str, rola: int) -> None:
	"""
	Adds the user with email user_email,
	password user_password and role rola
	to the end of the text file with
	all users (korisnici_fajl.txt)


	:param user_email: email of the user being added
	:param user_password: user password
	:param rola: user role
	:return: None
	"""
	print("Korisnik se upisuje u fajl...")
	iotkorisnik = IOTKorisnik(user_email, user_password, rola)
	with open(os.environ["FILE_PATH_2"], 'a') as f:
		f.write(str(iotkorisnik) + "\n")


# print(email_exists.__doc__)
# print(no_email.__doc__)
# print(izmjeni_korisnika.__doc__)
# print(upisi_korisnika.__doc__)
