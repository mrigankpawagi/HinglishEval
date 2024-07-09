import math


def poly(xs: list, x: float):
    """
    xs coefficients wale polynomial ko point x par evaluate karo.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Polynomial ko evaluate karta hai coefficients xs ke saath point x par.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """   if len(xs) == 0:
        return None
    p = 0
    for i, coeff in enumerate(xs):
        if coeff == 0:
            p += 1
        elif coeff == 1:
            p -= 1
        elif coeff == n:
            p += 1
        else:
            raise IndexError
    return p

