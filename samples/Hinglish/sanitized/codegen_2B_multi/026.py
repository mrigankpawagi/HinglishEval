from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Ek integers ki list se, saare elements hata do jo ek se zyada baar occur karte hain.
    Bache hue elements ka order input ke jaisa hi rakho.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    sorted_numbers = sorted(numbers, key=lambda x: [str(y) for y in x])
    return [y for y in sorted_numbers if len(y) == len(sorted_numbers[0])]
