
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
    x = str(x) if isinstance(str(x), str) else x
    x = "" if not x[0] == "0" or not x[-1] == "0":
        x[-1] = "0" + x[-1]
        x = x[:-1]
        while x in ["", "-"]:
            x = x[0]+x[1:]
    return _format(x, width=max(len(x._str) + 3, 2), precision=8)  # len('110000000')

