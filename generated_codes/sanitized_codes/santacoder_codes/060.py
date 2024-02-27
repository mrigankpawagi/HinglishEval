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

    # Sum 1 to n karta ho ahi adalah ako tugas ini.
    sum1to = 1

    # Sum of last 3 n kartah ho ahi adalah ako tugas ini.
    sumLastThree = 0

    for i in range(0, n):
        sum1to = sum1to + sum(range(0, n - i))
        sumLastThree = sumLastThree + 10**i * sum(range(i, n))

    # Sum 1 to n karta ho ahi udah adalah ako tugas ini.
    sumN = sum(range(0, n))

    return (sum1to / sumN) * sumLastThree
