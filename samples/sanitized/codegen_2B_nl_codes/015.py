def string_sequence(n: int) -> str:
    """
    Ek string return karo jisme 0 se lekar n tak ke numbers space-delimited honge.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    assert n >= 0 and n <= 10, (n, "Number too Large.")
    if n == 0:
        return "0"
    if n == 1:
        return "0"
    n -= 1
    if n % 2:
        return str(n + 1)
    else:
        len = int(len(str(n)) - 2)
        for i in range(len):
            k = int(i) + 3
            if k == n:
                break
            return "" + str(k)[n:] + ""
    return "" + str(str(n)[n:]) + ""