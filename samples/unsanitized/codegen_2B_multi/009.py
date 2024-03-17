from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """
    Diye gaye integers ki list mei se, sequence me diye gaye har moment tak paye gaye rolling maximum element ki list generate karo.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    return_list = []
    for i in range(0, len(numbers)):
        for element in return_list:
            if element <= (numbers[i]) and element >= (numbers[i] - 1):
                i = numbers[i]
                return_list.append(i)
                break
        else:
            return_list.append(numbers[i])

    return return_list
