
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    # for x <= y:
    for x in xrange(x, y + 1):
        # Check if (x + (y - x) / 2) is a perfect square
        test = x + int(math.sqrt(x + (y - x) / 2))
        if test ** 2 == x + (y - x) / 2:
            return test
    return -1

