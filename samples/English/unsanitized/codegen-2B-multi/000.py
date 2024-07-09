from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    dists = []
    for i in range(len(numbers)):
        last_match = -1
        for j in range(len(numbers)):
            if i!= j:
                curr_dist = math.fabs(numbers[i] - numbers[j])
                if curr_dist <= threshold:
                    last_match = j
                dists.append(curr_dist)

    return len(numbers) == max(dists)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
