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
    return (f(xs) / f_deriv(xs)[0])


def f(xs: list):
    """
    return f xs ko
    """
    return poly(xs, 1)


def f_deriv(xs: list, order: int = 2):
    """
    return f'_i xs ko
    """
    r = range(1, order + 1)
    x_coeffs = [xs[-i]] * r
    f_prime = sum([coeff * x_coeffs[i + 1] ^ (i + 1) for i, coeff in enumerate(x_coeffs)])
    return f_prime


def find_roots(xs: list):
    """
    return xs ko
    """
    f_prime = f_deriv(xs)
    roots = []
    # f'(x)= 0, f(x)= 0, polynomial ko evaluate ko.
    # so, return point wale polynomial ko root ko.
    if f_prime == 0:
        return xs[0]
    else:
        # find other polynomials ko
        for i, x0 in enumerate(xs):
            if f(xs) - f_prime == 0:
                i = find_zero(xs)
                break

        roots.append(i)
        l = len(xs) - 1
        while True