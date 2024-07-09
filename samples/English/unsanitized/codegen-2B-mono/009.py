from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_seq = [numbers[len(numbers) - 1]] * len(numbers)
    for index in range(len(numbers) - 1, -1, -1):
        if numbers[index] > rolling_max_seq[index]:
            rolling_max_seq[index] = numbers[index]
    return rolling_max_seq


