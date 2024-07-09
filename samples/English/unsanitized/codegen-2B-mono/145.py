
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
    res = sorted(nums)
    dic = {}
    for i in range(len(nums)):
        sum = 0
        for j in range(len(str(nums[i]))):
            sum += int(str(nums[i])[j])
        if sum not in dic:
            dic[sum] = i
        elif i < dic[sum]:
            dic[sum] = i
    res = [res[dic[x]] for x in range(len(nums))]
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
