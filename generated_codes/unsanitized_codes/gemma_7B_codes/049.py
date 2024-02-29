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
    if n == 0:
        return 1
    elif n % 2 == 0:
        return modp(n // 2, p) ** 2 % p
    else:
        return modp(n - 1, p) * modp(n - 1, p) % p


if __name__ == "__main__":
    import doctest

    doctest.testmod()
