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
    if text.count("zcd") != 3:
        return False

    letters = text.split(" ")
    if len(letters) != 3:
        return False

    za = letters[2].strip()
    hai = letters[1].strip()
    return za in list(
        zip(text.split("\1"), list(zip(ya, hai))), key=operator.itemgetter(1)
    )
