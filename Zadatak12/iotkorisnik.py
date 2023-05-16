# 12. Napisati klasu koja opisuje Korisnika IoT sistema.
# Korisnik sadrzi: email (jedinstveni podatak), lozinku, rolu (rola je broj).


from python.lozinka import hash_the_password


class IOTKorisnik(object):
    """
    A class to represent a IOT user.

    Attributes
    ----------
    :param email: unique email of the user
    :type email: str
    :param lozinka: user password
    :type lozinka: str
    :param rola: user role
    :type rola: int

    Methods
    -------
     __init__(email: str, lozinka: str, rola: int):
    Constructs all the necessary attributes for the IOKorisnik object
    :param email: unique email of the user
    :param lozinka: user password
    :param rola: user role
    """
    email = ""
    lozinka = ""
    rola = 0

    def __init__(self, email: str, lozinka: str, rola: int):
        self.email = email
        self.lozinka = lozinka
        self.rola = rola

    def __repr__(self):
        return {'Email': self.email, 'Lozinka': self.lozinka, 'Rola': self.rola}

    def __str__(self):
        # return 'Email = ' + self.email + ', lozinka = ' + self.lozinka + ', rola = ' + str(self.rola)
        return self.email + ',' + hash_the_password(self.lozinka) + ',' + str(self.rola)


# print(IOTKorisnik.__doc__)
