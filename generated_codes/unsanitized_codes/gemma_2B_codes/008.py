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
    if not numbers:
        return 0, 1
    return sum(numbers), product(numbers)


def product(numbers: List[int]) -> int:
    """
    Diye gaye integer list ke liye, ek integer return karo jismei list ke saare integers ka product ho.
    Empty list ke product ko 1 ke barabar hona chahiye.
    >>> product([])
    1
    >>> product([1, 2, 3, 4])
    24
    """
    if not numbers:
        return 1
    return product(numbers[1:]) * numbers[0]


def sum_product_2(numbers: List[int]) -> Tuple[int, int]:
    """
    Diye gaye integer list ke liye, ek tuple return karo jismei list ke saare integers ka sum aur product ho.
    Empty list ke sum ko 0 aur product ko 1 ke barabar hona chahiye.
    >>> sum_product_2([])
    (0, 1)
    >>> sum_product_2([1, 2, 3, 4])
    (10, 24)
    """
    if not numbers:
        return 0, 1
    return sum(numbers), product(numbers)


def product_2(numbers: List[int]) -> int:
    """
    Diye gaye integer list ke liye, ek integer return karo jismei list ke saare integers ka product ho.
    Empty list ke product ko 1 ke barabar hona chahiye.
    >>> product_2([])
    1
    >>> product_2([1, 2, 3, 4])
    24
    """
    if not numbers:
        return 1
    return product(numbers[1:]) * numbers[0]
