def is_equal_to_sum_even(n):
    """
    Returns True if the given number n can be expressed as the sum of exactly 4 positive even numbers, False otherwise.
    Examples:
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n % 4 == 0
