import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    res = min([round(poly(xs, x), 2) for x in xs if poly(xs, x) == 0])
    return ([-1] + list(xs) + [res]) if res else []


def find_roots(xs: list):
    """xs are coefficients of a polynomial.
    find_roots finds the set of all real roots of given polynomial.
    if there are multiple roots, find_roots returns as many lists
    of roots as many roots are there.
    >>> find_roots([-8, 9, -8, 1]) # roots are [-2] and [4]
    [[-2], [4]]
    """
    # TODO: implement me
    pass


if __name__ == '__main__':
    # testing module level method(s)
    import doctest

    doctest.testmod()
