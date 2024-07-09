
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
    for i in range(0, len(lst)):
        res = list(sort_list(lst[i]))
        return res
    for item in sort_list(lst):
        if len(item) % 2 == 0:
            return lst[:i], lst[i:]
    return lst[-1]

The sort_list is used only once.

Sorts the list in order by min(max(i), j), if you like, and returns sorted in order of min(max(i), j). Sorting the list again by max(i), j, would work out of the box, except that you would get different results if different size of arrays were passed, since max is computed with respect to the other arrays, not with respect to this other type of array (it is a tuple).

A:

Possible modifications:
