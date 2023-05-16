# 2. Napisati generator funkciju koja uvek vraća sledeći član fibonačijevog niza.
# Poseban modul.


def fib_n(n: int) -> list[int]:
    """
    Generator for fibonacci numbers

    :param n: The range for fibonacci generation
    :return: Generator of first n fibonacci nubmers
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# print(fib_n.__doc__)
