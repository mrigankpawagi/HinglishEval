
def minSubArraySum(nums):
    """
    Ek integer array nums diya gaya hai, usme se kisi bhi non-empty sub-array ka minimum sum dhundho.
    Udaharan
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    nums_index = -1
    nums_sum = 0

    while nums_index!= -1:
        if len(nums[nums_index]) == 1 and nums[nums_index][0] >= 0:
            nums_sum += nums[nums_index][0]
            nums_index = -1
        else:
            nums_index += 1

    return nums_sum


