

def derivative(xs: list):
    """
    xs ek polynomial ke coefficients ko represent karte hain.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Is polynomial ka derivative same form mein return karo.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """        y = [0]
    # we need to be careful of zero coefficiences because
    # xs is a list rather than a tuple
    if( len(xs) > 3 ):
        for x in range(3, len(xs) + 1):
            y.append(ys[ys.index(max(ys))-(x-3)] * x + max(ys))
        y.append(y[y.index(max(y))+1])
        return y
    else:
        for x in range(3, len(xs) + 1):
            y.append(ys[ys.index(max(ys))-(x-3)] * x + max(ys))
        return y

