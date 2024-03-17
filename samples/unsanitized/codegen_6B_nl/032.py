import math


def poly(xs: list, x: float):
    """
    xs coefficients wale polynomial ko point x par evaluate karo.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Polynomial ko evaluate karta hai coefficients xs ke saath point x par.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    for i in range(1, len(xs) - 1):
        if abs(poly(xs, x)) == 0:
            return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
        if abs(poly(xs, x + 2)) == 0:
            return xs[0] + xs[1] * x + (2 * xs[1]) * x^2 +.... xs[n] * x^n
        if abs(poly(xs, x + 10)) == 0:
            return xs[0] + xs[1] * x + (10 * xs[2]) * x^3 +...
                (10 * xs[2]) * x**4 +.... xs[n] * x^n


_x = 3
_y = 6
_n = 3
_d_num = 2
_d_den = 2
_d_e = 1
_d = 1


def test():
    xs = [