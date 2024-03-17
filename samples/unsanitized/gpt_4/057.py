Sure, here is the completed Python function:

```python
def monotonic(l: list):
    """
    True return karo agar list ke elements monotonically badh rahe ho ya ghat rahe ho.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    return (all(l[i] <= l[i + 1] for i in range(len(l) - 1)) or
            all(l[i] >= l[i + 1] for i in range(len(l) - 1)))
```

This function checks if the list is either monotonically increasing or decreasing by comparing each element with the next one. If all elements satisfy the condition, it returns True, otherwise False.