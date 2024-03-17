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
    sum_product: List[int] = []
    for num in numbers:
        sum_product.append(num)
    if not sum_product:
        return (0, 0)
    else:
        return (sum_product.pop() * -1, sum_product.pop())
