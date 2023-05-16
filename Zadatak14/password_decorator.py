# 14. Napisati dekorator koji provjerava da li je lozinka ispravna.
# Primjer u fajlu lozinka.py


from python.lozinka import verify_password
from python.Zadatak12.iotkorisnik import IOTKorisnik
import os


# Dekorator
def validate_password(func):
	"""
	Reads all users from a text file korisnici_fajl.txt
	and checks if the email passed as the first argument exists in the file.
	If it does not exist, it throws the appropriate exception.
	If there is, it checks if the password passed as the second argument
	matches the password read in the text file for that user.
	If the passwords match, it calls the function func
	passed as a parameter. And if they don't match,
	it throws the appropriate exception.

	:param func: the function that will be called
	"""
	with open(os.environ["FILE_PATH_2"], 'r') as f:
		lines = f.readlines()
	all_emails = []
	all_passwords = []
	for line in lines:
		tmp_line = line.split(',')
		all_emails.append(tmp_line[0])
		all_passwords.append(tmp_line[1])

	def inner(*args, **kwargs):
		email = args[0]
		password = args[1]
		if email not in all_emails:
			raise BaseException("Pogresan email %s" % email)
		else:
			index = all_emails.index(email)
			if verify_password(password, all_passwords[index]):
				return func(*args, **kwargs)
			else:
				raise BaseException("Lozinke se ne podudaraju")
	return inner


@validate_password
def izmjeni_lozinku(email: str, password: str, rola: int) -> None:
	"""
	Modifies the password of the user with email email.
	Allows entering a new password from the standard input
	and writes the user with the changed password again
	to the appropriate place
	in the text file with all users (korisnici_fajl.txt)

	:param email: email of the user being modified
	:param password: user password
	:param rola: user role
	:return: None
	"""
	print("Korisnik mijenja lozinku...")
	new_password = input('Unesite novu lozinku: ')
	iotkorisnik = IOTKorisnik(email, new_password, rola)
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


# print(validate_password.__doc__)
# print(izmjeni_lozinku.__doc__)
