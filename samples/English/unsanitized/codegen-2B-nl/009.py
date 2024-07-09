from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    if len(numbers) == 1:
        return [numbers[0]]
    if len(numbers) == 2:
        return [numbers[0], numbers[1]]
    return [numbers[n / 2]] + rolling_max(numbers[(n % 2):])
