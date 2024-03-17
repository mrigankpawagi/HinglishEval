def is_equal_to_sum_even(n):
    """
    Evaluate karo ki diya gaya number n kya exactly 4 positive even numbers ka sum ho sakta hai
    Udaharan
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n <= 4 and n % 2 == 0:
        return False
    if n == 4 or n == 6 or n == 8:
        return True
    for i in range(1, 5):
        if n % i == 0:
            if is_equal_to_sum_even(n // i) == False:
                return False
    return True