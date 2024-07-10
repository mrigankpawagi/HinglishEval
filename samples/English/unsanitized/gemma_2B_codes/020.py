from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    a_index = numbers.index(min(numbers))
    b_index = a_index + 1
    closest = a_index, b_index
    return numbers[closest[0]], numbers[closest[1]]


if __name__ == "__main__":
    with open("p019_numbers.txt", encoding="utf-8") as f:
        numbers = [float(x.strip()) for x in f if x]
    print(find_closest_elements(numbers))
