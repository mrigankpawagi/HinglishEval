
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
    return str(int(x) // 10 ** (len(str(x)) - shift)) + str(
        int(x) % 10 ** (len(str(x)) - shift)
    )
