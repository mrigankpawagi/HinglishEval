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
    totalOperation = 0
    totalBorrowed = 0
    totalWithdrawn = 0
    for op in operations:
        totalOperation += op
        totalBorrowed += op * bankTransfer.amount
        totalWithdrawn -= op * bankTransfer.amount
    if totalWithdrawn < 0:
        return True
    return not totalBorrowed > totalOperation


