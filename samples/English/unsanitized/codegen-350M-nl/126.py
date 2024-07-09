
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    res = []
    for l in lst:
        value = (l[0] * (l[0] + l[1])) % len(lst)
        # Is the value in the last element of l > the highest already
        # sorted?
        if not (sorted and value <= l[-1] and l[-1] < value < l[1]):
            value = (l[0] * value + l[1]) % len(lst)
            # Is this number one or more of the same value? (If True then it
            # is not in the list)
            if res:
                res = res + sorted(lst)
   