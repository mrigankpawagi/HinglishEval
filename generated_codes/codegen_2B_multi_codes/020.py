from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    assert len(numbers) >= 2
    last_two = None
    for n in numbers[1:]:
        if last_two is None:
            last_two = [n, n]
            continue
        last_two[0] = min(last_two[0], n)
        last_two[1] = max(last_two[1], n)

        # Check for duplicates
        if not last_two:
            # No duplicates found...
            return last_two

        # Duplicate found - find average
        last_two[0] = (sum(last_two[0:2]) + last_two[0]) / 2.
        last_two[1] = (sum(last_two[2:4]) + last_two[1]) / 2.
    return last_two



