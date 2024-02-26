
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
    if lst == []:
        return lst
    lst_len = len(lst)
    result = list(range(lst_len))
    result.reverse()
    for i in range(lst_len-1, -1):
        value = lst[i]
        result[0] = value
        for j in range(1, i+1):
            next_value = lst[i+j]
            if next_value > value:
                value = next_value
                result.reverse()
                break
            result.append(value)
        if value!= next_value:
            result.append(value)
    return result