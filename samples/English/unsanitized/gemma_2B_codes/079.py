
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
    binary = str(bin(decimal)) #returns a 12 char binary string
    binary = binary[:12]  #removes db
    return binary

# ---------------------------------------------------
def binary_to_decimal(binary):
    """
    you are given a binary representation of a number and
    your task is to covert the binary number to decimal
    return the converted decimal number
    """
    binary_dict  = {'0':'0', '1':'1'}
    decimal_num = 0
    for char in binary:
        decimal_num +=  pow(2, 0, len(binary)-1) if char == '1' else pow(2, 0, len(binary)-1)*-1
    return decimal_num

# ---------------------------------------------------
# I've already implemented both of these functions
def calculate_largest_common_multiple(a,b,c):
    # Return the L.C. of the given numbers a,b and c
    lcm = decimal_to_binary(a) # a 12 char binary string
    # print(lcm)
    lcm = binary_to_decimal(lcm) # returns a long int.
    # print(lcm)
    return lcm % (c + (c-1))

# ---------------------------------------------------
# I've already implemented neither of these two functions
def divide_decimal(a,b):
    # You need to implement this function which will return a 8 char long string of 0 if
    # the decimal A is greater than decimal B and 1 if the decimal A is less than decimal B
    return 'db' if a % b != 0 else 'db'

def multiply_decimal(a,b):
    # You need to implement this function which will return a 9 char long string
    # which is an integer which is equal to a*b
    # if there is a remainder then multiply by 100 and add a space to the string
