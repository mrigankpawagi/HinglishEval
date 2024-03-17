```python
def is_nested(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()
    return len(stack) == 0 and '][' not in string
```