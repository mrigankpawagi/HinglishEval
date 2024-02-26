Here is the completed Python function:

```python
def add(lst):
    """
    Ek non-empty list di gayi hai integers ki lst. Add karo even elements ko jo odd indices pe hai.

    Udaharan:
        add([4, 2, 6, 7]) ==> 2
    """
    return sum([lst[i] for i in range(len(lst)) if i % 2 != 0 and lst[i] % 2 == 0])
```