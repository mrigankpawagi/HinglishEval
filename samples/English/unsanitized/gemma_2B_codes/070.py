
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
    new_list = [x for x in [5, 5, 5, 5] if x != -5 ]
    print(lst)
    print(new_list)
    x_index = 0
    new_lst_index = 0
    while len(new_list) is not 0:
        for i in range(0, new_list[0]):
            if i not in new_list:
                new_list = new_list + [x for x in [0, 1, 2, 3] if x != -5 ]
                new_lst_index = new_lst_index + 1
                print('added ', x)
            else:
                new_list.remove(new_list.index(i))
                print('removed', i)
        if i == new_list[0]:
            x_index = new_lst_index
            new_lst_index = 0
        if len(new_list) == 0:
            new_list = new_list + [x for x in [3, 2, 1] if x != -5 ]
            return new_list
        new_lst_index = new_lst_index + 1
        print('current index', i, 'current size', len(new_list), x_index, new_lst_index, new_list)
    return new_list
