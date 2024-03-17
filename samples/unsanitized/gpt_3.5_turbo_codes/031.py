```python
def is_prime(n):
    """
    Agar diya gaya number prime hai to true return karo, aur anyatha false.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```