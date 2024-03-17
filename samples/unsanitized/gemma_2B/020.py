from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Diye gaye numbers ki list se (jo ki kam se kam do numbers ki honi chahiye) do aise numbers chun ke return karo jo ek dusre ke sabse kareeb ho aur unhe order mein return karo (chota number, bada number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        return numbers[0], numbers[1]
    numbers.sort()
    return numbers[0], numbers[-1]


def find_closest_elements_2(numbers: List[float]) -> Tuple[float, float]:
    """
    Diye gaye numbers ki list se (jo ki kam se kam do numbers ki honi chahiye) do aise numbers chun ke return karo jo ek dusre ke sabse kareeb ho aur unhe order mein return karo (chota number, bada number).
    >>> find_closest_elements_2([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements_2([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        return numbers[0], numbers[1]
    numbers.sort()
    return numbers[0], numbers[-1]


def find_closest_elements_3(numbers: List[float]) -> Tuple[float, float]:
    """
    Diye gaye numbers ki list se (jo ki kam se kam do numbers ki honi chahiye) do aise numbers chun ke return karo jo ek dusre ke sabse kareeb ho aur unhe order mein return karo (chota number, bada number).
    >>> find_closest_elements_3([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements_3([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        return numbers[0], numbers[1]
    numbers.sort()
    return numbers[0], numbers[-1]


def find_closest_elements_4(numbers: List