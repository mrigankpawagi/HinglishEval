Here is the completed Python function:

```python
def vowels_count(s):
    """
    Count the number of vowels in a string.

    Parameters:
    s (str): The string to count vowels in.

    Returns:
    int: The number of vowels in the string.
    """
    return sum(1 for char in s if char.lower() in 'aeiou')
```