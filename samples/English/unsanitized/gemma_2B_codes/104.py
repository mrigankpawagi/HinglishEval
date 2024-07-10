
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
    digits = {}
    result = []
    for i in x:
        if i not in digits:
            if isNumberEven(i):
                digits.update({i: list(str(i)[1::])})
                result.append(i)
        else:
            if isNumberEven(digits[i].pop()[-1]):
                digits[i].append(i[-1])
