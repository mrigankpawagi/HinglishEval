
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
    if len(lst) < 2:
        return None

    min_1 = min(lst)
    min_2 = min(lst)

    for i in lst:
        if i < min_1:
            min_2 = min_1
            min_1 = i
        elif i < min_2:
            min_2 = i

    return min_2
