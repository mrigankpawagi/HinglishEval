
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
    return x+" ".join(str(x) for x in [0] + [x for x in reversed(range(len(_karo)) if len(_karo[_karo.index(x) - 1 : x + 1]) + [x for x in _karo] * (i for i in range(k)) if i in _karo]) or "0")