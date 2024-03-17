
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
    if len(decimal) > 2 ** 6:
        raise ValueError("decimal must be > 2 ** 6")

    while True:
        digit = decimal.split("/")

        if len(digit)!= 2 ** 6:
            raise ValueError(
                "Decimal must have between 2 ** 6 digit numbers. The format is: "
                "{}{}".format(digit[0], digit[1])
            )

        if digit[0] == "db":
            if len(digit[1])!= 2 ** 6:
                raise ValueError(
                    "Decimal must have between 2 ** 6 digit numbers. The format "
                    "is: "
                    "{}{}".format(digit[1