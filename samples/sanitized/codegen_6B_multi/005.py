from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Input list `numbers' ke har do consecutive elements ke beech mein ek number 'delimeter' insert karo.
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    previous = None
    ret = []
    for n, next_num in zip(numbers, numbers[1:] + [None]):
        if previous:
            ret.append(previous + [n, next_num])
        else:
            ret.append([n])
        previous = next_num
    return ret