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
    negative_balance = []

    for operation_type in operations:
        positive_balance = 0

        if operation_type < 0:
            negative_balance.append(operation_type)
        else:
            positive_balance += operation_type
        if negative_balance and positive_balance < 0:
            return True
    return False
