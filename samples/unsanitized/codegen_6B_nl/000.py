from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Diye gaye numbers ki list mein, kya koi do numbers ek dusre se diye gaye threshold se zyada close hain.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if len(numbers) < 2:
        return False
    min_element, max_element = numbers[0], numbers[-1]
    if max_element - min_element < threshold:
        return False
    elif (max_element < threshold) or (min_element > threshold + 0.2):
        return False
    else:
        return True


