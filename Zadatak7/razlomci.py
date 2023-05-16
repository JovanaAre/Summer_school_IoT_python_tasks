# 7. Napisati klasu koja implementira razlomke.
# Razlomci imaju brojioc i imenioc.
# Preklopiti metode __str__ , __mul__ i __add__
# kako bi omogućili ispisivanje u obliku razlomaka, množenje i sabiranje
# razlomaka respektivno.


class Razlomak(object):
	"""
	A class to represent a fraction, used for implementation
	of the fraction add and multiplication operations

	Attributes
	----------
	:param brojilac: the numerator of the fraction
	:type brojilac: int
	:param imenilac: the denominator of the fraction
	:type imenilac: int

	Methods
	-------
	__init__(brojilac : int, imenilac : int = 1):
	Constructs all the necessary attributes for the fraction object.
	:param brojilac: the numerator of the fraction
	:param imenilac: the denominator of the fraction
	"""
	def __init__(self, brojilac: int, imenilac: int = 1):
		self.brojilac = brojilac
		self.imenilac = imenilac

	def __repr__(self):
		return "Razlomak(%s,%s)" % (self.brojilac, self.imenilac)

	def __str__(self):
		return "(%d/%d)" % (self.brojilac, self.imenilac)

		# self + other
	def __add__(self, other):
		novi_brojilac = self.brojilac * other.imenilac + self.imenilac * other.brojilac
		novi_imenilac = self.imenilac * other.imenilac
		return Razlomak(novi_brojilac, novi_imenilac)

		# self * other
	def __mul__(self, other):
		novi_brojilac = self.brojilac * other.brojilac
		novi_imenilac = self.imenilac * other.imenilac
		return Razlomak(novi_brojilac, novi_imenilac)


# print(Razlomak.__doc__)
