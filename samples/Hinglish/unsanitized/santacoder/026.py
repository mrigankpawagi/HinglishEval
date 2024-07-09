from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Ek integers ki list se, saare elements hata do jo ek se zyada baar occur karte hain.
    Bache hue elements ka order input ke jaisa hi rakho.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create mapping baby dictionary.
    seen = set()
    seen_add = seen.add
    return [x for x in numbers if not (x in seen or seen_add(x))]

