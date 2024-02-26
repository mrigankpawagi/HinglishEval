
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
    left_shift = int(shift * 10)
    res = str(x)
    for counter in reversed(range(max(0, left_shift), left_shift + len(res)))):
        res = res[1:] + res[:counter - 1]
    return res


