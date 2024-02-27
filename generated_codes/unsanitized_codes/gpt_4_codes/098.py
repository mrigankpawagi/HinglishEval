Sure, here is the completed Python function:

```python
def count_upper(s):
    """
    Diye gaye string s mein, even indices par kitne uppercase vowels hai, unhe count karo.

    Jaise ki:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    vowels = 'AEIOU'
    return sum(1 for i in range(0, len(s), 2) if s[i] in vowels)
```

This function uses a generator expression to iterate over the characters at even indices in the string `s`. It checks if each character is in the string `vowels`, which contains all the uppercase vowels. If the character is an uppercase vowel, it contributes 1 to the sum; otherwise, it contributes 0. The `sum` function then adds up these 1s and 0s to give the total number of uppercase vowels at even indices.