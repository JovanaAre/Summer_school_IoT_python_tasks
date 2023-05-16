# 1. Napisati funkciju koja vraća rešenja kvadratne jednačine. U posebnom modulu.

import cmath


def quad_equation(a: int, b: int, c: int) -> tuple[complex, complex]:
    """
     Returns the solutions of a quadratic equation

    :param a: Coefficient of x^2
    :param b: Coefficient of x
    :param c: Constant
    :return: Solutions of quadratic equation (tuple x1,x2)
    """
    x1 = (-b + (cmath.sqrt(b**2 - 4 * a * c))) / (2*a)
    x2 = (-b - (cmath.sqrt(b**2 - 4 * a * c))) / (2 * a)
    return x1, x2


# print(quad_equation.__doc__)

