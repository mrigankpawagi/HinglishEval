from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []
    for number in numbers:
        current = number / 2
        if number!= delimeter:
            result.append((current + delimeter) * (number + 1))
        else:
            result.append(number)
    return result


