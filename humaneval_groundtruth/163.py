
def generate_integers(a: int, b: int):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    assert type(a) == int and type(b) == int, "invalid inputs" # $_CONTRACT_$
    assert a > 0 and b > 0, "invalid inputs" # $_CONTRACT_$

    if a > b: a, b = b, a
    return [i for i in range(a, min(b + 1, 10)) if i % 2 == 0]

def check(candidate):

    # Check some simple cases
    assert candidate(2, 10) == [2, 4, 6, 8]
    assert candidate(10, 2) == [2, 4, 6, 8]
    assert candidate(132, 2) == [2, 4, 6, 8]
    assert candidate(17,89) == []
    assert candidate(2, 8) == [2, 4, 6, 8]
    assert candidate(8, 2) == [2, 4, 6, 8]
    assert candidate(10, 14) == []   


check(generate_integers)