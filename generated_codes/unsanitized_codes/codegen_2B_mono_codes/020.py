from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Diye gaye numbers ki list se (jo ki kam se kam do numbers ki honi chahiye) do aise numbers chun ke return karo jo ek dusre ke sabse kareeb ho aur unhe order mein return karo (chota number, bada number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    n_len = len(numbers)
    left = 0
    right = n_len - 1
    while left < right:
        mid = (left + right) // 2
        if numbers[mid] > numbers[right]:
            left = mid + 1
        elif numbers[mid] < numbers[right]:
            right = mid
    return right, numbers[right]


