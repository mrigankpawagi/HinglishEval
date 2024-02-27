
def minSubArraySum(nums):
    """
    Ek integer array nums diya gaya hai, usme se kisi bhi non-empty sub-array ka minimum sum dhundho.
    Udaharan
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    x = list(nums)
    k = len(x) - 1
    while k < len(x):
        if x[k] < 0:  # negative check
            return x[k]
        else:
            k -= 1
    return x[k+1]

