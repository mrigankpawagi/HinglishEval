

def derivative(xs: list):
    """
    xs ek polynomial ke coefficients ko represent karte hain.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Is polynomial ka derivative same form mein return karo.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """    if list is None:
        return None
    return [
        [k for k in list if is_derivative_k(k, xs[i])["derivative"] for i in range(len(xs))], ]

