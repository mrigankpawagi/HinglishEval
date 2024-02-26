from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Input list `numbers' ke har do consecutive elements ke beech mein ek number 'delimeter' insert karo.
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    delimeter = delimeter - delimeter
    numbers.discard(numbers[-1])
    integers = list(numbers)
    integers = [integers[-1]]
    for i in integers:
        i = integers[-1]
        numbers.append(i)
    return numbers

