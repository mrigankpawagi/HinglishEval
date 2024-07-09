
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    return min(nums[1:]) + min(nums[2:])


class Solution(object):
    def minSubArraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)
