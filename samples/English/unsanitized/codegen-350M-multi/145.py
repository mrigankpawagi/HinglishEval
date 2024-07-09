
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
    nums_l = []
    sums = [digits[0] for digits in sorted(nums)]
    for i in range(len(sums) - 1):
        nums_l.append(sums[i])
        sums[i] = '%d' % (nums[i] * 10)
    sums[-1] = '-%d' % (nums[-1] * 10)
    nums = nums_l + [sums[0]]
    return nums[::-1]  # order by descending


