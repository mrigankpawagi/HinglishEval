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

    k = len(numbers)

    a = 0
    for i in numbers:
        a += i
        break

    for k in reversed(range(k)):
        if a % k == 0:
            return (a, a / k)
        a = 0
    return (0, 0)
