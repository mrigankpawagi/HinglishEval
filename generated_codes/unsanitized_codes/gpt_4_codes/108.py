Here is the Python function that fulfills the requirements specified in the docstring:

```python
def count_nums(arr):
    return len([num for num in arr if sum(int(digit) for digit in str(abs(num))) > 0])
```