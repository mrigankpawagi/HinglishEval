
def minSubArraySum(nums):
    """
    Ek integer array nums diya gaya hai, usme se kisi bhi non-empty sub-array ka minimum sum dhundho.
    Udaharan
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    idx = 0
    while idx < nums.size():
        k = nums[idx]
        if k < 1:
            break
        idx += 1
    return int(k)

