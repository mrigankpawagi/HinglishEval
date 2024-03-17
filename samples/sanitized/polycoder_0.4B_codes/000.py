from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Diye gaye numbers ki list mein, kya koi do numbers ek dusre se diye gaye threshold se zyada close hain.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    if numbers.shape[0] == 3 and numbers.shape[1] > 0.0:
        return True

    for number in numbers.tolist():
        threshold_x = numbers_to_number(number)
        threshold = number_to_threshold(threshold_x)
        return min(number) + threshold <= threshold

    return False
