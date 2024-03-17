from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Input list `numbers' ke har do consecutive elements ke beech mein ek number 'delimeter' insert karo.
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if len(numbers) == 0:
        return []
    if len(numbers) == 1:
        return numbers
    if len(numbers) == 2:
        return numbers + [delimeter]
    return numbers[:2] + [delimeter] + intersperse(numbers[2:], delimeter)

