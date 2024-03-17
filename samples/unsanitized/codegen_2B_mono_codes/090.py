
def next_smallest(lst):
    """
    Aapko ek list di gayi hai integers ki.
    Ek function likho next_smallest() jo list ka 2nd sabse chhota element return kare.
    Agar aisa koi element nahi hai to None return kare.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """ 
    if not lst:
        return 
    if len(lst) == 1:
        return lst[0]
    if lst[1] >= lst[0]:
        return 
    while lst[1]!= lst[0]:
        left = sorted(lst[1], reverse = True)
        if left == lst[1]:
            return left 
        else:
            lst[1] = left[0]
        
