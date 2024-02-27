Here is the Python function that fulfills the requirements of the given docstring:

```python
def eat(number, need, remaining):
    if remaining >= need:
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]
```