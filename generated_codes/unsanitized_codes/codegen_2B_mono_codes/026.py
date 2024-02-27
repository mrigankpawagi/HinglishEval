from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Ek integers ki list se, saare elements hata do jo ek se zyada baar occur karte hain.
    Bache hue elements ka order input ke jaisa hi rakho.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    numbers = list(dict.fromkeys(numbers))
    numbers.sort()
    return numbers

arr =  [1, 3, 4, 5, 1, 3, 4, 5, 7, 12, 4, 10, 0, 5, 3, 8, 3, 1, 12, 5, 1, 3, 4, 5, 1, 3]
print(f'removed: {remove_duplicates(arr)}')

#===============================================================================
