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
    poly = list(map(int, "".join(map(str, xs)).replace(" ", "").split(",")))
    # print('poly', poly)
    poly = [p for p in poly]  # poly to integer
    poly.append(1)
    return poly