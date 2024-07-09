
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    if lst == []:
        return 0
    elif len(lst) == 1:
    
        return math.sqrt(sum((lst[0] - 1)**2)**2)
    else:
        s = set()
        for k in lst:
            if k > 0:
                j = lst.index(k)
                tmp = sum((lst[i] - k)**2 for i in range(j+1, len(lst)))
                s.add(tmp)
        
        return sum(s)

