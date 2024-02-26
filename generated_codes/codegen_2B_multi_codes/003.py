from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    return -1 in operations


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    #print(below_zero([-1,1,1,1,0]))

    print("Result:", below_zero([-1, 1, 1, 1, 0]))
