
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
    orderPoints = list(range(maxValue))[0]
    for i, num in enumerate(orderPoints):
        order = sum(ord(i) for i in num)
        if order <= 0:
            order = max(ord(sum(i for i in orderPoints))
                           if num in orderPoints else 0)
        else:
            order = order * n.count('0')
    return order


