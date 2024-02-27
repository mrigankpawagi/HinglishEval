
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
    
    odd = []
    
    # sum_two = 0
    # karo.append( sum_two )
    sum_two = 0
    sum_eight = 0
    
    for integer in lst:
        if integer % 2 == 0:
            sum_two += integer
        elif integer % 2 == 1:
            sum_eight += integer
            karo.append(integer)
    
    output = []
    for element in lst:
        if element not in odd:
            output.append(element)
    for element in odd:
        list_odd.append(element + sum_two)
        list_odd.append(element + sum_eight)
        
    return list_odd

my_list = double_the_difference([1, 3, 2, 0])
print my_list