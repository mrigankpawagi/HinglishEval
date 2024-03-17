from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """
    Diye gaye integers ki list mei se, sequence me diye gaye har moment tak paye gaye rolling maximum element ki list generate karo.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_list = []
    for i in range(len(numbers)):
        max_list.append(max(numbers[: i + 1]))
    return max_list


def rolling_min(numbers: List[int]) -> List[int]:
    """
    Diye gaye integers ki list mei se, sequence me diye gaye har moment tak paye gaye rolling minimum element ki list generate karo.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    """
    min_list = []
    for i in range(len(numbers)):
        min_list.append(min(numbers[: i + 1]))
    return min_list


def rolling_sum(numbers: List[int]) -> List[int]:
    """
    Diye gaye integers ki list mei se, sequence me diye gaye har moment tak paye gaye rolling sum ki list generate karo.
    >>> rolling_sum([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 6, 8, 11, 15, 17]
    """
    sum_list = []
    for i in range(len(numbers)):
        sum_list.append(sum(numbers[: i + 1]))
    return sum_list


def rolling_average(numbers: List[int]) -> List[float]:
    """
    Diye gaye integers ki list mei se, sequence me diye gaye har moment tak paye gaye rolling average ki list generate karo.
    >>> rolling_average([1, 2, 3, 2, 3, 4, 2])
    [1.0, 1.5, 2.0, 2.25, 2.5, 2.8333333333333335, 3.0]
    """
    average_list = []
    for i in range(len(numbers)):
        average_list.append(sum(numbers[: i + 1]) / (i + 1))
