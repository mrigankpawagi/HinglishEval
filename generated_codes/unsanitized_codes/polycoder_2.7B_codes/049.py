

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
    try:
        a = np.mod(n, p)
    except ValueError:
        a = 0

    try:
        p = a ** 2
    except ValueError:
        p = a

    return a, p

