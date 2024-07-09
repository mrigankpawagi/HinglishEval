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
    if n == 1:
        return []
    factors = [1]
    count = 2
    while n > 0:
        if n % count!= 0:
            factors.append(count)
            n = n / count
        count += 1
    if n!= 1:
        factors.append(n)
    return [n] + [x + 1 for x in factors if fact <= x]


if __name__ == "__main__":
    test_cases = [factorize(n) for n in range(1, 101)]
    for problem in test_cases:
        assert list(reversed(problem)) == sorted(problem), \
            ("Input was not factorization. Problem is: " +
             str(problem))
