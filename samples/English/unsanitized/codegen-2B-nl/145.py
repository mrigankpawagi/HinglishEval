
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
    def is_equal(x, y):
        x = x.to_string()
        y = y.to_string()
        sum = x + y

        try:
            return sum == '0' and x == y
        except (ValueError, TypeError):
            return False

    lst = set(map(int, nums))
    for num in lst:
        lst2 = sorted(lst - [num], key = operator.getitem, reverse=True)
        if num in lst2:
            lst.remove(num)

    return lst
