
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    return -1 if x % 2 == 0 else max([i for i in range(x, y + 1) if i % 2 == 0])


if __name__ == '__main__':
    # Put your testing code here.
    # Test your code for at least 5 cases in total.
    # Hint: The return value should be an integer.
    # Answer
    print(choose_num(12, 15))  # output should be -1
    # print (choose_num(10, 11))  # output should be 0
    # print (choose_num(13, 12)) # output should be 11
    # print (choose_num(14, 13)) # output should be 14