# 5. Napisati funkciju koja iscrtava kvadrat sa stranicom od n karaktera.
# Ako nije zadat drugi parametar, za iscrtavanje koristiti #,
# u suprotnom iscrtati zadatim karakterom.


def square(size: int, symbol: str = '#') -> None:
    """
    Prints hollow square symbol pattern

    :param size: The size of the side of the square
    :param symbol: Symbol to be printed
    :return: None
    """
    for i in range(0, size):
        for j in range(0, size):
            if i == 0 or i == size-1 or j == 0 or j == size-1:
                print(symbol, end="")
            else:
                print(" ", end="")
        print()


# print(square.__doc__)
