
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    if not isinstance(lst, list) or len(lst) == 0:
        return None
    
    val1 = lst[0]
    leng = len(lst)
    for i in range(1, leng):
        if val1 > lst[i]:
            val1 = lst[i]
    
    res = lst[0]
    for i in range(0, leng):
        if val1 > lst[i]:
            res = lst[i]
    
    return res 

