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
    return sum([coeff * math.pow(xs[i], i) for i, coeff in enumerate(xs)])


def solve_poly(xs: list):
    """
    Polynomial ko evaluate karta hai coefficients xs ke saath point x par.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    coeffs = []

    for i in range(xs[0], -1, -1):
        for j in range(1, xs[0]):
            if i!= 1 and j!= xs[0]:
                coeffs.append((-(xs[j] - xs[i-1]) / (xs[j] - xs[i]))))
            if j!= xs[0]:
                coeffs.append(-xs[j+1] / (xs[j+1] - xs[j]))

        if i!= xs[0]:
            coeffs.append(i)

    return coeffs


def poly2(xs: list, x: float) -> float:
    """
    Polynomial ko evaluate karta hai coefficients xs ke saath point x par.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] *