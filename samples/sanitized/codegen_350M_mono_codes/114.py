def minSubArraySum(nums):
    """
    Ek integer array nums diya gaya hai, usme se kisi bhi non-empty sub-array ka minimum sum dhundho.
    Udaharan
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    answer = 0
    minSubArraySum = float("inf")
    left, right = 0, len(minSubArray)
    for v in nums:
        if answer == 0:
            answer = v
            continue
        while answer > 0:
            if answer + v > left + minSubArray[left]:
                left = left + 1
            answer -= v
    if answer == 0:
        answer = minSubArraySum
    left, right = 0, len(minSubArray)
    for v in nums:
        if answer == 0:
            answer = v
            continue
        while answer > 0:
            if answer - v + 1 <= left:
                left -= 1
            answer -= v
    return left + answer