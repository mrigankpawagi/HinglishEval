```python
def sort_even(l: list):
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    sorted_even_indices = sorted(even_indices)
    sorted_list = []
    for i in range(len(l)):
        if i % 2 == 0:
            sorted_list.append(sorted_even_indices.pop(0))
        else:
            sorted_list.append(l[i])
    return sorted_list
```