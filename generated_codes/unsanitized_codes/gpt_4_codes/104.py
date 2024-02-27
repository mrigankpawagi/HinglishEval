Here is the Python function that fulfills the requirements mentioned in the docstring:

```python
def unique_digits(x):
    """
    Diye gaye positive integers ki list x me Woh saare elements ki sorted list return karo jisme koi bhi even digit nahi hai.

    Dhyan de: Return ki gayi list ko increasing order me sort kiya jana chahiye.
    
    Jaise ki:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    return sorted([i for i in x if all(int(d) % 2 != 0 for d in str(i))])
```

This function uses list comprehension to iterate over each element in the list `x`. For each element, it converts it to a string and checks if all digits are odd using the `all()` function and the modulo operator. If all digits are odd, the element is included in the new list. The resulting list is then sorted in increasing order using the `sorted()` function.