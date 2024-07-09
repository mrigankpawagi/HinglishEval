
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
    res = []
    for d in str(x):
        #if len(d) not in [2,3]:
        if len(d)>3:
            continue
        digits = [int(l)!=0 for l in d.split('0')]
        # digits = [int(l) for l in d.split('0')]
        digits = '0'.join([str(d) for d in digits])
        if digits not in res:
            res.append(digits)
    return sorted(res)

