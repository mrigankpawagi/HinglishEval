
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum, sum = 0, 0
    for num in nums:
        print(num, sum)
        if sum == 0 and num >= 0:
            if num > 0:
                sum = num
        else:
            sum += num
            print(sum)
            print("sum is : ", sum)
        if sum <0:
            sum += num
            min_sum += sum
        else:
            min_sum += sum
            print("sum is : ", min_sum)
        print(min_sum)
    return min_sum


if __name__ == '__main__':
    print(minSubArraySum([-1,-2,0,1,2,2,2,4,4,4]))
