from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Diye gaye numbers ki list se (jo ki kam se kam do numbers ki honi chahiye) do aise numbers chun ke return karo jo ek dusre ke sabse kareeb ho aur unhe order mein return karo (chota number, bada number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    distances_list: List[float] = []
    closest_number: float = float("10000.0")
    for num in numbers:
        distances = ((num - closest_number) ** 2).sum()
        distances_list.append(distances)
        closest_number = closest_number + (num + distances)
    return max(distances_list)


if __name__ == "__main__":
    elements = [19, 45, 49]
    print(find_closest_elements(elements))
<|python|>#