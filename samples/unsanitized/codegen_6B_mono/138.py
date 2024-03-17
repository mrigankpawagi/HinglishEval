
def is_equal_to_sum_even(n):
    """
    Evaluate karo ki diya gaya number n kya exactly 4 positive even numbers ka sum ho sakta hai
    Udaharan
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    is_p_even_list = [i for i in xrange(1, n // 2 + 1) if i % 2 == 0]
    equal_to = n // 2
    for i in is_p_even_list:
        equal_to -= i
    return True if equal_to == 0 else False

