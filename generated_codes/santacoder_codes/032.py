import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Polynomial ko evaluate karta hai coefficients xs ke saath point x par.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """   current_x = 0
    polynomial = 0
    while 1:
        polynomial += poly(xs, current_x)
        if math.isclose(current_x, 0, abs_tol=1e-2):
            zero_idx = xs.index(0)
            return current_x, zero_idx
        else:
            current_x += 0.001

