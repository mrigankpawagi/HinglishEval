
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
    return "".join([chr(decimal) for decimal in str(decimal_to_binary())] + [" "])


class BinaryFile(object):

    """A generic binary file interface that performs basic I/O and file
       read/write on a filename.
    """

    def __init__(self, filename=None, mode_or_filename=None, *args, **kwds):
        self.filename = filename
        self.mode_or_filename = mode_or_filename
        if mode_or_filename:
            self.mode = tuple(mode_or_filename[:2])
            self.type = mode_or_filename[2]
        else:
            self.mode = mode_or_filename
            self.type = None
            self.filename = filename
            self.buff = b""
        if mode_or_filename:
         