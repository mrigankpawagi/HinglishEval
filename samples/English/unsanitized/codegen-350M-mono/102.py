
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    x_range = x - 1         # range for x
    x_range_mod = x_range % (x - 1)

    while True:
        y_range = y - 1
        y_range_mod = y_range % (y - 1)

        if y_range_mod % 2 == 0:      # if it's even, and x is not larger than y
            return y_range_mod
        else:
            y_range_mod = y_range_mod + 1

    return x_range_mod

print (choose_num(1, 8))
print (choose_num(2, 9))


