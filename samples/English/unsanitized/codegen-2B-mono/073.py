
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
    l, r, count, min_count = 0, len(arr) - 1, 0, float('inf')
    while l <= r:
        if abs(arr[l] - arr[r]) < min_count:
            count = 1
            min_count = abs(arr[l] - arr[r])
            mid = l
        elif abs(arr[l] - arr[r]) == min_count:
            count += 1
            min_count = abs(arr[l] - arr[r])
        l += 1
        r -= 1
    return min_count - 1  # -1 because change mid element to any of them.


# Tests
assert (smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4)
assert (smallest_change([1, 2, 3, 2, 1]) == 0)
print('Done')
assert (smallest_change([1, 2, 3]) == 1)
assert (smallest_change([1, 2, 3, 4, 3]) == 1)
assert (smallest_change([1, 2, 3, 2, 6, 4]) == 1)

assert (smallest_change([9, 8, 7, 1, 2, 3, 4]) == 1)
assert (smallest_change([9, 8, 7]) == 0)
assert (smallest_change([1, 3, 4]) == 1)

assert (smallest_change([]) == 0)
assert (smallest_change([100000000000, 2, 3]) ==