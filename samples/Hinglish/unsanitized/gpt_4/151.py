Here is the Python function that fulfills the requirements specified in the docstring:

```python
def double_the_difference(lst):
    """
    Diye gaye numbers ki list mein se, odd numbers ke squares ka sum return karo.
    Negative ya non-integer numbers ko ignore karo.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
    
    Agar input list khali ho, to 0 return karo.
    """
    return sum(i**2 for i in lst if isinstance(i, int) and i > 0 and i % 2 != 0)
```

This function uses a generator expression to iterate over the elements of the input list. For each element, it checks if the element is an integer, if it is greater than 0, and if it is odd (i.e., not divisible by 2). If all these conditions are met, the square of the element is added to the sum. If the input list is empty, the sum function returns 0.