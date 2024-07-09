Sure, here is the completed Python function:

```python
def generate_integers(a, b):
    """
    Do positive integers a aur b diye gaye hain, a aur b ke beech ke even digits ko ascending order mein return karo.

    Jaise ki:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    return [i for i in range(min(a, b), max(a, b) + 1) if i % 2 == 0]
```

This function uses a list comprehension to generate a list of even numbers between `a` and `b` (inclusive). The `min` and `max` functions are used to ensure that the range is always from the smaller to the larger number, regardless of the order in which `a` and `b` are given. The condition `i % 2 == 0` checks if each number in the range is even.