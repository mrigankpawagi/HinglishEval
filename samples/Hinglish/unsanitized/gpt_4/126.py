Here is the Python function that fulfills the requirements mentioned in the docstring:

```python
def is_sorted(lst):
    """
    Ek numbers ki list di gayi hai, return karo ki kya ye ascending order mein sorted hai ya nahi. Agar list mein ek se jyada same number ke duplicate hain, to False return karo. Maan lo ki koi negative number nahi hai aur sirf integers hain.

    Udaharan
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    """
    return lst == sorted(lst) and len(lst) == len(set(lst))
```

This function first checks if the list is sorted in ascending order by comparing it with its sorted version. If the list is not sorted, the function will return False. Then it checks if there are any duplicate numbers in the list by comparing the length of the list with the length of the set of the list (which removes duplicates). If there are duplicates, the function will return False. If both conditions are met, the function will return True.