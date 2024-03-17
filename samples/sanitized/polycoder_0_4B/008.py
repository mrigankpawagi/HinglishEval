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
    sum_list = [0] * 64

    # make sum with integers
    for i in numbers:
        sum_list[i] += 1
    sum_list[number_to_index(number)] = 1
    sum_list[number_to_index(1)] = 1
    sum_list[number_to_index(2)] = 0
    sum_list[number_to_index(3)] = 0
    sum_list[number_to_index(4)] = 0
    return sum_list
