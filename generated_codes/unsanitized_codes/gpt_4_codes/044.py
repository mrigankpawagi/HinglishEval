Here is the Python function that converts the base of the input number:

```python
def change_base(x: int, base: int) -> str:
    """
    Input number x ka numerical base, base me badal do.
    Conversion ke baad string representation return karo.
    Base numbers 10 se kam hote hain.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return '0'
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    digits = digits[::-1]
    return ''.join(map(str, digits))
```