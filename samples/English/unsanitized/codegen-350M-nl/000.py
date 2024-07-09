from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if len(numbers)!= n:
        return False

    elements = numbers.tuple()  # Copy the same list of elements

    # Check if the elements are all either exactly the same length or the same length
    # only if the two elements are not the same length.
    if len(elements)!= len(numbers):
        return True

    for i in numbers:
        if i == elements[i] == elements[i]:
            continue

        check = 0.0
        for v2 in elements[i][::2]:
            check += float(v2.r) - 1
        check += float(numbers[i][0]) - 1

        if check % len(numbers)!= 0:
            break
    return check == 0


