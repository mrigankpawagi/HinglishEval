from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_start = float('-inf')
    closest_end = float('-inf')

    for number in numbers:
        # If a number is the smallest, we need not find the previous value
        if distance(closest_start, number) < closest_start:
            closest_start = distance(closest_start, number)

        # Find the closest number
        if distance(closest_end, number) < closest_end:
            closest_end = distance(closest_end, number)

    return closest_end - closest_start, closest_end - closest_start


