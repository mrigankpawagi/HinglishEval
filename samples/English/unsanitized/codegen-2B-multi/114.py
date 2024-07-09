
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    total = 0
    for i in xrange(len(nums)):
        total += nums[i]
        if total < 0:
            return total
        sums = []
        id = 0
        while len(sums) <= i:
            sums.append(total)
            total += nums[id]
            id += 1

        sums[i+1:] = [total] * (len(sums)-i-1)
        if total + nums[i] in sums:
            return total + nums[i]
    raise Exception

sol = minSubArraySum([-1, -2, -3])
print sol
