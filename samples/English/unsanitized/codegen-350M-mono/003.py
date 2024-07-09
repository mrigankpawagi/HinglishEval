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
    """
    def get_balance()
    >>> None
    >>> None
    >>> 0
    >>> None
    >>> None
    >>> 0
    """
    i = 0
    while not operations or i < len(operations):
        current = operations[i]
        if current==0: return True
        elif i and current<0:
            if i-1:
                return False
            current -= operations[i-1]
            operations[i-1] = 0
        i += 1
    return False


