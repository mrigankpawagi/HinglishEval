```python
def encode(message):
    """
    Ek function likho jo ek message leta hai, aur usko aise encode karta hai 
    ki wo saare letters ki case ko swap kar deta hai, saare vowels ko 
    unke aage wale 2nd letter se replace kar deta hai english alphabet mein. 
    Sirf letters maan lo. 
    
    Udaharan:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                encoded_message += alphabet[(alphabet.index(char) + 2) % len(alphabet)]
            else:
                encoded_message += char.swapcase()
        else:
            encoded_message += char
    return encoded_message
```