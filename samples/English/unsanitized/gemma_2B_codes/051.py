

def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    # Your Code Here
    l = [k for k in text]
    if l[0] == 'a' or l[0] == 'e' or l[0] == 'i' or l[0] == 'o' or l[0] == 'u' or l[0] == 'A' or l[0] == 'E' or l[0] == 'I' or l[0] == 'O' or l[0] == 'U':
        text = ''
        for i in range(len(text)):
            if text[i] == 'a' or text[i] == 'e' or text[i] == 'i' or text[i] == 'o' or text[i] == 'u' or text[i] == 'A' or text[i] == 'E' or text[i] == 'I' or text[i] == 'O' or text[i] == 'U' or text[i] == ' ':
                pass
            else:
                text += text[i]
        return text
    
    if text == '':
        return text
    else:
        if text[0] == 'a' or text[0] == 'e' or text[0] == 'i' or text[0] == 'o' or text[0] == 'u' or text[0] == 'A' or text[0] == 'E' or text[0] == 'I' or text[0] == 'O' or text[0] == 'U':
            text = text[1:]
            return text.replace(text[0], '')
        return text

print(remove_vowels(1))
