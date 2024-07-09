from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    r"""
    For each element in the input, remove it without changing any elements occurring twice.
    For instance,
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1]
    >>> remove_duplicates([1, 2, 3, 2])
    [1, 2, 2, 2, 2]
    """
    for i, element in enumerate(numbers):
        if len(element) == 2 and not (2 == element[0] and 2 == element[1]):
            if element[0] == i:
                values = values.pop(0).values
        elif len(element[0]) > len(values):
            values = [values[0]]
    values.sort()
    values = values[::-1]
    for i, (value, other) in enumerate(values):
        if value!= i and (value in other or value == i):
            values[i] = value
    values = values[::-1]
    return sorted(values, key=key)


