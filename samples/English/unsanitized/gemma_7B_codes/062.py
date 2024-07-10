

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

    l = []
    for i in range(2, len(xs) + 1):
        l.append(xs[i-1] * i)
    return l




def partial_derivatives(xs: list, degree: int):
    l = derivative(xs)
    for i in range(2, min(len(xs), degree)):
        l = derivative(l)
    return tuple(l)




if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(partial_derivatives([1, 2, 3], 2))
    print(partial_derivatives([1, 2, 3], 3))
    print(partial_derivatives([2, 7, 6, 3, 4], 2))
