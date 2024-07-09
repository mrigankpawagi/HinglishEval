
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
    res = 1
    if n == 1:
        return res

    b = n - 1  # 2
    c = n  # 3
    d = b - 1  # 4
    e = b  # 5

    while True:
        for x in range(c, d + 1):
            res = res * x
        d = e  # 5 (previous value in while)
        e = d + 1  # 6
        b = d  # 5 (previous value in while)
        c = e  # 6
        d = c - 1  # 3
        e = b  # 5 (previous value in while)
        if d <= 5:
            break

    return res
