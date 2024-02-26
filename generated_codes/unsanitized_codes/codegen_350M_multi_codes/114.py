
def minSubArraySum(nums):
    """
    Ek integer array nums diya gaya hai, usme se kisi bhi non-empty sub-array ka minimum sum dhundho.
    Udaharan
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0
    if len(nums[0]) == 1:
        return min([x for x in nums if x > 0])
    for i in range(len(nums)-1):
        for j in range(1, len(nums)-1):
            suma = 0
            for k in range(j):
                suma += nums[i]
                if k > i - j - 1:
                    continue
                if nums[i] < nums[k]:
                    suma += nums[k]
            suma += nums[i]
            for k in range(j):
                suma -= nums[i]
            suma -= nums[i]
            if suma == 0:
                return nums[i]
    return -1

# This sample has O(n^2) queries
