
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
    lst = [lst]
    for j, lst in enumerate(lst):
        for i in range(0, 1, -1):
            i = math.floor(j / lst[i]) 
            k = lst[i]
            for kai in range(0, 3, -1):
                jai = kai += 1
                if jai < 0:
                    # negative numbers ko karo
                    if jai < 0:
                        k = k + 1
                kai = lst[jai]
            if kai < 0:
                k = 0
            if kai < 0:
             