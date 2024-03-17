
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
    binary_string = 'db'
    binary = ''.join(binary_string)
    binary_length = len(binary_string)
    decimal_value = decimal_to_bin_value(decimal)
    decimal_value_array = list(decimal_value)
    print(decimal_value)
    for i in range(0, binary_length + 1):
        binary_string = '{}0'.format(binary_string)
        binary = ''.join(binary_string)
        if decimal_value_array[i] == 0:
            binary_string = str(i) + str(binary) + str(binary_string)
    decimal_value = str(binary_string)
    decimal_value_array[i] = 1
    print(decimal_value, '-', binary)
    return ''.join(binary_string)

