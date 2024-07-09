
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
    # Method-1. (Pythonic): Sorting array and returning k elements
    """
        n = len(arr)
        arr.sort()
        sorted_arr = [arr[i] for i in range(n) if i < n - k or (i >= n - k and i < 2 * n - k)]
        return sorted_arr
    """

    # Method-2
    def find_Kth(arr, k):
        # Edge case
        if k <= 0 or len(arr) == 0:
            raise ValueError("k needs to be an integer and greater than or equal to 0.")

        # Sort the array
        arr.sort()

        # Find the max value
        return arr[-k]

    # Test your method
    if k < 1 or k > len(arr):
        raise ValueError("The value of k needs to be within the range of 1 to len(arr).")

    kth_element = find_Kth(arr, k)
    # print("The elements for K is:", kth_element)
    # Return sorted array with k elements
    return arr[:k] if kth_element == arr[len(arr) - k] else arr[:-k] + arr[-k:len(arr)]


