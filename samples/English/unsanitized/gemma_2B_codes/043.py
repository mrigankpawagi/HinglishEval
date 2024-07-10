

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
## your code goes here!
    i = 0
    while i < len(l):
        j = i+1
        while j < len(l):
            # check if current pair's sum is 0
            
            if l[i] + l[j] == 0:
                return True
        
        i += 1
##            
    return False
    
## test your function by calling it with different lists using these:
##     >>> pairs_sum_to_zero([1, 3, 5, 0])  # True
##     >>> pairs_sum_to_zero([1, 3, -2, 1]) # True
##     >>> pairs_sum_to_zero([1, 2, 3, 7]) # return False instead of True, because there are distinct elements
##     >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7]) # False
##     >>> pairs_sum_to_zero([1])   # False
##
