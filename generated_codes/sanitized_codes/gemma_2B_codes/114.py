
def minSubArraySum(nums):
    """
    Ek integer array nums diya gaya hai, usme se kisi bhi non-empty sub-array ka minimum sum dhundho.
    Udaharan
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    min_sum = nums[0]
    min_index = 0
    for i in range(1, len(nums)):
        if nums[i] < min_sum:
            min_sum = nums[i]
            min_index = i
        if min_sum < 0:
            min_sum = 0
    return min_sum
