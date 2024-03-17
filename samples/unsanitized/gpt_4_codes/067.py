```python
def fruit_distribution(s,n):
    fruits = s.split()
    apples = int(fruits[0])
    oranges = int(fruits[3])
    mangoes = n - apples - oranges
    return mangoes
```