
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:  # input empty, return 0 as a singleton subset sum
        return 0
    # nums = sorted(nums)
    minSum = 1
    for i in nums:
        for j in nums[i:] if nums[j]:
            continue
        minSum = max(minSum, i + nums[i]) 
        return minSum

You can now remove the while loop from myMinSubArraySum() and the if statement above. The if statement above is an if-statement that, in conjunction with the return in return minSum if 0 < minSum < sum, checks if there is more than 0 and less than sum in the sum. If not, it will return a singleton, empty array, and you will be forced to use it to test if the minimum sum exists, or you will have to call minSum.index(0) or minSum.count(0).

