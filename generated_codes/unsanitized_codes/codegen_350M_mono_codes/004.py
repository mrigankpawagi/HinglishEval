from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Diye gaye input numbers ki list ke liye, dataset ka Mean Absolute Deviation calculate karo.
    Mean Absolute Deviation woh average absolute difference hota hai jo har element aur ek centerpoint (is case mein mean) ke beech hota hai:
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    x_mean = sum(numbers) / len(numbers)

    m_d = sum([(x - x_mean) ** 2 for x in numbers]) / len(numbers)
    m_dev = abs(m_d)

    return round(m_dev, 2)


