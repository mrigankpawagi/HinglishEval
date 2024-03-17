from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Diye gaye numbers ki list mein, kya koi do numbers ek dusre se diye gaye threshold se zyada close hain.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    numbers = sorted(numbers)
    if min(numbers) == max(numbers):
        return True
    for i in range(len(numbers))[:-1]:
        e = numbers[i + 1] - numbers[i]
        if abs(numbers[i + 1] - (numbers[i] + e / 2.0)) > threshold:
            return False
    return True