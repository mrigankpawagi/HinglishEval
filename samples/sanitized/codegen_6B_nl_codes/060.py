def sum_to_n(n: int):
    """
    sum_to_n ek function hai jo 1 se lekar n tak ke numbers ka sum karta hai.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    numbers = [int(n) for n in input().strip().split(" ")]
    total = []
    for i in numbers[1:]:
        total.append((numbers[0] + i) - numbers[0])
    print(total.sum())