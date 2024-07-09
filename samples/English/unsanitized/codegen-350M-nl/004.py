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
    mean_diff = 0
    for number in numbers:
        x = mean(number)
        y = number - mean(number)
        n = sum(x ** 2, axis=0) * y
        mean_absolute_diff = mean_absolute_deviation(numbers) / n
        yield(mean_absolute_diff)


@pytest.fixture(scope='module', params=(), before_setup=None)
