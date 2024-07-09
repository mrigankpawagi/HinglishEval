
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
    if not lst:
        return []

    min_val, max_val = min(lst), max(lst)

    lst = [x for x in sorted(lst)]

    first_index = 0
    last_index = len(lst) - 1

    while min_val <= lst[first_index]:
        first_index += 1
    while max_val >= lst[last_index]:
        last_index -= 1

    first_list = lst[:first_index]
    second_list = lst[first_index:last_index+1]
    third_list = lst[last_index+1:]

    return strange_sort_list(third_list) + \
        strange_sort_list(second_list) + \
        strange_sort_list(first_list)

for i in xrange(int(raw_input())):
    n = int(raw_input())
    result = strange_sort_list(n)
    print 'Case #{}: {}'.format(i+1, str(result))
