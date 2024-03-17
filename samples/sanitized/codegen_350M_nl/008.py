from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Diye gaye integer list ke liye, ek tuple return karo jismei list ke saare integers ka sum aur product ho.
    Empty list ke sum ko 0 aur product ko 1 ke barabar hona chahiye.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """

    sum_plus_one = sums[:]
    sum_plus_one[0] = nums.sum(1) + sums[0]
    sum_plus_one[1] = sum_plus_one[0]
    sum_plus_one[2] = nums.sum(1) + sums[1]
    sum_plus_one[3] = sum_plus_one[2]
    sum_plus_one[4] = nums.sum(1) + sums[2]
    # sum_plus_one[-1] = sum_plus_one[0] = sum_plus_one[3]
    sum_plus_one[-1] = sum_plus_one[-1]

    sum_plus_one_to_one = sums[:]
    sum_plus_one_to_one[0] = sums[0]
    sum_plus_one_to_one[1] = sum_plus_one[0]
    sum_plus_one_to_one[2] = sums[1]
    sum_plus_one_to_one[3] = sums[2]
    sum_plus_one_to_one[4] = sum_plus_one[3]
    return sum_plus_one_to_one

