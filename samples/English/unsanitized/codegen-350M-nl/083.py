
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    for i in range(1,n):
        if i%2==0:
            return 2
    return 0

