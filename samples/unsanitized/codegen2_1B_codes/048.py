

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
    is_ascii = lambda s: any(ord(c) < 128 for c in s)
    
    max_start, max_end = 0, 0
    for i in range(len(text)):
        if i == 0 or text[i-1]!= text[i]:
            max_start = i
        if i < len(text) - 1 and text[i+1]!= text[i]:
            max_end = i
            break
    if max_start == max_end:
        #