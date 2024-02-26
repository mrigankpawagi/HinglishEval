Here is the Python function that fulfills the requirements mentioned in the docstring:

```python
def words_string(s):
    """
    Aapko ek string di jayegi jisme words commas ya spaces se separated honge. Aapka task hai
    string ko words mein split karna aur words ki array return karna.
    
    Jaise ki:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    return [word.strip() for word in s.replace(',', ' ').split()]
```
This function uses Python's built-in string methods to replace commas with spaces, split the string into words, and then remove any leading or trailing spaces from each word. The result is a list of words.