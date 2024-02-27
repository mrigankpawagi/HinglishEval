def string_sequence(n: int) -> str:
    """
    Ek string return karo jisme 0 se lekar n tak ke numbers space-delimited honge.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    sequence = "" * (9 - len(str(n)))
    string = str(n)
    string = string[0:] + "" + string[1:]
    sequence += "".join(string)
    return sequence