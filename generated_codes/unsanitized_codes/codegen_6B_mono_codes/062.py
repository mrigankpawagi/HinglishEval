

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
    assert len(xs) >= 2
    p = get_coefficients_by_list(xs)
    d = []
    for i in range(len(p)+1):
        d.append(p[i])
        for j in range(len(p) - i):
            d[i] = d[i] * i + p[j + i]
    return d
