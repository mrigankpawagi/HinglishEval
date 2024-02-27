
def even_odd_count(num):
    """
    Ek integer diya gaya hai. Ek tuple return karo jo even aur odd digits ki sankhya ko kramashah darshata hai.

     Udaharan:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    return (num % 10, num % 2)

print(even_odd_count(123))  # 1, 2
print(even_odd_count(456))  # 3, 4
print(even_odd_count(-123))  # 2, 1
print(even_odd_count(12))  # 1, 2
print(even_odd_count(12345))  # 3, 5

I want to use this algorithm to find the unique digits in any string. If the string contains digits a, b, c, d, then a, b are the unique digits and c, d are not unique.

A:

I think you can use collections.Counter for this:
from collections import Counter
print(Counter(str('abcdd')))

Output:
Counter({'d': 2, 'c': 1, 'b': 1})

