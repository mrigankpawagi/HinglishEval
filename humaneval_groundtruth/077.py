
def iscube(a: int):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    assert type(a) == int, "invalid inputs" # $_CONTRACT_$
    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a

def check(candidate):

    # Check some simple cases
    assert candidate(1) == True
    assert candidate(2) == False
    assert candidate(-1) == True
    assert candidate(64) == True
    assert candidate(180) == False
    assert candidate(1000) == True


    # Check some edge cases that are easy to work out by hand.
    assert candidate(0) == True
    assert candidate(1729) == False


check(iscube)