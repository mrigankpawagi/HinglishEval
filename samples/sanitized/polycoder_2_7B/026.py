from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Ek integers ki list se, saare elements hata do jo ek se zyada baar occur karte hain.
    Bache hue elements ka order input ke jaisa hi rakho.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if not isinstance(numbers, List):
        numbers = [numbers]
    result = []
    numbers.sort()
    for index in range(len(numbers)):
        if numbers[index] == number:
            result.append(numbers[index])
    return result
