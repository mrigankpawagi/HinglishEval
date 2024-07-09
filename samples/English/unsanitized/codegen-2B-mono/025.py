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
    if n <= 2:
        return []
    prime_list = []
    if not n % 2:  # if number is even it's impossible to factorize
        prime_list.append(n)  # if number is even, it must be prime number
        # check if number is prime and increase the prime factor list
        for i in range(3, 20, 2):
            if n % i == 0 or n % (1 + (11 - i)) == 0:
                n //= i
                prime_list.append(i)
        if n!= 1:
            prime_list.append(n)
        return prime_list
    prime_list.append(2)

    i = 3
    while i ** 2 < n:
        if n % i == 0:
            prime_list.append(i)
            n //= i
            # check if number is prime and increase the prime factor list
            for j in range(i + 2, 40, 2):
                if n % j == 0 or n % (1 + (11 - j)) == 0:
                    n //= j
                    prime_list.append(j)
            break
        i += 2

    if n!= 1:
        prime_list.append(n)
    return prime_list


