
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    total = sum(arr)
    index = 0
    changed = 0
    while total == 0:
        cpy = []
        count = None
        for i in range(index - 1, -1, -1):
            if count == None:
                cpy.append(arr[0])
                count = 1
            else:
                cpy.append(arr[index])
                new_count = count * (-1)
                count = new_count
        print('%s changed to %s' % (cpy[0], cpy[-1]))
        total -= count
        index += 1
    return index

A:

#!/usr/bin/python

