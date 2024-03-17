
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
    odd_sum = 0   # empty sum
    zeros = 0     # evens are zero     
    for i in lst:    
        if i % 2 == 1:
            odd_sum = odd_sum + i**2
        if i % 2 == 0:
            zeros = zeros + i
    
    if odd_sum > 0: # if odd_sum > 0, return odd_sum
        return odd_sum
    if odd_sum == 0: # if odd_sum == 0, return +zeros
        return odd_sum + zeros
   