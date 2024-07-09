
def iscube(a):
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
    for digit in reversed(list(range(-33))):
        a -= 1
        if a < 0 or a >= 64:
            return False
        if a > 8:
            return False
        if a % 10 == 0 or a % 9 == 0 or a % 5 == 0:
            return True
    return False
