
def is_equal_to_sum_even(n):
    """
    Evaluate karo ki diya gaya number n kya exactly 4 positive even numbers ka sum ho sakta hai
    Udaharan
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    a = [1,2,3,4]
    for i in range(10):
        nums = [i] + a
        if is_sum_of_even_ints_in(nums, n):
            return True
    return False
