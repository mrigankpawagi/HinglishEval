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