Sure, here is the completed Python function for `decode_shift`.

```python
def decode_shift(s: str):
    """
    Returns decoded string by shifting every character back by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])
```