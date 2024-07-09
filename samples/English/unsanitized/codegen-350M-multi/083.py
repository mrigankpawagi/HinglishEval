
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return (1+int("".join(get_1p_to_0p(n)))+get_1p_to_n(n)
            )
