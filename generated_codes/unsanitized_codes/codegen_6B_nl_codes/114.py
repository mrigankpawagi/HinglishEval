
def minSubArraySum(nums):
    """
    Ek integer array nums diya gaya hai, usme se kisi bhi non-empty sub-array ka minimum sum dhundho.
    Udaharan
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    def getMSSum(p, l, nums: Tuple[int]):
        if l == 0 or nums[0] == 0:
            return 0
        elif l == 1:
            return pow(nums[0] + 1, p)
        else:
            return getMSSum(p, l - 1, reduce(lambda sum, i: pow(sum, p) + nums[i] + 1, range(l), nums) + nums[l - 1])
    def getMSB(nums: Tuple[int]):
        if nums:
            m = len(nums) - 1
            return getMSB(nums[:m] + [nums[-1] / 1], m)
        else:
            return 0
    return getMSB[1 << nums.index('1')] + reduce(lambda sum, i: sum + i, reversed(nums), 0) + getMSB[1 << nums.index('-1')]

A:

In short:
