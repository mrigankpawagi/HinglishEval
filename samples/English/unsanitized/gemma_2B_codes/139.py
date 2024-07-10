
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    if type(n) != int:
        raise TypeError('{0}: Should receive an integer', n)
    if n < 0:
        raise ValueError('{0}: Negative numbers are not allowed', n)
    if n == 0:
        return 1
    ret = 1
    c = n
    while c >= 1:
        n_factorial = 1
        for _ in range(1, c + 1):
            n_factorial *= _
        ret = ret * n * n_factorial
        c -= 1
    return ret
