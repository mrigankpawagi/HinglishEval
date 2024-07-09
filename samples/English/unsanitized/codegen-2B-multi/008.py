from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if not numbers:
        return (0, 1)

    n = len(numbers)
    max_val = numbers[0]
    result = numbers[0]
    for i in range(1, n):
        max_val = max(max_val, numbers[i])
        result = max(result, numbers[i] * (i + 1))
    return (result, len(numbers) * n + result)


if __name__ == "__main__":
    with open("./input.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        numbers = line.strip().split(", ")
        numbers = map(int, numbers)
        print(sum(numbers))
        print(sum_product(numbers))
