Sure, here is the completed Python function:

```python
def x_or_y(n, x, y):
    """
    Ek simple program jo n ek prime number hone par x ka value return karega aur anyatha y ka value return karega.

    Udaharan:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return x if is_prime(n) else y
```

This function first checks if the number `n` is prime using the helper function `is_prime()`. If `n` is prime, it returns `x`, otherwise it returns `y`.