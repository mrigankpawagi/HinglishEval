```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    start = 0
    while start < len(string):
        index = string.find(substring, start)
        if index == -1:
            break
        count += 1
        start = index + 1
    return count
```