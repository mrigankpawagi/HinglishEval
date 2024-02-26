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
    return xs[0]


def find_one_for(xs: list, x: float) -> float:
    """
    Polynomial ko evaluate ko evaluate karta hai polynomial ko
    evaluate karta hai x par.
    return x(x+1)^2 + x(x+1) + x
    """
    return sum([coeff * math.pow(x + 1, exp) for exp, coeff in enumerate(xs)])


def find_one_for_poly(poly_list, x: float) -> float:
    """
    Polynomial ko evaluate karta hai evaluate ko evaluate karta hai
    evaluate ko evaluate karta hai polynomial ko.
    return 0
    """
    return poly(poly_list, x + 1)


def find_first_difference(x: float, xs: list) -> float:
    """
    Returns the first difference wale x polynomial ek, wale x karva hai
    evaluate ko evaluate karta hai polynomial ko.
    return sum(x_c - x_c+1) for each x_c in xs
    """
    return sum([poly(xs, x - 1) for x in xs])


def find_first_difference_poly(poly_list, x: float) -> float:
    """
    Returns the first difference wale x polyn