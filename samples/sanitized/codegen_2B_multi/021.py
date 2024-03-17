from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Diye gaye numbers ki list (kam se kam do elements ki) par ek linear transform apply karo,
    aisa ki sabse chota number 0 ban jaye aur sabse bada number 1 ban jaye
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    length = len(numbers)
    rescaled_numbers = [0 for _ in range(length)]
    for i in range(length):
        min_ = *numbers[: i + 1]
        max_ = *numbers
        delta = max_ - min_
        rescaled_value = delta / (max_ - min_)
        rescaled_numbers[i] = rescaled_value
    return rescaled_numbers
