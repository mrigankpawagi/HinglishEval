
def minSubArraySum(nums):
    """
    Ek integer array nums diya gaya hai, usme se kisi bhi non-empty sub-array ka minimum sum dhundho.
    Udaharan
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return min(nums[0], nums[1])
    if n == 3:
        return min(nums[0], nums[1], nums[2])
    if n == 4:
        return min(nums[0], nums[1], nums[2], nums[3])
    if n == 5:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4])
    if n == 6:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5])
    if n == 7:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6])
    if n == 8:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7])
    if n == 9:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7], nums[8])
    if n == 10:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7], nums[8], nums[9])
    if n == 11:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7], nums[8], nums[9], nums[10])
    if n == 12:
        return min(nums[0], nums[1], nums[2], nums[3], nums[4], nums[5], nums[6], nums[7], nums[8], nums[9], nums[10], nums[11])
    if n == 13:
        return min(nums[0], nums