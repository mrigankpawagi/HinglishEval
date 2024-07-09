

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    # TODO: Write this function -- we're starting to look a little goofy
    # as we're going to need to go through the entire list of numbers
    #  before checking the value.

    # TODO: Test divisibility (e.g., n is prime, n*q = prime) by dividing
    #  through each item in the 'numbers' list.

    for e in range(2, n):
        if n % e == 0:
            # print(f"The number: {n} is not a prime due to the divisibility of {e}.")
            return False
    return True

# ------------------------------------------------------------------------
# Using is_prime() as a function definition as we saw in the above problem.

