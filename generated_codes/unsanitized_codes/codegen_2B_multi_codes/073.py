
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
    if len(arr) < 2:
        return 0
    left_is_odd = False
    current = arr[0]
    left = 1
    if arr[0] % 11 == 1:
        left_is_odd = True
    for left in range(1, len(arr)):
        current = arr[left]
        if left < len(arr) - 1:
            current += arr[left + 1]
        if left > 0:
            if left-1 == 0:
                if current%11 == 1 or current%11 == 7:
                    left_is_odd = False
                    if current % 11 == 2:
                        left_is_odd = True
            elif left < len(arr) - 2:
                current -= arr[left + 2]
            else:
                last_left = left - 1
                current -= arr[last_left]
        if left_is_odd or arr[0] > 9:
            if current%11 == 2:
                left_is_odd = True
        else:
            current += arr[0]
        arr[left] = left_is_odd and current % 11 or current + 10
        left += 1
    return len(arr) - 1
