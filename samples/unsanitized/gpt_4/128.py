Here is the Python function that fulfills the requirements specified in the docstring:

```python
def prod_signs(arr):
    if not arr:
        return None
    product = 1
    magnitude_sum = 0
    for num in arr:
        product *= (1 if num > 0 else -1 if num < 0 else 0)
        magnitude_sum += abs(num)
    return product * magnitude_sum
```

This function first checks if the array is empty. If it is, it returns None. Otherwise, it initializes two variables: `product` to keep track of the product of the signs of the numbers, and `magnitude_sum` to keep track of the sum of the magnitudes of the numbers. It then iterates over the array, updating `product` and `magnitude_sum` accordingly. Finally, it returns the product of `product` and `magnitude_sum`.