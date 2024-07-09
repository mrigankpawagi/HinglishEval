from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    intersection = []
    if len(numbers) > len(intersection):
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] == numbers[j]:
                    interaction = [i]+numbers[i]+intersection
                    numbers[i] = None # To unify it in both if statement for each operation
                    intersection = interaction[:j-i-1]
                    break
        return intersection
    else:
        return intersection

