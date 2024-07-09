
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0

    minSub = nums[0] + min(nums[1:])
    for i in range(1, len(nums)):
        if minSub > nums[i]:
            minSub = nums[i] + min(nums[(i - 1) : nums.length])

    return minSub
