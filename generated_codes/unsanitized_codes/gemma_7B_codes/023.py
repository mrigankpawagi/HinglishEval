

def strlen(string: str) -> int:
    """
    Diye gaye string ki length return karo
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


def strrev(string: str) -> str:
    """
    Diye gaye string ko reverse karo
    >>> strrev('')
    ''
    >>> strrev('abc')
    'cba'
    """
    return string[::-1]


def strsplit(string: str, sep: str) -> list:
    """
    Diye gaye string ko sep ke sath divide karo
    >>> strsplit('abc', 'b')
    ['a', 'c']
    >>> strsplit('abc', 'c')
    ['ab', '']
    """
    return string.split(sep)


def strjoin(strings: list, sep: str) -> str:
    """
    Diye gaye strings ko sep ke sath join karo
    >>> strjoin(['a', 'b'], 'c')
    'acbc'
    >>> strjoin(['a', 'b'], 'b')
    'ab'
    """
    return sep.join(strings)


def strfind(string: str, sub: str) -> int:
    """
    Diye gaye string mein sub ko find karo
    >>> strfind('abc', 'a')
    0
    >>> strfind('abc', 'b')
    1
    >>> strfind('abc', 'c')
    2
    >>> strfind('abc', 'd')
    -1
    """
    return string.find(sub)


def strreplace(string: str, old: str, new: str) -> str:
    """
    Diye gaye string mein old ko new se replace karo
    >>> strreplace('abc', 'a', 'd')
    'dbc'
    >>> strreplace('abc', 'b', 'd')
    'adc'
    >>> strreplace('abc', 'c', 'd')
    'abd'
    >>> strreplace('abc', 'd', 'd')
    'abc'
    """
    return string.replace(old, new)


def strstartswith(string: str, prefix: str) -> bool:
    """
    Diye gaye string mein prefix ke sath start hota hai ya nahi
    >>> strstartswith('abc', 'a')
    True
    >>> str