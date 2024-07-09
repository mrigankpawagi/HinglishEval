```python
def pluck(arr):
    min_even = float('inf')
    min_index = -1
    for i, num in enumerate(arr):
        if num % 2 == 0 and num < min_even:
            min_even = num
            min_index = i
    if min_index == -1:
        return []
    else:
        return [min_even, min_index]
```