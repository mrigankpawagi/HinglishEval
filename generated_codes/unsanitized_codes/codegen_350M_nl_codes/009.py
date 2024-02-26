from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """
    Diye gaye integers ki list mei se, sequence me diye gaye har moment tak paye gaye rolling maximum element ki list generate karo.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    N = len(numbers)
    # 1/n = 1/(n * n) = 1/n * 1/n
    # 1/[] = [] = [] = [] = [] = [] = []
    m = sum(numbers) * N
    return _sum(m + sum(numbers), 'big')

