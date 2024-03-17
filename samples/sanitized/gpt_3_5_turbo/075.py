def is_multiply_prime(a):
    """
    Returns True if the given number is a multiplication of prime numbers, and False otherwise.
    Where (a) is less than 100.
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    factors = []
    for i in range(2, a):
        if a % i == 0 and is_prime(i):
            factors.append(i)
    if len(factors) > 0:
        product = 1
        for factor in factors:
            product *= factor
        if product == a:
            return True
    return False
