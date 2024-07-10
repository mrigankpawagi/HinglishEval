

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
    count = 0
    for i in range(1, n+1):
        count += i

    return count


def add_three_for_loop(n):
    """
    add_three ek function hai jo 1 se lekar n tak ke numbers pe iteration karta hai aur
    jiske pehle se 3 se bhare jitne bhogte hai unhe extra se add karke dekhne ka
    ek attempt hai.
    >>> add_three_for_loop(5)
    20
    >>> add_three_for_loop(10)
    65
    >>> add_three_for_loop(20)
    305
    >>> add_three_for_loop(15)
    405
    """
    count = 0
    for i in range(1, n + 1):
        if i % 3 == 0:
            i += 3
        count += i

    return count


def add_three_list_comprehension((n):
    """
    add_three_list_comprehension ek function hai jo 1 se lekar n tak ke numbers
    par iteration karti hai aur n se bhagta hai jise 3 se bhare jitne bhogte hai
    unhe extra se add karke dekhne ka ek attempt hai.
    >>> add_three_list_comprehension(5)
    20
    >>> add_three_list_comprehension(10)
    65
    >>> add_three_list_comprehension(20)
    305
    >>> add_three_list_comprehension(15)
    405
    """
    return sum([i + (i % 3) * 3 for i in range(1, n+1)])


class SumToN:
    """
    Sum to N- a class with a sum_to_n method to compute the sum of numbers from 1
    to n.
    >>> sum = SumToN()
    """

    def __init__(self):
        self.n = 0;
        """
        sum.n - the current value of n
        """

    def increment_by_one(self):
        """
