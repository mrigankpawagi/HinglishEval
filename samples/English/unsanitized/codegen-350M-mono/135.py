
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    def can_arrange_rec(arr):
        """Helper function that recursively creates lists. Uses recursion. Returns
        the index of the element that is not greater than arr[-1] starting from
        starting from the left child and returns -1 if all elements of arr[-1]
        do not greater than arr[-1].
        """
        result = -1
        if arr[0] >= arr[-1]:
            return -1
        for idx, item in enumerate(arr):
            next_to = arr[idx+1:]
            if item >= arr[idx]:
                continue
            # Check next_to list if item does not meet the largest number in the
            # array.
            # Skip the second highest item whose number is larger than item.
            elif next_to and item < next_to[-1]:
                continue
            else:
                result = arr.index(item)
                break
            # After the item meets the largest number in next_to, recurse on the
            # rest of arr.
            can_arrange_rec(next_to)
        return result

    return can_arrange_rec(arr)

