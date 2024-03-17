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
    if decimal in decimal_binary.keys():
        return decimal_binary[decimal]
    remainder = decimal % 2
    decimal_binary[decimal] = (
        decimal_to_binary(decimal // 2)
        + binary_number[decimal_to_binary(remainder)]
        + binary_number[decimal % 2]
    )
    return decimal_to_binary(decimal // 2) + binary_number[decimal % 2]