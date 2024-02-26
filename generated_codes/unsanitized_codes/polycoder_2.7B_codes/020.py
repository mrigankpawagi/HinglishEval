from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Diye gaye numbers ki list se (jo ki kam se kam do numbers ki honi chahiye) do aise numbers chun ke return karo jo ek dusre ke sabse kareeb ho aur unhe order mein return karo (chota number, bada number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    first = float('-inf')
    second = 0.0
    for number in numbers:
        closest, distance = math.sqrt(
            (number - first) ** 2 + (number - second) ** 2
        )  # sqrt(number * (number-first) * (number-second)) - distance
        if closest < 0:
            first = number
        if distance >= closest:
            second = number
    return first, distance
