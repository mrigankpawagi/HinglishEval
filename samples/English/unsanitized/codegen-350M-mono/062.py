

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    result = [1] * len(xs)
    for idx in range(0, len(xs) - 1, 2):
        result[idx + 1] = 0 - result[idx] * xs[idx]
    return result


# print(derivative([1, -2, 3]))
# print(derivative([1, 2, 3]))
# print(derivative([1, 2, 3], 1))


