from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Input list `numbers' ke har do consecutive elements ke beech mein ek number 'delimeter' insert karo.
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    new_numbers: List[int] = []
    i = 0
    while i < len(numbers):
        new_numbers.append(numbers[i] + delimeter)
        i += 1
    return new_numbers


