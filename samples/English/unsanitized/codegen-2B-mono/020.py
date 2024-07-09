from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Your code here

    for i in range(len(numbers)):
        # Find distance between numbers
        distances = abs(numbers[i] - numbers)
        # Find min value of distances
        min_num = sorted(distances)[0]
        # Find indices of distances for both values of min distance
        min_indices = distances.index(min_num)
        # Take the min value and return them 
        return numbers[min_indices]



# def find_closest_elements(numbers: List[float]) -> Tuple[float]:
#     """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
#     other. No duplicates.
#     >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2, 6.5])
#     (2.0, 3.0)
#     >>> find_closest_elements([3.0, 4.0, 2.0, 1.0, 6.5])
#     (6.5, 3.0)
#     """
#     # Your code here

#     for i in range(len(numbers)):
#         # Find distance between numbers
#         distances = abs(numbers[i] - numbers)
#         # Find min value of distances
#         min_num = sorted