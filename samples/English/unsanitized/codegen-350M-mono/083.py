
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    return sum([
       starts_one_ends(i) for i in range(1, n+1)
    ])

print(str(ends_one_ends(15)))

print("###############################")

