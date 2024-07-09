
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
    if (len(lst) > 1):
        tmp = []
        for i in range(len(lst)):
            tmp.append(lst[i])
        for i in range(1, len(lst), 2):
            tmp.append(max(tmp))
        for i in range(len(tmp) - 1, -1, -1):
            tmp.append(min(tmp))
        tmp.reverse()
        return lst + tmp

print strange_sort_list([])
print strange_sort_list([1,2,3,4])

I run the code on my mac and I get the following output:
$ python2.7 strange_sort_list.py
[1]
[1, 4, 2]

[1]
[4, 2, 1]

[1, 2, 3, 4]

[4, 2, 1]
[4, 1, 2, 3]

[4, 2, 1]

A:

Since (len(lst) > 1) will be False until len(lst) == 1

