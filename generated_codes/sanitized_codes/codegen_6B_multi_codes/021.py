from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Diye gaye numbers ki list (kam se kam do elements ki) par ek linear transform apply karo,
    aisa ki sabse chota number 0 ban jaye aur sabse bada number 1 ban jaye
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Rescale all floats, with min and max
    min_num = min(numbers)
    max_num = max(numbers)
    ranges = [max_num - min_num]
    rescaled_numbers = [float(number) * 1 / ranges[0] for number in numbers]
    return rescaled_numbers