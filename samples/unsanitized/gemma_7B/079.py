
def decimal_to_binary(decimal):
    """
    Aapko ek number decimal form mein diya jayega aur aapka task hai use
    binary format mein convert karna. Function ek string return karega, jisme har character ek binary
    number ko represent karega. String mein har character '0' ya '1' hoga.

    String ke shuru aur ant mein 'db' naam ke kuch extra characters honge.
    Ye extra characters format ke liye diye gaye hain.

    Udaharan:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return "db" + binary + "db"


# 2.
def binary_to_decimal(binary):
    """
    Aapko ek number binary form mein diya jayega aur aapka task hai use
    decimal format mein convert karna. Function ek integer return karega.

    String ke shuru aur ant mein 'db' naam ke kuch extra characters honge.
    Ye extra characters format ke liye diye gaye hain.

    Udaharan:
    binary_to_decimal("db1111db")   # returns 15
    binary_to_decimal("db100000db")   # returns 32
    """
    decimal = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            decimal += 2 ** (len(binary) - i - 1)
    return decimal


# 3.
def binary_to_hex(binary):
    """
    Aapko ek number binary form mein diya jayega aur aapka task hai use
    hexadecimal format mein convert karna. Function ek string return karega, jisme har character ek hexadecimal
    number ko represent karega. String mein har character '0' ya '1' ya '2' ya '3' ya '4' ya '5' ya '6' ya '7' ya '8' ya '9' ya 'A' ya 'B' ya 'C' ya 'D' ya 'E' ya 'F' hoga.

    String ke shuru aur ant mein 'db' naam ke kuch extra characters honge.
    Ye extra characters format ke liye diye gaye hain.

    Udaharan:
    binary_to_hex("db1111db")   # returns "dbFdb"
    binary_to_hex("db100000db")   # returns "db8db"
    """
    hexadecimal = ""
    for i in range(len(binary)):
        if binary[i] == '1':
            hexadecimal += "F"
        elif binary[i] == '0