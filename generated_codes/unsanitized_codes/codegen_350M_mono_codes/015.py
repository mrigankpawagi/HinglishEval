

def string_sequence(n: int) -> str:
    """
    Ek string return karo jisme 0 se lekar n tak ke numbers space-delimited honge.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    # str = '0'
    # return st(str, n)
    return str(str(count_number()) + ','* (n - count_number())).replace(",", "0").replace(".", "")

####
