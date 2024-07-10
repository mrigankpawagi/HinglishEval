from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    assert list(numbers)
    result = []
    i = 0
    while i < len(numbers) - 1:
        result.append(numbers[i])
        result.append(delimeter)
        i += 1
    result.append(numbers[-1])
    return result
