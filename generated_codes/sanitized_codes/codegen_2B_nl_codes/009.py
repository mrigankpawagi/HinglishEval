from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """
    Diye gaye integers ki list mei se, sequence me diye gaye har moment tak paye gaye rolling maximum element ki list generate karo.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    x = [0]
    max_index = number_list_index
    for i in range(len(numbers) - 1, 0, -1):
        for j in range(max_index, 0, -1):
            x[j] = numbers[j - max_index][-i]
            max_index -= 1
        if max_index != 0:
            x[max_index] = numbers[-i][-j]
    return [min(int(x[0]), int(max(x))) for i, x in enumerate(x)]