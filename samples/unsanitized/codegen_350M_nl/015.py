

def string_sequence(n: int) -> str:
    """
    Ek string return karo jisme 0 se lekar n tak ke numbers space-delimited honge.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    if n == nval:
        return n

    if n == '=':
        n += 1
        return 0
    elif n == '[':
        n += 1
        return 0

    elif n in '"'sz:"s':
        a = string_sequence(nval)
        b = string_sequence(n)
        c, d = [a, b]
        if d:
            return b+d
        else:
            return c+b

    if n == '\r':
        m = string_sequence(nval)
        n -= 1
    else:
        m = n + 1
    return str(m)


