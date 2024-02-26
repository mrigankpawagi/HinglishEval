```python
def odd_count(lst):
    output = []
    for string in lst:
        count = sum(1 for char in string if int(char) % 2 != 0)
        output.append(f"input ki string {len(string)} mein odd elements ki sankhya {count}.")
    return output
```