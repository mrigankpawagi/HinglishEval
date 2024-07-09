from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    rescale_min = numbers[0]
    rescale_max = numbers[0]

    for n in numbers:
        if n < rescale_min:
            rescale_min = n
        if n > rescale_max:
            rescale_max = n

    for i in range(len(numbers)-1):
        numbers[i+1] -= rescale_min
        numbers[i+1] /= (rescale_max - rescale_min + 1e-32)

    return numbers


