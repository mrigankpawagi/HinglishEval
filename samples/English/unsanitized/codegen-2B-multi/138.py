
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return(2*n % 2 == 0 and is_even(n - 1) == False and is_even(n - 3) == False and is_even(n - 5) == False)

