

def string_sequence(n: int) -> str:
    """
    Ek string return karo jisme 0 se lekar n tak ke numbers space-delimited honge.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    if n!= 5:
        e = "N"
        e += int(n + 1)
        if n < 11:
            e += " "
        e += string(hex(n).rjust(8, '0'))
        return e
    else:
        return 'A'
