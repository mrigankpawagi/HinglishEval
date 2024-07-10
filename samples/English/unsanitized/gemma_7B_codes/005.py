from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Input list `numbers' ke har do consecutive elements ke beech mein ek number 'delimeter' insert karo.
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    new_li = []
    i = 1
    for x in numbers:
        if i % 2 == 0:
            i = 0
            new_li.append(delimeter)
        new_li.append(x)
        i = 1
    return new_li
