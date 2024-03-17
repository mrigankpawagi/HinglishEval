

def derivative(xs: list):
    """
    xs ek polynomial ke coefficients ko represent karte hain.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Is polynomial ka derivative same form mein return karo.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [xs[i] * xs[i + 1] for i in range(len(xs) - 1)]

def derivative_2(xs: list):
    """
    xs ek polynomial ke coefficients ko represent karte hain.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Is polynomial ka derivative same form mein return karo.
    >>> derivative_2([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative_2([1, 2, 3])
    [2, 6]
    """
    return [xs[i] * xs[i + 1] for i in range(len(xs) - 1)]

def derivative_3(xs: list):
    """
    xs ek polynomial ke coefficients ko represent karte hain.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Is polynomial ka derivative same form mein return karo.
    >>> derivative_3([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative_3([1, 2, 3])
    [2, 6]
    """
    return [xs[i] * xs[i + 1] for i in range(len(xs) - 1)]

def derivative_4(xs: list):
    """
    xs ek polynomial ke coefficients ko represent karte hain.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Is polynomial ka derivative same form mein return karo.
    >>> derivative_4([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative_4([1, 2, 3])
    [2, 6]
    """
    return [xs[i] * xs[i + 1] for i in range(len(xs) - 1)]

def derivative_5(xs: list):
    """
    xs ek polynomial ke coefficients ko represent karte hain