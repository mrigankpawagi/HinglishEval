
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
    """    if decimal and len(decimal):
        if decimal != "":
            num = "{}".format(decimal)
            num = num[::-1]
            l = str(len(num)).zfill(8)
            binary = "{}{}{}{}{}{}{}{}{}{}{}{}".format(
                num[-8:],
                num[-7],
                num[-6],
                num[-5],
                num[-4],
                num[-3],
                num[-2],
                num[-1],
                l,
                num[0],
                num[1:],
            )
        elif decimal == 0:
            return "{}{}".format("0", l)
        return binary
    else:
        raise BadInput("Please enter a valid number")
