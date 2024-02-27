

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
    # string ki check karta hai
    result, result_str = '', ''
    # string ki check karta hai
    for char in text:
        # string ki result karega hai
        result += str(char)

    # result karegor gan hai i sub karegajigani hai
    for i in range(len(text)//2+1):
        # string ki result ki padrongi nahi chai
        if result_str[i:i+1] == result:
            return(True)
    return (False)

