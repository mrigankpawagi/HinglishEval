def minSubArraySum(nums):
    """
    Ek integer array nums diya gaya hai, usme se kisi bhi non-empty sub-array ka minimum sum dhundho.
    Udaharan
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sums = 0
    min_sum = float("Inf")
    for i in range(0, len(nums)):
        sums = sums + nums[i]
        if sums < min_sum:
            min_sum = sums
        # If sum is 1, don't check for sum at next index.
        if sums > 1:
            # If 1 is part of the current sum, check if another 1 needs
            # to be added
            sums = sums - nums[i]
            # print(sums)
    if min_sum == float("Inf"):
        return 0
    else:
        return min_sum