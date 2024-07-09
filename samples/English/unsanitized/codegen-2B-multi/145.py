
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
    if 1 in nums:
        return nums
    else:
        return sorted(nums, key=lambda x: x // 10 ^ (10 ** (x % 10)))


# -----
# PROBLEMS
# -----

# The list [1, 4, 5, 99, 4, 1, 4, 4, 8, 1, 5, 1] is not always sorted.
# Write a program to sort the list!


""" 
This is based on:
https://stackoverflow.com/questions/15772902/recursive-merge-sort-in-python
"""


