from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # NOTE: We can do this using a better way since the largest number does not depend on the smallest
    # and thus we'll never be performing the transformations in the same row; the smallest number
    # stays as it is.

    minv = min(numbers)

    if minv < 1.0e-9:
        print(minv)
    else:
        print(1.0 / minv)
        scaled = []
        index = 0
        for num in numbers:
            curv = pow(num, -1)
            if curv < 1.0e-9:
                scaled.append(curv)
                index += 1
            else:
                scaled.append((1.0 / curv) * num)
        scaled = scaled[:index]
        print(scale_to_unit(scaled))


