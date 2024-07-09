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
    assert isinstance(ns, list)
    if not ns:
        ns = []
    assert len(ns) >= 2
    n = len(xs)
    s = [1 for x in xs]
    r = [0]
    for i, x in enumerate(xs):
        r.append(x * x - n * n * x)
    i = 0
    while i < len(r) - 1:
        y = r[i]
        for j, x in enumerate(r[i:]):
            r[j] = y + x
            if j + 1 == i:
                return r, s
    return r, s