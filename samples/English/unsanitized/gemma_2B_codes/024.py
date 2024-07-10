

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    current_num = n // 2
    while True:
        if current_num <= 1:
            return current_num
        current_num -= 1
