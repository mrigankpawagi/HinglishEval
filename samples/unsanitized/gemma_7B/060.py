

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
    return n * (n + 1) // 2


def sum_to_n_recursive(n: int):
    """
    sum_to_n_recursive ek function hai jo 1 se lekar n tak ke numbers ka sum karta hai.
    >>> sum_to_n_recursive(30)
    465
    >>> sum_to_n_recursive(100)
    5050
    >>> sum_to_n_recursive(5)
    15
    >>> sum_to_n_recursive(10)
    55
    >>> sum_to_n_recursive(1)
    1
    """
    if n == 1:
        return 1
    return n + sum_to_n_recursive(n - 1)


def sum_to_n_iterative(n: int):
    """
    sum_to_n_iterative ek function hai jo 1 se lekar n tak ke numbers ka sum karta hai.
    >>> sum_to_n_iterative(30)
    465
    >>> sum_to_n_iterative(100)
    5050
    >>> sum_to_n_iterative(5)
    15
    >>> sum_to_n_iterative(10)
    55
    >>> sum_to_n_iterative(1)
    1
    """
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


def sum_to_n_iterative_2(n: int):
    """
    sum_to_n_iterative_2 ek function hai jo 1 se lekar n tak ke numbers ka sum karta hai.
    >>> sum_to_n_iterative_2(30)
    465
    >>> sum_to_n_iterative_2(100)
    5050
    >>> sum_to_n_iterative_2(5)
    15
    >>> sum_to_n_iterative_2(10)
    55
    >>> sum_to_n_iterative_2(1)
    1
    