# 3. Napisati funkciju koja testira da li je string palindrom.
# Poseban modul.


def palindrome(string: str) -> bool:
    """
    Checks whether a string is a palindrome

    :param string: The string to be checked
    :return: True if the string is a palindrome, otherwise is False
    """
    return string == string[::-1]


# print(palindrome.__doc__)
