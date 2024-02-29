

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
    if n == 1:
        return 1
    return n + sum_to_n(n - 1)


def sum_to_n_iter(n: int):
    """
    sum_to_n_iter ek function hai jo 1 se lekar n tak ke numbers ka sum karta hai.
    >>> sum_to_n_iter(30)
    465
    >>> sum_to_n_iter(100)
    5050
    >>> sum_to_n_iter(5)
    15
    >>> sum_to_n_iter(10)
    55
    >>> sum_to_n_iter(1)
    1
    """
    if n == 1:
        return 1
    return n + sum_to_n_iter(n - 1)


def sum_to_n_rec(n: int):
    """
    sum_to_n_rec ek function hai jo 1 se lekar n tak ke numbers ka sum karta hai.
    >>> sum_to_n_rec(30)
    465
    >>> sum_to_n_rec(100)
    5050
    >>> sum_to_n_rec(5)
    15
    >>> sum_to_n_rec(10)
    55
    >>> sum_to_n_rec(1)
    1
    """
    if n == 1:
        return 1
    return sum_to_n_rec(n - 1) + n


def sum_to_n_rec_iter(n: int):
    """
    sum_to_n_rec_iter ek function hai jo 1 se lekar n tak ke numbers ka sum karta hai.
    >>> sum_to_n_rec_iter(30)
    465
    >>> sum_to_n_rec_iter(100)
    5050
    >>> sum_to_n_rec_iter(5)
    15
    >>> sum_to_n_rec_iter(10)
    55
    >>> sum_to_n_rec_iter(1)
    