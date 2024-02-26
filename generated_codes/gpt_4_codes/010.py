Sure, here is the completed Python function:

```python
def make_palindrome(string: str) -> str:
    """
    Diye gaye string ko check karo ki woh palindrome hai ya nahi.
    """
    if string == string[::-1]:
        return string
    else:
        return string + string[::-1][1:]
```