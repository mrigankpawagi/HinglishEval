

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


__all__ = ['read_bytes_into','read_bytes_file', 'chop_up_lines','strlen', ]
