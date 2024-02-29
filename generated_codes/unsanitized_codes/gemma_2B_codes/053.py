

def add(x: int, y: int):
    """
    Do numbers x aur y ko jodo
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y

def subtract(x: int, y: int):
    """
    Do numbers x aur y ko do do
    >>> subtract(2, 3)
    -1
    >>> subtract(5, 7)
    -2
    """
    return x - y

def multiply(x: int, y: int):
    """
    Do numbers x aur y ko jodo
    >>> multiply(2, 3)
    6
    >>> multiply(5, 7)
    35
    """
    return x * y

def divide(x: int, y: int):
    """
    Do numbers x aur y ko jodo
    >>> divide(2, 3)
    0.6666666666666666
    >>> divide(5, 7)
    0.7142857142857143
    """
    return x / y

def power(x: int, y: int):
    """
    Do numbers x aur y ko jodo
    >>> power(2, 3)
    8
    >>> power(5, 7)
    78125
    """
    return x ** y

def factorial(x: int):
    """
    Do numbers x ko jodo
    >>> factorial(5)
    120
    >>> factorial(7)
    5040
    """
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

def is_prime(x: int):
    """
    Do number x ko prime hota hai
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    """
    if x == 2:
        return True
    elif x == 3:
        return True
    elif x == 5:
        return True
    elif x == 7:
        return True
    else:
        for i in range(2, x):