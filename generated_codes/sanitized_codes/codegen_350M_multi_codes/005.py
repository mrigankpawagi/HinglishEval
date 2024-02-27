from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Input list `numbers' ke har do consecutive elements ke beech mein ek number 'delimeter' insert karo.
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if any(numbers[0] <= numbers[-1] for _ in range(0, len(numbers))):
        # Numeris van karobou.
        new_numbers = []
        nums = list(numbers)
        c = 0
        new_numbers.append(nums[c])
        while c + 1 < len(numbers):
            # Voorgeef c = c + 1
            new_numbers.append(nums[c])
            c += 1
        new_numbers.append(nums[-1])
        # Beeee!
        return new_numbers
    else:
        # Numeris van tussen
        new_numbers = []
        c = 0
        for elem in list(numbers):
            new_numbers.append(elems[c])
            c += 1
        # Beeee!
        return new_numbers

