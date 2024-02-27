
def is_equal_to_sum_even(n):
    """
    Evaluate karo ki diya gaya number n kya exactly 4 positive even numbers ka sum ho sakta hai
    Udaharan
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    if n == 1:
        return True
    elif n == 4:
        udaharan = 0
        ka_sum = 4
        sak_sum = 1
        is_equal_to_sum_even(ka_sum)
        is_equal_to_sum_even(sak_sum)
    elif n == 6:
        udaharan = 2
        ka_sum = 3
        sak_sum = 2
        is_equal_to_sum_even(ka_sum)
        is_equal_to_sum_even(sak_sum)
    elif n == 8:
        udaharan = 10
        ka_sum = 3
        sak_sum = 2
        is_equal_to_sum_even(ka_sum)
        is_equal_to_sum_even(sak_sum)
    else:
        raise RuntimeError, "Unknown comparison k of n {} is_equal_to_sum_even(n)".format(n)

