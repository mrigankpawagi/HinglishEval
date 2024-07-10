from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Ek integers ki list se, saare elements hata do jo ek se zyada baar occur karte hain.
    Bache hue elements ka order input ke jaisa hi rakho.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    # write your code here
    i = 0
    j = 0
    x = []
    y = []
    n = len(numbers)
    while j < n:
        if not (numbers[i] == numbers[j]):
            x.append(numbers[j])
            i += 1
            j += 1
        else:
            j += 1
    y.append(x)
    return y
