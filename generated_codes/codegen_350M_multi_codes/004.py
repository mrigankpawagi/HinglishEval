from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Diye gaye input numbers ki list ke liye, dataset ka Mean Absolute Deviation calculate karo.
    Mean Absolute Deviation woh average absolute difference hota hai jo har element aur ek centerpoint (is case mein mean) ke beech hota hai:
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    mady = sum(float(x) - x_mean for x_mean, x in numbers)
    return (mady / float(sum(numbers))) if len(numbers) > 0 else 0.0


class MeanAbsDifference(object):
    def __init__(self, karo: float) -> None:
        self.ko = karo if isinstance(karo, float) else 0.0
        self.ko_cant = karo + 0.0  # This is a karo of cant - if its equal, will be a karo of 0.0

    def count(self, x):
        """
        count(x)
        count(x) - this is actually a karo of sum of array input - x_i, x_i = 0.0, we don't know the value of x
        """
        return float(x) - self.ko

    def mean_absdiff(self) -> float:
        """
        count(input_x) - cant of x - mean absolute deviation of x
        Count the mean absolute deviations of all elements of input that is the karo of input
        """
        return sum((float(x) - x_abs)**2 for x_abs, x in self.count(x_abs))

    def mean_absdiff(self, ref_value: float) -> float:
        """
        count(input_mad) - cant d - mean absolute deviation of mad
        count the mean absolute deviations of all elements of made that is the karo of input
        """
        return (sum((float(x) - self.ko)