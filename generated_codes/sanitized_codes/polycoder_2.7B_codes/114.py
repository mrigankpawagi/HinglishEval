def minSubArraySum(nums):
    """
    Ek integer array nums diya gaya hai, usme se kisi bhi non-empty sub-array ka minimum sum dhundho.
    Udaharan
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    temp = list(map(tuple, nums))
    temp.sort()
    result = 0
    left = 0
    right = 0
    while left <= right:
        mid = (left + right) // 2
        curr = temp[mid]
        if curr <= 1:
            left = mid + 1
        else:
            right = mid - 1
            result = max(result, curr)
    return result
