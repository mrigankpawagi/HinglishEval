
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    lst = filter(lambda x: x >= 0, lst)
    if len(lst) < 2:
        return -1
    m = 0
    if len(lst) == 1:
        return m
    else:
        for x in lst[:len(lst) - 1]:
            if m > x:
                return m
            else:
                m = m + 1
    return m


