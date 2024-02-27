

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

    # d = d1 * d1 - d2 * d2
    d = [0] * len(xs)
    for i, j in zip(range(len(xs) - 1), range(len(xs) - 2, -1, -1)):
        s = 0
        for k in range(i, j + 1):
            s += 1 / xs[k] * d[i]
        d[i] = s
    return d


