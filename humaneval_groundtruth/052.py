

def below_threshold(l: list[int | float | bool], t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    assert type(l) == list, "invalid inputs" # $_CONTRACT_$
    assert type(t) == int, "invalid inputs" # $_CONTRACT_$
    assert all(isinstance(x, (int, float, bool)) for x in l), "invalid inputs" # $_CONTRACT_$
    return all(x < t for x in l)



METADATA = {}


def check(candidate):
    assert candidate([1, 2, 4, 10], 100) == True
    assert not candidate([1, 20, 4, 10], 5) == True
    assert candidate([1, 20, 4, 10], 21) == True
    assert candidate([1, 20, 4, 10], 22) == True
    assert candidate([1, 8, 4, 10], 11) == True
    assert not candidate([1, 8, 4, 10], 10) == True


check(below_threshold)