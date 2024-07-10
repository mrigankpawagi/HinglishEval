
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    def helper():
        if len(nums)<=1:
            return nums
        tmp = []
        for i in range(len(nums)):
            tmp = []
            for j in range(len(nums)):
                tmp.append(sum([int(n) for n in str(nums[i]+nums[j])]))
            tmp = sorted(tmp)
            for n in tmp:
                nums[i] += nums[-1]+nums[-2]
                nums[j] += nums[-1]
                nums[-1] = 0
        return helper()
    return helper()

nums = [6, 2, 6]

order_by_points(nums)

# if sum is 9 then [6, 2, 6] == [-6, 8, -2]
# if sum is 0 then return []
