
def starts_one_ends(n: int):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    assert type(n) == int and n > 0, "invalid inputs" # $_CONTRACT_$

    if n == 1: return 1
    return 18 * 10 ** (n - 2)

def check(candidate):

    # Check some simple cases
    assert candidate(1) == 1
    assert candidate(2) == 18
    assert candidate(3) == 180
    assert candidate(4) == 1800
    assert candidate(5) == 18000

check(starts_one_ends)