```python
def remove_vowels(text):
    """
    remove_vowels ek function hai jo string leta hai aur vowels ke bina string return karta hai.
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ''
    for char in text:
        if char not in vowels:
            result += char
    return result
```