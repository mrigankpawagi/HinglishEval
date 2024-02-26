
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if not (n % 2 == 0 and n-2*a_and_b_sum_even == 0 and 2*b_sum_odd == 0):
        return False
    return a_sum_even(n) == 0 and b_sum_odd(n) == 0



