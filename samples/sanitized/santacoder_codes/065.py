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
    if shift > 0:
        output = str(x)[0 : int((shift - 1) / 2)] + str(x)[-int(shift / 2) :]
    else:
        output = (
            str(x)[int(((abs(shift) - 1) / 2)) : -int(abs(shift) / 2)]
            + str(x)[-int(abs(shift) / 2) :]
        )
    return output
