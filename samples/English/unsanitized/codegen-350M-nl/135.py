
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if not (len(arr) < 2):
        return -1
    # Create a new array
    new_arr = arr[-1]
    if (len(new_arr) < 2):
        new_arr = arr
    arr = new_arr
    if len(arr) > 1:
        arr = [1][]
    return new_arr[len(arr)-1]

class Solution:
    def can_arrange(self, arr):
        """
        Create a function which returns the largest element of array
        which doesn't have a duplicate value of 1.
        """
        for i in (1,2,4,3,5):
            arr[len(arr)-1] = 1
        return can_arrange(arr)
