

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    p, q = 2, n
    while q > 2:  # 2 < p < q < sqrt(n)
        if n % 12 == 0 and n % 2 ** 3 == 9 and n % 12!= 39 and n % 2 + 2!= q:
            _assert_prime(n)
            q += p
        else:
            p += 2
            n, q = n / 2, n % 2
    return n

# if __name__ == "__main__":
#    print LargestPrimeFactor(2048)
#    print LargestPrimeFactor(10000000)
