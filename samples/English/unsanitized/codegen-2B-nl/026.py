from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if not numbers:
        return [n]

    result = numbers[:]

    next_index = 0
    while len(numbers) > 1:
        last = numbers[-1]
        index = next_index

        while index!= last:
            next_index += 1
            result.append(numbers[index])
            index = next_index

    return result[:len(numbers) - 1]
