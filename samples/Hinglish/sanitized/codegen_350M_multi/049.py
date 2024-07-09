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
    k = int(math.pow(2, (p - 1)))
    for i in range(2, n):
        if i:
            k = k - 1
        if (i * (2**i - 1) ** i) / (n - 1) > 1:
            k = k + 1
    return k**p