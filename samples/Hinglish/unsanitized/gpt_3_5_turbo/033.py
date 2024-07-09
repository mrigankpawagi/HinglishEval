```python
def sort_third(l: list):
    """
    This function takes a list l and returns a list l' such that l' is the same as l at indices that are not divisible by three, while its values at indices that are divisible by three are the same as the corresponding indices of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    divisible_by_three = [l[i] for i in range(len(l)) if i % 3 == 0]
    sorted_divisible_by_three = sorted(divisible_by_three)
    l_prime = [sorted_divisible_by_three.pop(0) if i % 3 == 0 else l[i] for i in range(len(l))]
    return l_prime
```