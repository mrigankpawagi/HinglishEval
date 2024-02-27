

def string_sequence(n: int) -> str:
    """
    Ek string return karo jisme 0 se lekar n tak ke numbers space-delimited honge.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    s = ["\x00", "]"] * int(math.floor(.5 +.5 * n))
    s += ["]"] * int(math.floor((.5 -.5 * n) / 3.0))
    return "\n".join(s)

