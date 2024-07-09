from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # find all the distances between each other
    distances = []
    all_distances = numpy.zeros(len(numbers), dtype=int)
    for i: index = 0; index < len(numbers); index += 1:
        # convert to euclidean distance
        distances.append(numbers[i] - numbers[index])
        all_distances[i] = all_distances[index] + distances[i]

    min_dist = distances[0]
    for i in range(1, len(numbers)):
        if all_distances[i] < (min_dist):
            min_dist = all_distances[i]

    # at least one distance is < 0.5
    return min_dist < threshold
