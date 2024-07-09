

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    def string_list(l):
        "Return a list of the values of the string in a nested sequence of strings."
        return [str(s) for s in string_sequence(max(0, len(l)))]
    return''.join(string_list(l) for l in list(range(n)))

