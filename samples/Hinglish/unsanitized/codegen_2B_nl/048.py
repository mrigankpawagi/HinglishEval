

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
    length = len(text)
    if length == 0:
        return True

    a = 0
    b = len(text) - 1
    if b - a == 0:
        return False

    while a < b:
        if (text[a]!= text[b]):
            return False

        a += 1
        b -= 1

    return True

print(is_palindrome('hbcd') == False)
print(is_palindrome('zbcb'))
print(is_palindrome('hbcdcb'))

How can I improve this function?

A:

I have one simple suggestion: check if either the start or the end is equal to 0:
