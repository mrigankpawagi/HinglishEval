def modp(n: int, p: int):
    """
    2^n modulo p return karo (numerics ka dhyan rakho).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    if p is 1:
        return 0
    if n is 0:
        return 1
    m = p - 1
    y = 0
    while m is not 0:
        x = 1
        while m % 2 is 0:
            m //= 2
            y += x
            x *= p
        m //= 2
        y += x
        x *= p
    return y % p