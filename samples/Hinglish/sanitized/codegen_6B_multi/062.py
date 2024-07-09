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
    try:
        k1 = 0
        k2 = len(xs) - 1
        cout = [[k1]]
        for i in range(k2 + 1):
            cout.append(
                list(map(lambda x: x * get_it_tuple(i), xs)) + (numpy.power(xs[i], i),)
            )
        return list(map(lambda x: numpy.sum(x), numpy.array(cout)))
    except TypeError as e:
        return False