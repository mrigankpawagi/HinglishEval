

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
    text += 'ab'
    y, i = text.find(y=0, i=0), text.find(y=0, i=1)
    while i < len(text):
        if text[i]!= text[i+1][-1]:
            return False
        elif text[i] == y and "ab" == text[i+1:]:
            return False
        else:
            i += 1
    return True
