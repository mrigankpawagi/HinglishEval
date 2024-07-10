
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    k = k if k >= 0 else len(arr)

    max_idx = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > arr[max_idx]:
            max_idx = i

    return arr[max_idx + k - 1:] if max_idx + k - 1 < len(arr) else arr[:k]

print(maximum([-3, -4, 5], 3))
print(maximum([-4, -4, 4], 2))
print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))
