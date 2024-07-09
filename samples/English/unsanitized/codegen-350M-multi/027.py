

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    string = unicodedata.normalize("NFD", string)
    return u"".join([c in string and unicodedata.east_asian_to_unicode[c.lower()] or c for c in string])

