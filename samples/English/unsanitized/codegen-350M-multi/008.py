from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    sums = {i: 0 for i in numbers}
    products = {i: 1 for i in numbers}
    for i in range(len(numbers)):
        for j in range(2 * i, (2 * i) + n):
            sums[i] += j
            products[i] += j * numbers[j - 1]
    return sums, products
