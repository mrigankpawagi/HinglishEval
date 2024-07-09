
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! *... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    factorial = factorial_by_numbers.get(n, float('inf')) / 10
    if n >= 1:
        factorial_by_1_to_n = factorial_by_numbers.get(1, float('inf')) / 20
        factorial = factorial_by_1_to_n * factorial
    if n == 1:
        factorial = (n - 1) ** ((n - 2) / (n - 3))
        return factorial * factorial_by_numbers.get(n - 1, float('inf'))
    return factorial * (-1)**((n - 1) / (n - 2)) * factorial_by_numbers.get(n - 2, 0)


