from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    #  Evaluate as if all input values are zeros except for the zero mean
    assert len(numbers) > 0, "No numbers passed to mean_absolute_deviation"
    numbers = list(numbers)    # make a copy of the given numbers list
    if numbers[0] == 0:
        numbers.pop(0) # remove first number in the list
        numbers.pop(0) # remove first number in the list

    numbers_mean = sum(numbers) / len(numbers) # calculate mean
    x_mean = round(numbers_mean, 3) # round to 3 decimals: round mean to 3 digits
    # return mean absolute deviation minus mean absolute deviation
    return round(abs(numbers[0] - x_mean), 3)
