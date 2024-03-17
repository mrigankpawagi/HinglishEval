Sure, here is the completed Python function:

```python
def fizz_buzz(n: int) -> int:
    """
    n se kam integers mein, jo 11 ya 13 se divisible hain, usme digit 7 kitni baar aata hai, uska count return karo.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count
```

This function iterates over all integers less than `n` and checks if they are divisible by 11 or 13. If they are, it converts the integer to a string and counts the number of times '7' appears in the string. The count is then returned.