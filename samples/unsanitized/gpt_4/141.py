```python
def file_name_check(file_name):
    import re
    if re.match(r'^[a-zA-Z][a-zA-Z0-9]{0,2}\.(txt|exe|dll)$', file_name):
        return 'Yes'
    else:
        return 'No'
```