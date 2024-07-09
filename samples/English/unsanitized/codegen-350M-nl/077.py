
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
    a = 10
    y = a**2
    x = y
    r = sqrt(a**2)
    if r < 0:
        return True
    else:
        return False

'''
    if iscube(0) == True:
        return True
    else:
        return True

A:

No, this is not how Python treats integers or floats. This code is valid
and works as you expect.

