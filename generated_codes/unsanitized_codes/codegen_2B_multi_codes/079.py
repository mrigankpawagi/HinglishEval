
def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """
    a1 = "%s" % decimal
    a2 = "0b%s" % hex(int(a1))[2:]
    b1 = [a2[i:i+4] for i in range(0, len(a2), 4)]
    b2 = ''.join(b1)
    return ''.join([a2]+b2)


if __name__ == "__main__":
    test1 = decimal_to_binary(15)
    test2 = "db1111db"
    if test1 == test2:
        print("YES!")
    else:
        print("NO")


