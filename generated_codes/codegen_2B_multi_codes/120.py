
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
    if len(arr) == 0:
        return []

    if arr[k-1] < arr[0]:
        return [arr[0], arr[k-1]]

    if len(arr) == 1:
        return arr

    if arr[k-1] > arr[k-2]:
        return [[arr[0]]] + maximum(arr[k-2:], k)

    return maximum(arr[k-1:k-2], k) + [[arr[k-1]]]


class Solution(object):
    def maximumSwap(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """

        l = []
        for i in range(k+1,len(arr)):
            l.append([])
        for i in range(len(arr)):
            l[i%(k+1)].append(arr[i])
        print(l)
        maxn = [i for i in l]

        maxn = []
        k = 0
        for i in range(len(maxn)):
            if len(maxn[i]) > len(maxn[0]):
                maxn[0] = maxn[i]
                k = i
        