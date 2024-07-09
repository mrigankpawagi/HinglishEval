
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
    if (not lst):
        return []
    new_lst = [lst.pop(0)]
    while lst:
        if(new_lst[len(new_lst)-1] > lst.pop(0)):
            new_lst.append(lst.pop(0))
    return new_lst


if __name__ == '__main__':
    lst = [2, 3, 1, 4]
    print("The original list is : {0}".format(lst))
    print("The result is : {0}".format(strange_sort_list(lst)))
