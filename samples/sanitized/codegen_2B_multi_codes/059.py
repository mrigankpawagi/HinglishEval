

def largest_prime_factor(n: int):
    """
    n ka sabse bada prime factor return karo. Maan lo ki n > 1 hai aur yeh prime nahi hai.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """   if n == 1 or n == 2:
        return 1

    prime_finder = PrimeFinder()
    i = prime_finder.nextprime(n)
    i -= 1

    while i >= 2:
        if n % i == 0:
            # check is not prime because when divide it is still not prime, but
            # then add 1 more prime to get to the next prime
            # if prime_finder.nextprime(n - i) == 1:
            continue
        i += 1

    return i + 1
