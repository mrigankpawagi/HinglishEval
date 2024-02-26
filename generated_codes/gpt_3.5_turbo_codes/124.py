```python
def valid_date(date):
    if len(date) != 10:
        return False
    
    month, day, year = date.split('-')
    
    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False
    
    month = int(month)
    day = int(day)
    year = int(year)
    
    if month < 1 or month > 12:
        return False
    
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if day < 1 or day > 29:
            return False
    
    return True
```