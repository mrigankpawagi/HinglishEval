def minSubArraySum(nums):
    """
    Ek integer array nums diya gaya hai, usme se kisi bhi non-empty sub-array ka minimum sum dhundho.
    Udaharan
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    i = 0
    minSum = 0
    # 1. The idea is to store sums of sub-arrays in an array. For eg, if there are n = 5 sub-arrays:
    #     [0, 1, 2, 3, 4] Sum(0, 1) = 1, Sum(1, 2)=3, Sum(3, 4)=2
    sums = []
    for index, elem in enumerate(nums):
        sums.append(elem)
        i = index
        while i < len(nums):
            sums[i] += nums[i - 1]
            i += 1
    minSum = sums[0]
    for val in sums:
        if val < minSum:
            minSum = val
    return minSum