from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_num = numbers[0]
    size = len(numbers)
    scale_factor = 1 / (max(numbers) - min_num)
    result = [scale_factor * numbers[i] - min_num for i in range(size)]
    return result


def find_biggest(numbers: List[float]) -> List[float]:
    """ Return the largest in a list of numbers
    >>> find_biggest([4, 5, 6])
    6
    >>> find_biggest([4, 6, 5])
    6
    >>> find_biggest([1, 2, 3, 4])
    4
    >>> find_biggest([4, 1.22, 3])
    4.0
    """
    result = numbers[0]
    for i in numbers:
        if i > result:
            result = i
    return result

def add_numbers(a: List[float], b: List[float], c: List[float]) -> List[float]:
    result = []
    res_sum = 0.0
    for i in range(len(a)):
        res_sum += a[i]
    for i in range(len(a)):
        res_sum += b[i]
    return [a[i]+b[i]+c[i]+res_sum for i in range(len(a))]
