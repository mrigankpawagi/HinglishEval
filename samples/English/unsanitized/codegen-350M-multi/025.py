from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n > 0:
        if n % 2 == 0:
            factors.append(n)
        elif n % 3 == 0:
            factors.append(3 * n // (3 * n - 1))
        else:
            i = n // (3 * n - 1)
            if factors.count(i) < n // n:
                factors.append(3 * n // (3 * n - 1))
            else:
                factors.append(2 * i)

    return factors


# *****************************************************************************
# ***                      COMPUTATION                                   ***
# *****************************************************************************

