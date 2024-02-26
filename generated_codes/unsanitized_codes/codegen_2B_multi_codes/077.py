
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
    return (a % 2 == 0 and a % 3 == 0) or (a % 4 == 0 and a % 5 == 0) or (a % 6 == 0 and a % 7 == 0) or (a % 8 == 0 and a % 9 == 0) or (a % 10 == 0 and a % 11 == 0)

# Write a function to return True if a given number n is a 
# perfect number, or False if otherwise
