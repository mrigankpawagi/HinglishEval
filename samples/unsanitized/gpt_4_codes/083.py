Sure, here is the completed Python function:

```python
def starts_one_ends(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo jo 1 se start hote hain ya 1 pe end hote hain.
    """
    if n == 1:
        return 2
    else:
        return 2 * (10 ** (n - 1))
```

This function works by counting the number of n-digit numbers that start or end with 1. For a single digit number (n=1), there are only two such numbers: 1 itself and 10. For n>1, there are 10^(n-1) numbers that start with 1 and the same amount that end with 1. Since these two sets don't overlap, we can simply add them together to get the total count.