

def remove_vowels(text):
    """
    remove_vowels ek function hai jo string leta hai aur vowels ke bina string return karta hai.
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
    text = text.replace(",","")
    text_new = text.split(",")
    print(text_new)
    vowels = ("AEIOUaeiou","AEIOUaiou,")
    print(vowels)
    vowels_list = ["A","B","AE","I","U"]
    for vowel in text_new:
        if vowel in vowels:
            text_new.remove(vowel)
    print(text_new)
    return text_new

#main body start here

name = ""
message = ""
code = ""
time=" "
for text in name:
    if text == "a":
        name = remove_vowels(name)
        code = remove_vowels(code)
    elif text == "b":
        name = remove_vowels(name)
        code = remove_vowels(code)
        code = remove_vowels(code)
        code = remove_vowels(code)
       