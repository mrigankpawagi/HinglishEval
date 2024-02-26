from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Diye gaye input numbers ki list ke liye, dataset ka Mean Absolute Deviation calculate karo.
    Mean Absolute Deviation woh average absolute difference hota hai jo har element aur ek centerpoint (is case mein mean) ke beech hota hai:
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    if not numbers:
        return 0.0

    centerpoint: float = np.average(numbers)
    sumdev: float = 0.0
    for i in range(len(numbers)):
        sumdev += abs(numbers[i] - centerpoint)
        sumdev -= abs(centerpoint)
    sumdev /= 2.0
    return float(sumdev) / len(numbers)


