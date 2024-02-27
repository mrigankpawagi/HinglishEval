
def is_equal_to_sum_even(n):
    """
    Evaluate karo ki diya gaya number n kya exactly 4 positive even numbers ka sum ho sakta hai
    Udaharan
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    check = False
    if check is False:
        yh = len(str(n))
        if (yh-1) % 2 == 0:
            check = True
        if check == True and (yh - 1) % 2 == 0:
            check = False
    return check


#