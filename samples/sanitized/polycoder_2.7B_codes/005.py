from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Input list `numbers' ke har do consecutive elements ke beech mein ek number 'delimeter' insert karo.
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    #    # Find the starting indices that have consecutive values at delimeter
    #    # and the index of largest consecutive index
    #    # If the value at delimeter and number 'number' are consecutive,
    #    # remove them until they are at a lower number.
    #    #     [3, 2, 1, 3], 4)
