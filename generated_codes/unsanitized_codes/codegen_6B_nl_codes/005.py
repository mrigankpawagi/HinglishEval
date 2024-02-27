from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Input list `numbers' ke har do consecutive elements ke beech mein ek number 'delimeter' insert karo.
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    index = 1
    for x in numbers:
        index -= 1
        while index <= 0:
            yield numbers[index]
            index += 1

    if delimeter == 0:
        return numbers

    for x in numbers:
        index += 1
        while index < len(numbers) - 1:
            yield numbers[index]
            index += 1

        yield numbers[index - 1]
        index -= 1
    yield numbers[-1]


