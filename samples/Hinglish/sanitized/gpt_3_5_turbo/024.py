def largest_divisor(n: int) -> int:
    """
    Returns the largest number that evenly divides n and is smaller than n.
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
