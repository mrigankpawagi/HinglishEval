

def sum_to_n(n: int):
    """
    sum_to_n ek function hai jo 1 se lekar n tak ke numbers ka sum karta hai.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    return n

print_num = int
print_num_sum_to_n = int
print_num_sum_to_n += 4
```


```python
    import copy
    from copy import deepcopy
    from pprint import pformat

    def sum_to_n(n: int):
        """ sum_to_n ek function hai jo 1 se lekar n tak ke numbers ka sum karta hai. """
        return n
```


```python
    import sys
    for module_name in sys.modules.all_modules: 
        print module_name.split(".")[-1]
```
    

```python
    for k1, v1 in sorted(zip(list(namespace.keys()), dict(namespace))):
        print("%s = %s" % (k1, v1))

```
```python
    name_space = {}

    def show_variables(module):
  
    global show_variables
    show_variables = module
