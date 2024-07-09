

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
    # TODO: Write your best solution here
    if not l:  # we can't check for empty list.
        return False
    if len(set([d for lst in l for d in l if d == lst]))!= len(l):
        return False
    return True


print(pairs_sum_to_zero([13, 0]))
# True

print(pairs_sum_to_zero([1, 3, 0, 5, -2, 1]))
# True

print(pairs_sum_to_zero([7, 10, 5, -7, 4, 1]))
# True
