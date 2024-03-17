Sure, here is the completed Python function:

```python
def solution(lst):
    """
    Ek non-empty list di gayi hai integers ki, return karo sum of all odd elements jo even positions pe hain.
    
    Udaharan
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    return sum([lst[i] for i in range(len(lst)) if i % 2 == 0 and lst[i] % 2 != 0])
```

This function uses list comprehension to create a list of all odd elements at even positions in the input list. It then returns the sum of these elements. The `range(len(lst))` part generates indices for all elements in the list, and the `if i % 2 == 0 and lst[i] % 2 != 0` part checks if the index is even and the element at that index is odd.