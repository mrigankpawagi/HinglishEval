
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
    lg = len(lst)
    if lg == 1:
        return lst[0]
    
    lst = []
    lg = _smallest(lst, lg - 1)
    return lst[lg]
    

if __name__ == "__main__":
    print next_smallest([1, 2, 3, 4, 5])
