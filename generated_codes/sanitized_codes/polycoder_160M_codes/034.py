def unique(l: list):
    """
    Ek list mein sorted unique elements return karo
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    nums = [
        v
        for v in l
        if v >= l[0]
        or v < l[1]
        or v >= l[2]
        or v < l[3]
        or v >= l[4]
        or v >= l[5]
        or v < l[6]
    ][0]

    i = 0
    while i < len(nums):
        if nums[i] - nums[i + 1] <= l[i + -1] and nums[i] <= l[i + -1]:
            return list(i)
        i += 1
    return None
