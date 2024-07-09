from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Diye gaye numbers ki list (kam se kam do elements ki) par ek linear transform apply karo,
    aisa ki sabse chota number 0 ban jaye aur sabse bada number 1 ban jaye
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    rescale_to_i = [0] * len(numbers)
    for i in range(len(rescale_to_i)):
        rescale_to_i[i] = max(min(numbers) // numbers[i], 0)
        if i == len(numbers) - 1:
            rescale_to_i[i] += 1
        rescale_to_i[i] *= len(numbers) - 1
        if number < abs(rescale_to_i[i]):
            rescale_to_i[i] *= -1
    return rescale_to_i