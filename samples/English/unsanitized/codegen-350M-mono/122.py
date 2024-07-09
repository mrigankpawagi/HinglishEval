
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    # the sum of first n elements of size k:
    sum = 0
    # check if index < k or index == k
    # return first k elements, and sum to the next index
    if len(arr) in range(2 * k + 1) and arr[-k - 1] >= '0':
        # if len(arr) is in range and size is greater than k
        # use it directly, use count of elements by that index
        sum += arr[-k - 1]
    # elif index >= k, use 0 by default
    else:
        sum = 0
    return sum