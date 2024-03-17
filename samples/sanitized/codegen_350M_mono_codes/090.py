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
    for i in range(1, len(lst)):
        for j in range(len(lst) - i):
            if lst[j + 1] < lst[j]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
                break
        if len(lst) == 2:
            break
    return lst[1]