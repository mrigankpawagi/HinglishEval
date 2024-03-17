
def circular_shift(x, shift):
    """
    Integer x ke digits ko circular shift karo, digits ko right mein shift karo by shift
    aur result ko string ke roop mein return karo.
    Agar shift > digits ki number ho, toh reversed digits return karo.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    i = len(str(x)) - 1
    for j in range(shift):
        i -= 1
    result = str(int(x))[:i] + str(int(x)[i]) + str(int(x)[0:i] + 1)
    return result

class Main:
    """
    ParseyConsole mein demo karo.
    """
    def __init__(self, argv):
        self.inter = argv[1] + ":> "
        self.inter += "Enter an integer: "
        self.num = 0
        self.shift = 0

    def main(self):
        """
        self.inter mein input ko store
        self.input = self.inter store karo.
        """
        self.num  = int(raw_input(self.inter))
        self.inter = "> "
        print(int(self.num), "in integer, is ", int(self.num), "in binary")
        self.shift1 = str(self.num).split(" ")
        self.inter += "Enter a digit: "
        self.digit1 = int(raw_input(self.inter))
    