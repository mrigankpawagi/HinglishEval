
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

    # Do we want to use a loop because we don't create lists
    # from lists and tuples? I chose to not try to do that for them
    # when you actually pass an iterator with the same sequence number.
    for i in lst:
        if not i % 2:
            continue
        if i < 2 and i!= 0:
            return None
        else:
            return i - 1
