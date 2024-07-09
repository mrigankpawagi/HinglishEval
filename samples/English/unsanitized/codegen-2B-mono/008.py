from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    from functools import reduce
    num_sum = sum(numbers)
    num_prod = reduce(lambda x, y: x * y, numbers)
    return num_sum, num_prod


'''
    Sum of squares of numbers
    1^2 + 2^2 + 3^2 +... + n^2
- (n/2) * ((n-1)/2) * (n/2) - 1/2

If a is odd:

a^2 = (a+1)/2
    ** 


If a is even:

a^2 = (a / 2) * (1 + 3 * 4 / 2 )


'''


