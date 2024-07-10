
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    for i in range(2, int(round(a**0.5)) + 1):
        if a % i == 0:
            if i > 3:
                return False
            return True
    return False


def is_multiply_prime_1(a):
    # a is number
    if a % 2 == 0 or a == 2:
        return True
    if a % 3 == 0 or a == 3:
        return True
    for i in range(5, int(round(a**(1/3))) + 1, 2):
        if a % i == 0 or a % (i * 2) == 0:
            return True
    return False


def is_multiply_prime_2(a):
    """Return True if is prime, False otherwise.
    """
    for i in range(2, int(round(a**(1/2))) + 1):
        if a % i == 0:
            return False
    return True
