# 4. Napisati funkciju koja vrši poredjenje dva stringa poput strcmp().
# Funkcija vraca 0 ako su stringovi jednaki,
# -1 ako je prvi string veci od drugog i
# 1 ako je drugi string veći od prvog.


def strcmp(string1: str, string2: str) -> int:
    """
    Compares two strings

    :param string1: First string
    :param string2: Another string
    :return: 0: strings are equal, 1: first string is smaller, -1: second string is smaller
    """
    if string1 == string2:
        return 0
    elif string1 < string2:
        return 1
    else:
        return -1


# print(strcmp.__doc__)
