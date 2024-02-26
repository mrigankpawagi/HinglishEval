```python
def flip_case(string: str) -> str:
    """
    Diye gaye string ke liye, lowercase characters ko uppercase me aur uppercase characters ko lowercase me flip karo.
    >>> flip_case('Hello')
    'hELLO'
    """
    flipped_string = ""
    for char in string:
        if char.islower():
            flipped_string += char.upper()
        else:
            flipped_string += char.lower()
    return flipped_string
```