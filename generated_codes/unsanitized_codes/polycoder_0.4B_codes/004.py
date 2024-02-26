from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Diye gaye input numbers ki list ke liye, dataset ka Mean Absolute Deviation calculate karo.
    Mean Absolute Deviation woh average absolute difference hota hai jo har element aur ek centerpoint (is case mein mean) ke beech hota hai:
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # https://en.wikipedia.org/wiki/Average_absolute_ deviation_calculation
    return sum([mean_absolute_deviation(n) for n in numbers])

