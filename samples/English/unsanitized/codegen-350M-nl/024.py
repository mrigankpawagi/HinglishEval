

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # We'll do some checking to ensure that this gives us a valid NIL object
    if n <= 0:
        print 'Nil'
    # For a given number n, find the smallest number that divides n
    return abs(n) <= n and n > 0

