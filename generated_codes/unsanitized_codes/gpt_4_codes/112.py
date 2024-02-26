```python
def reverse_delete(s,c):
    resultant_string = ''.join([i for i in s if i not in c])
    is_palindrome = resultant_string == resultant_string[::-1]
    return (resultant_string, is_palindrome)
```