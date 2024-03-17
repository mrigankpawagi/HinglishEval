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
    if p == 0:
        raise ValueError("invalid prime")
    if n == 0:
        return 1
    if n <= 0:
        raise ValueError("invalid number")
    if p % 2 == 0:
        k = 0
    else:
        k = 1
    if n == 1:
        return k

    for i in range(2, int(np.ceil(np.log2(n)) + 1)):
        if pow(k, i, p) == 1 or pow(k, i, p) == n - 1:
            continue
        else:
            break

    x = pow(k, int(np.ceil(np.log2(n)) - i) + 1, p)

    return x if pow(x - n, i, p) == n - 1 else n - x
