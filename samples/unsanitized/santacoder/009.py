from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """
    Diye gaye integers ki list mei se, sequence me diye gaye har moment tak paye gaye rolling maximum element ki list generate karo.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    temp_max: Tuple[int,...] = tuple(max(x) for x in zip(*numbers))
    res: List[int] = [max(temp_max)]
    for i in range(len(numbers)):
        res.append(max(res[-1], numbers[i]))
    return res

