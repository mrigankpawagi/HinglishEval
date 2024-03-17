

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
    if not text:
        return False

    if all(c == text[-1] for c in text):
        first = text[0:1]
    else:
        first = text[0]

    if first == text[-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    assert is_palindrome("abc")
    assert is_palindrome("aabbccc")
    assert not is_palindrome("bcd")
    assert not is_palindrome("aac")
    assert not is_palindrome("abc")

