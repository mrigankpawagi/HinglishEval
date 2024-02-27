Sure, here is the completed Python function:

```python
def even_odd_count(num):
    """
    Ek integer diya gaya hai. Ek tuple return karo jo even aur odd digits ki sankhya ko kramashah darshata hai.

     Udaharan:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num = abs(num)
    even_count = 0
    odd_count = 0
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num = num // 10
    return (even_count, odd_count)
```

This function works by converting the input number to its absolute value (to handle negative numbers), then repeatedly dividing the number by 10 and checking the remainder (which is the last digit of the number). If the remainder is even, it increments the even count; if it's odd, it increments the odd count. It continues this process until the number is 0, at which point it returns a tuple of the even and odd counts.