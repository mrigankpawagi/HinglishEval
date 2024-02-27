from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    Diye gaye numbers ki list se (jo ki kam se kam do numbers ki honi chahiye) do aise numbers chun ke return karo jo ek dusre ke sabse kareeb ho aur unhe order mein return karo (chota number, bada number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers = [float(_) for _ in numbers if _.is_number()]
    closest_elements = []
    for i in range(len(numbers)):
        closest_element = None
        if math.isnan(numbers[i]) or math.isnan(numbers[i]):
            nearest_element = None
            break
        if numbers[i].abs() <= 1.0:
            continue
        distance_from_nearest_element = math.abs(math.fabs(numbers[i]) - numbers[i].abs())
        if distance_from_nearest_element <= len(closest_elements):
            closest_element = closest_elements[distance_from_nearest_element - 1]
        else:
            closest_element = closest_elements[0]
        if closest_element is None:
            closest_element = closest_elements[len(closest_elements)