from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closet_list = []
    smaller_list = []
    # Sort the list of numbers in ascending order
    numbers.sort()
    # Assert all the numbers are in the list in ascending order
    assert numbers[0] < numbers[-1]
    # Iterate and select the elements of each sorted list and assign the result of that smallest to the closet list and the others to
    # the larger lists
    for e in numbers:
        closet = e

        if closet < closet:
            smaller_list.append(closet)

        else:
            closet_list.append(closet)
            larger_list = list(smaller_list[-1:])
    return closet_list, larger_list


# def find_closest_elements_(numbers: List[float]) -> List[float]:
#     """ From a list of numbers (of length at least two) select and return two that are the closest to each other and return them in
#     order (smaller number, larger number).
#     >>> find_closest_elements([100, 200, 300, 100, 200, 300])
#     [300, 200, 100]
#     >>> find_closest_elements([100, 600, 0, 700, 100, 600])
#     [600, 700, 100]
#     """
#     closet_list = []
#     smaller_list = []
