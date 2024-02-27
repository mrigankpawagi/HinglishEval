def minSubArraySum(nums):
    """
    Ek integer array nums diya gaya hai, usme se kisi bhi non-empty sub-array ka minimum sum dhundho.
    Udaharan
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    r = [num, num, num, num, num, num, num, num, num, num, 0, 0, 0, 0, 0, 0]
    for i in r:
        l[i] = minSubArraySum(nums[i])[0]
    for i in l:
        l[i] = minSubArraySum(l[i])
    return sum(l[:2] + [r[:2]])
