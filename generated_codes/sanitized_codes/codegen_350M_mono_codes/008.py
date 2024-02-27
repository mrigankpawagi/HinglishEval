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
    product_or_suma = 1
    sumofint = 0
    for number in numbers:
        product_or_suma *= number
    sumofint = product_or_suma
    for number in numbers:
        sumofint -= product_or_suma * number
    return sum_product_of_two_numbers(numbers, sum, product_or_suma, product_or_suma)