from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Diye gaye numbers ki list se (jo ki kam se kam do numbers ki honi chahiye) do aise numbers chun ke return karo jo ek dusre ke sabse kareeb ho aur unhe order mein return karo (chota number, bada number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if numbers == []:
        return (0.0, 0.0)

    closest, distance = None, None

    for i in range(len(numbers)):
        if numbers[i] > closest or numbers[i] < closest:
            closest = numbers[i]
            for j in range(i + 1, len(numbers)):
                if numbers[j] < closest:
                    continue
                distance[j - i] = numbers[j] - closest

    return (closest, distance)


