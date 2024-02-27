from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    interspersed = []
    for num in numbers:
        interspersed.append(num)
        interspersed.append(delimeter)
    return interspersed
