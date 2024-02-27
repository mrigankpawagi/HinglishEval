Here is the Python function that fulfills the requirements of the given docstring:

```python
def iscube(a):
    """
    Ek function likho jo ek integer a leta hai aur True return karta hai 
    agar yeh integer kisi integer number ka cube hai.
    Dhyan de: aap maan sakte ho ki input hamesha valid hoga.
    Udaharan:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    """
    cube_root = round(a ** (1. / 3))
    return cube_root ** 3 == a
```