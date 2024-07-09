from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Diye gaye input numbers ki list ke liye, dataset ka Mean Absolute Deviation calculate karo.
    Mean Absolute Deviation woh average absolute difference hota hai jo har element aur ek centerpoint (is case mein mean) ke beech hota hai:
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    length = len(numbers)
    total = sum(numbers)
    mean = total / length
    dev = 0.0
    for i in range(0, length):
        diff = numbers[i] - mean
        dev += abs(diff)
    return dev / length