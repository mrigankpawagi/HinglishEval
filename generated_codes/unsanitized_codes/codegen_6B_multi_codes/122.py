
def add_elements(arr, k):
    """
    Ek non-empty array of integers arr aur ek integer k diya gaya hai, pehle k elements mein se jinme maximum do digits hai unka sum return karo.

    Udaharan:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """

    # Constraints
    if len(arr) == 1:
        return ord(arr[0])
#
    s = 0
    for i in arr:
        s += ord(i)
    if s < k: # sum < k means sum of elements > k
        return s

    if len(arr) == k:
        return sum(arr)

    # add last 2 k elements
    s = s + (arr[-2] * k)
    if len(arr) > k-1:
        return add_elements(arr[:-1], k) + s
    else:
        return add_elements(arr, k) + s


_ = add_elements([111,21,3,4000,5,6,7,8,9], 4)
print "%s" % _
