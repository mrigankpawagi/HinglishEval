from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Diye gaye numbers ki list (kam se kam do elements ki) par ek linear transform apply karo,
    aisa ki sabse chota number 0 ban jaye aur sabse bada number 1 ban jaye
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    for i in range(len(numbers) - 1):
        numbers[i] = numbers[i] / float(numbers[i] - numbers[i + 1])
    return numbers