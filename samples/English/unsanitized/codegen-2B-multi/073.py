
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
    # If the length of the array is 1, return 0
    if len(arr) == 1:
        return 0
    
    # Sort arr. If the length of the array is 2, compare the first two values and return whether
    # or not both are equal
    if len(arr) == 2:
        if arr[0]!= arr[1]:
            return 1
        else:
            return 0
    # Check the number of elements on its own and sum the same value
    elif len(arr) == 3:
        total_val = arr[0] + arr[1] + arr[2]
        return abs(total_val - smallest_change(arr[:2]))
    # If the length of the array is 4, take the 3-to-6, 6-to-3 range and compare the indices of
    # the elements. If they are all in either direction, check their values for whether they're equal
    # and return 0 if equal and 1 if not equal so that we can skip all 4 subtletials quickly.
    elif len(arr) == 4:
        # Compare the first and second indices and return if they're both equal
        if arr[0] == arr[1] and arr[2] == arr[3]:
            return 0
        elif arr[0] == arr[1] or arr[0] == arr[3] or arr[2] == arr[3]:
            return 1

        # Split these values into 3 lists, and take the sum of each list
        # 2 to 3 --> 0 + 0 + 0, 4 to