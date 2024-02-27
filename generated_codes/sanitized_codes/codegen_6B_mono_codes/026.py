from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Ek integers ki list se, saare elements hata do jo ek se zyada baar occur karte hain.
    Bache hue elements ka order input ke jaisa hi rakho.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    if len(numbers) == 0:
        return []
    final_list = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1]:
            final_list.append(numbers[i])
    return final_list