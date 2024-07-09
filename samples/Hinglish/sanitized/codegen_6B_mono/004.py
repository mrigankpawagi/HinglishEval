from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Diye gaye input numbers ki list ke liye, dataset ka Mean Absolute Deviation calculate karo.
    Mean Absolute Deviation woh average absolute difference hota hai jo har element aur ek centerpoint (is case mein mean) ke beech hota hai:
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    n = len(numbers)
    temp_sum = 0
    for num in numbers:
        temp_sum += abs(num - sum(numbers) / n)
    return temp_sum / n