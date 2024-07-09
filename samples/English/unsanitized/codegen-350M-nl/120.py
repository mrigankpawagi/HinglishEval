
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
    if k < 1:
        raise ValueError(
            "k must be less than 1, not " + str(k))
    n = len(arr)
    while k < n:
        k0 = k + n - 1
        arr[0] = max(arr[0], [c * k0 for c in n])
        arr[n - 1 - k0] = k0
    k += 1

    # Sort the maximum array
    return max([c for c in arr[0]], k)

### Python

    @classmethod
    def max_int(cls, arr):
        """
        Returns a sorted list of the maximum integer in arr
        """
        maxk