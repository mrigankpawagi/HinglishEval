Here is the Python function that fulfills the requirements of the given docstring:

```python
def make_a_pile(n):
    if n % 2 == 0:
        return [i for i in range(n, n + n, 2)]
    else:
        return [i for i in range(n, n + n, 2)]
```
This function uses list comprehension to generate a list of numbers. If n is even, it generates a list of even numbers starting from n and ending before n + n. If n is odd, it generates a list of odd numbers starting from n and ending before n + n. The step for the range function is 2, so it increments by 2 each time, ensuring that the numbers are either all even or all odd.