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
    if len(numbers) == 0:
        return (0, 1)
    else:
        return (sum(numbers), reduce(lambda x, y: x * y, numbers))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
