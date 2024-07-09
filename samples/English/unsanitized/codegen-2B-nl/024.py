

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    return (n - n // abs(n) if n//abs(n)>0 else n) // abs(n)