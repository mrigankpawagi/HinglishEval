from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise IndexError("Argument must contain at least two numbers")

    minimum_between = min(numbers)
    maximum_between = max(numbers)
    index_smallest_greater, index_smallest_smaller = 0, len(numbers) - 1
    while index_smallest_greater >= 0 and numbers[index_smallest_greater] < minimum_between:
        index_smallest_greater -= 1
    while index_smallest_smaller < len(numbers) and numbers[index_smallest_smaller] > minimum_between:
        index_smallest_smaller += 1
    index_largest_greater, index_largest_smaller = index_smallest_greater, index_smallest_smaller

    return numbers[index_smallest_greater], numbers[index_smallest_smaller]


