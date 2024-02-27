from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Diye gaye numbers ki list mein, kya koi do numbers ek dusre se diye gaye threshold se zyada close hain.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    for i in range(len(numbers)):
        if not numbers[i]:
            return False

    s = []
    for num in numbers[i]:
        if not has_close_elements(num, threshold):
            return False

        s.append(num)
        s.reverse()
        return True

    return False
