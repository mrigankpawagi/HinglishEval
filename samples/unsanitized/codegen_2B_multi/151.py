def double_the_difference(lst):
    """
    Diye gaye numbers ki list mein se, odd numbers ke squares ka sum return karo.
    Negative ya non-integer numbers ko ignore karo.

    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0

    Agar input list khali ho, to 0 return karo.
    """
    output = 0
    for i in lst:
        output = output + 2 ** (i % 10)
    return output
