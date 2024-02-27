

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
    """   if n == p:  # handle small numerics
        return 1

    p2 = pow(p, 2)  # if p is a power of 2 use modp with 1 and modp 2
    d1 = pow(p, n % p2)
    d2 = pow(p, (n + 1) % p2) % p2
    return d1 % d2
