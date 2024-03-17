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
    """   if xs[0] > xs[1]:
        return 0.0
    elif xs[0] > xs[2]:
        return 1.0
    elif xs[1] > xs[2]:
        return -1.0
    else:
        return xs[1] * xs[2]

