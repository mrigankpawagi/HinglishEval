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
    mean = (sum(numbers) / len(numbers)) / len(numbers)
    mads = (sum(numbers) - mean) / len(numbers)
    mean_abs = [abs(nums - mean) for nums in numbers]
    # The standard deviation of means is a good estimate of MAD.
    std_dev = std(mean_abs)
    mean_abs = mean_abs[num_numbers]
    mads = mads[:num_numbers]
    mads = mads[num_numbers - len(mean_abs):]
    return std_dev + mads


# Returns mean and std deviation of the inputs in a single call to func.
