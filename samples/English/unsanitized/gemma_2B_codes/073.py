
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
    dp = {}
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            dp[[arr[i]] = i
            continue
        dp[[arr[i], (arr[i] - 1 + (len(arr) + 2)) % (len(arr) + 2)]] = i
        dp[[arr[i], (arr[i] + 1) % (len(arr) + 2)]] = len(arr) + 1 + i]]
        dp[[arr[i], (arr[i] + (len(arr) + 2)) % (len(arr) + 2)]] = len(arr) + 1 + i]]
        dp[[arr[i], arr[i] % (len(arr) + 2)]] = i

    min_change = int(1e6)
    for p, i in dp.items():
        if len(arr) % 2 != 0 and p[0] > p[1]:
            continue
        if i > min_change:
            break # already too deep
        for i in range(p[0], min(p[1] - 1, len(arr) // 2)):
            if arr[i] % 2 == 0:
                continue
            min_change = min(min_change, i)
    return min_change
