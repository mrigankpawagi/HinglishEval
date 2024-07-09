from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """
    Diye gaye integers ki list mei se, sequence me diye gaye har moment tak paye gaye rolling maximum element ki list generate karo.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max = [[None] * len(numbers) for _ in range(len(numbers))]
    for i in range(0, len(numbers) - 1):
        for _ in range(numbers[i + 1]):
            rolling_max[_][i] = rolling_max[_][i + 1] = numbers[i]
    return rolling_max

