def minSubArraySum(nums):
    """
    Ek integer array nums diya gaya hai, usme se kisi bhi non-empty sub-array ka minimum sum dhundho.
    Udaharan
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = nums[0]
    current_sum = nums[0]
    for num in nums[1:]:
        current_sum = min(current_sum + num, num)
        min_sum = min(min_sum, current_sum)
    return min_sum
