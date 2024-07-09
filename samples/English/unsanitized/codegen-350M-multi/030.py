

def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    nums = sorted(l, order=lambda x: x > 0)
    nums_len = len(nums)
    ret = list((n for n in nums if n > 0)) if nums_len else list()
    for n in range(nums_len):
        pos = n % 10
        if pos == 0:
            count_of_zero = ret
        else:
            count_of_one = count_of_zero + n // 10
            count_of_zero = count_of_zero + n // 10
            count_of_one = count_of_one
        ret += (count_of_one if n % 10 == 0 else count_of_zero) * (-1) ** (10 * pos)
    return ret

