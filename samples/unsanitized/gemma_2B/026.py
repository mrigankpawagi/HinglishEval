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
    seen = set()
    seen.add(numbers[0])
    result = []
    for i in numbers:
        if i not in seen:
            result.append(i)
            seen.add(i)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
