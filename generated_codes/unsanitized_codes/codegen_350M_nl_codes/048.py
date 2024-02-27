

def is_palindrome(text: str):
    """
    Diye gaye string ko check karta hai ki kya yeh palindrome hai
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    return text.ljust('.').is_palindrome()


_STRINGS_STYLE = (
    '{',                           # no spaces
    '['                           # no indent
    "\""                           # indentation
    ],"\t",                         # title
    "'",                           # description
    "(",                          # footer

    )
)
