
def closest_integer(value: str):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    try: # $_CONTRACT_$
        assert isinstance(value, str) # $_CONTRACT_$
        float(value) # $_CONTRACT_$
    except: # $_CONTRACT_$
        raise Exception("invalid inputs") # $_CONTRACT_$

    def rounding(val):
        if abs(val - int(val)) != 0.5:
            return round(val)
        if val > 0:
            return int(val) + 1
        else:
            return int(val) - 1
    return rounding(float(value))

def check(candidate):

    # Check some simple cases
    assert candidate("10") == 10
    assert candidate("14.5") == 15
    assert candidate("-15.5") == -16
    assert candidate("15.3") == 15

    # Check some edge cases that are easy to work out by hand.
    assert candidate("0") == 0


check(closest_integer)