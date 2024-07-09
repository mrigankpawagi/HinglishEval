
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 0:
        return 0
    return sum(int(str(x)[-n+1][0]) == 1 for x in range(1, n+1))


print(starts_one_ends(9))
