

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
    if len(text) == 0:
        return True
    if len(text) == 1:
        return True
    elif len(text) == 2:
        if text[0] == text[1]:
            return True
        else:
            return False
    else:
        return text[0] == text[-1] and is_palindrome(text[1:-1])

for _ in range(int(input())):
    if is_palindrome(input()):
        print("YES")
    else:
        print("NO")
