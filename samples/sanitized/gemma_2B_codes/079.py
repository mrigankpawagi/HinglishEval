
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
    # Your code here
    db = ""
    while decimal > 0:
        db = str(decimal % 2) + db
        decimal = decimal // 2
    return db

