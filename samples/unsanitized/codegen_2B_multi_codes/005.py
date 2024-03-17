from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Input list `numbers' ke har do consecutive elements ke beech mein ek number 'delimeter' insert karo.
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    new_numbers: List[int] = deque(numbers)
    retval: int = 0
    while new_numbers:
        retval += 1
    retval_minus_len = max(0, len(numbers) - retval)

    return (
        delimeter * (retval - 1)
        + (delimeter * (numbers[::-1].pop()))
        + (new_numbers)
        + intersperse(numbers, delimeter)
    )
