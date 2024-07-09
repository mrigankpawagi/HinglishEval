
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # n = len(nums)
    # if not nums:
    #     return 0

    # start, end = 0, 0
    # min = float('inf')
    # sum = 0
    # while end < len(nums):
    #     while end < len(nums):
    #         sum += nums[end]
    #         end += 1
    #         if sum < min:
    #             min = sum
    #     start += 1
    # return min

    max_sum = float('-inf')
    sum = 0

    for i in range(len(nums)):
        sum += nums[i]

        while sum <= max_sum:
            sum -= nums[i]

        max_sum = max(max_sum, sum)

    return max_sum


if __name__ == '__main__':
    # arr =[1,2]
    #  arr = [2,3,4]
    #  arr =[13, 5, 1]
    # arr = [2, 3, 4]
    arr =[3,2,5,7,4,6]

    # arr = [5, 8, 100, 5, 8, 20]

    # arr = [2,3,4,5,6,7,0]
    # arr =[1,2,3,4,11,5]

    print('Min subarray length is:',
          minSubArraySum(arr))
