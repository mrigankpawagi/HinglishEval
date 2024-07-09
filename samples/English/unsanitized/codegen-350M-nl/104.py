
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    for idx in range(ord(x) + 1):
        if not len(x) == 0 and x[-1] is not None:
            return x
        else:
            return unique_digits(x[-1])
    return [i+1 for i in x]

