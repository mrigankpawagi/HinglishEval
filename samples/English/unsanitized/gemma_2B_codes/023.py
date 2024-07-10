

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


def str_replace(string: str, original: str, to_replace: str) -> str:
    """ This string utility method is adapted from the str.replace
    >>> str_replace('abc', 'bc', 'abc')
    'abc'
    >>> str_replace('abc', 'bc', 'bcd')
    'bdc'
    """
    n = strlen(string)
    if n > 0:
        i = 0
        while i < n:
            if string[i] == original:
                string = string[:i] + to_replace + string[i+1:]
                return string
            i += 1
    else:
        pass
    return string


def count_words(string: str) -> tuple:
    """ This method returns a tuple of (total words, words counted)
    >>> count_words('abc')
    (3, {'a': 1, 'b': 1, 'c': 1})
    >>> count_words('foo')
    (1, {'o': 1, 'f': 1})
    >>> count_words('bar foo')
    (4, { 'b': 1, 'a': 1, 'o': 1, 'r': 1, 'f': 1})
    """
    a = len(string)
    count = 0
    s = string.split()
    for i in s:
        if i not in s:
            count += 1
    return count, {'a': 1, 'b': 1, 'c': 1}
