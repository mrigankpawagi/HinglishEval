

def derivative(xs: list):
    """
    xs ek polynomial ke coefficients ko represent karte hain.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Is polynomial ka derivative same form mein return karo.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) < 2:
        raise ValueError(f"length {len(xs)} does not equal {2}")
    if len(xs) % 2!= 0:
        raise ValueError(f"length {len(xs)} does not equal {(len(xs) - 1) // 2}")
    first_polynomial = [xs[0], xs[1]]
    last_polynomial = xs[-1]

    for i in range(1, len(xs) - 1):
        first_poly_tmp = first_polynomial[-1] + (xs[i + 1] - xs[i]) / (2 * (xs[i] ** 2 - xp))
        last_poly_tmp = last_polynomial + (xs[i:] - [xs[i], -(xs[i + 1] * xp - xs[i + 1]) / (xs[i + 1] ** 2 - xp)]) / (2 * (xs[i + 1] ** 2 - xp))
        first_polypolynom<mask_1><sep><mask_1>ial.append(first_poly_tmp)
        last_polypolynomial.append(last_poly_tmp)

    res = first_polynomial[-2] * last_polycoeff[-1] - first_polypolynomial[-2] * last_polypolynomial[-1]

    return [first_polynomial[-1], last_poly_from_last(last_polynomial[-2]), res]

from math import factorial, log
__factorial = factorial
__lgamma = log(__factorial(__factorial(__factorial(__factorial(__