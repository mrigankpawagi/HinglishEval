
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    start = 0
    end = 0
    max_diff = 0
    for i, x in enumerate(arr):
        if x == arr[i-1]:
            start = end = i
        else:
            end += 1
            if max_diff < end - start:
                max_diff = end - start

    if not (start >= 0):
        return -1

    return max_diff
