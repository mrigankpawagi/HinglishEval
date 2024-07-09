
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
    if not arr or len(arr) == 1:
        return 0
    mid_index = int(len(arr)/2)
    last_element = arr[len(arr)-1]
    first_element = arr[0]
    
    left_part = smallest_change(arr[:mid_index])
    right_part = smallest_change(arr[mid_index:len(arr)-1])
    sub_result = (first_element + last_element) - (last_element * 2)
    return min(left_part, sub_result) if left_part!= 0 else right_part
    
# The main function that gets the data from the user
