

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
    return 0 if n == 0 else (
        pow(2, int(math.log(n, 2))) - pow(n % 2, int(math.log(p, 2)))
    ) % (p - 1)