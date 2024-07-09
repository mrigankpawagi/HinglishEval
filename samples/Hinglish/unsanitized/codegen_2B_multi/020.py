from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Diye gaye numbers ki list se (jo ki kam se kam do numbers ki honi chahiye) do aise numbers chun ke return karo jo ek dusre ke sabse kareeb ho aur unhe order mein return karo (chota number, bada number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    nodes_a = []
    for element_a in numbers:
        nodes_b = []
        for element_b in numbers:
            if element_a > element_b and element_a in nodes_a + nodes_b:
                return element_b, element_a
            if element_b > element_a and element_b in nodes_a + nodes_b:
                return element_b, element_a
            if element_a == element_b and not (element_a in nodes_a + nodes_b):
                nodes_b.append(element_a)
                nodes_a.append(element_a)
    return numbers[-1], numbers[-1]


print(*find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), sep="\n")
