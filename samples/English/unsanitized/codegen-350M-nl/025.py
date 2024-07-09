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
    # We try hard as usual to preserve order
    # [x for x in factorize(int) if x]
    # since if we try to read the elements we will have a look for a unique factor.
    runes = [r for _, i in zip(n, factorize(_))]  # create a new Runes sequence with the last i
    for r, d in runes[n:]:  # check if the i < n
        if not r:  # check if we can write out our Runes sequence
            runes += [i]  # update the Runes sequence to new position, we are going to print them
            return runes  # return Runes
    return list(factorize(n=d))  # return output
