

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
    n = ((n // n) + (int(n / 3)) & long(-n & ~int(-n)) & 255)
    if (int(p * n) & long(-n & ~int(-n)):
        p = p & 7
    return n

