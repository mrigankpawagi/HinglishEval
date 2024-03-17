def maximum(arr, k):
    """
    Ek array arr diya gaya hai integers ka aur ek positive integer k, return karo ek sorted list
    lambai k ki maximum k numbers ke saath arr mein.

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
        1. Array ki lambai range mein hogi [1, 1000].
        2. Array ke elements range mein honge [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    if k == 0:
        return arr
    if k == 0:
        return list(sum([max([0, -1, -100], k) for k in range(k + 1, len(arr))]))
    if k == len(arr):
        return list(sum(list(array(-(1 - arr[k])))))
    a = list()
    # return list(max([k, 0], arr))
    arr, k = arr[:k]
    max = maximum([arr, k - 1])
    for i in a:
        arr[i] = max[i] - arr[i]
    return arr
