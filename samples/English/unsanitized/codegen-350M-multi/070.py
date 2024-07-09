
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    res = []
    for elem in lst:
        if elem % 2 == 0:
            if elem < 0:
                res.append(-1 if (res[-1] + elem - res[-2]) % 2 == 1 else res[-2])
            else:
                res.append(res[-1] + elem - res[-2])
    return res

