

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    
    if len(l) == 0:
        return False

    temp = 0
    comparisons = set()
    for i in l:
        if i in comparisons:
            return False
        comparisons.add(i)
        for j in l:
            if i + j == 0:
                return True 
            temp += j
    return False
#Another way, 
