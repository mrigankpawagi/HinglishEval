
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! *... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    if not n > 0:
        raise ValueError("non-positive integer expected")
    if not isinstance(n, int):
        raise TypeError("integer expected, got %s instead" % type(n))
    return factorial2(n)


##### Integer arithmetic tests

@check_version(2, 3, 0, "bacon")
