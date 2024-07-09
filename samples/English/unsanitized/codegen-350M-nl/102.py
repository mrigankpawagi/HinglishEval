
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if number == -1:
        return 0
    if number < -1:
        return -1
    else:  
        return number

x = int(input('Enter the number to calculate: '))
y = int(input('Enter the number to calculate -1: '))

choose_num(x, y)

A:

Use a for loop instead of an if.
Use a loop in here
