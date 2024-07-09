

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    a = number

    # We could've used Decimal, but that only allows whole number input
    maxint = sys.maxsize

    # This function runs in O(logmaxint) time, but logmaxint doesn't
    # scale linearly with the problem, hence the binary search.
    for i in itertools.count(2):
        if 2 ** i >= maxint: break
        b = maxint // i    ## b = integer required after flooring
        n, d = divmod(a, i)

        if 2 ** (i - 1) > n:
            break

        if n in (0, maxint, 1):
            return float(d)
        for j in itertools.count(0):
            if d + 1 <= maxint:
                return float(d) + truncate_number(n) * i
            n, d = divmod(n, i )
            if n > 10**j:
                if truncate_number(n + truncate_number(j) * i) - i <= maxint:
                    return float(maxint * i)


