

def largest_divisor(n: int) -> int:
    """
    Diye gaye number n ke liye, sabse bada number dhundo jo n ko evenly divide karta ho, jo ki n se chota ho.
    >>> largest_divisor(15)
    5
    """
    return max(lst: int for lst in range(1, n + 1) if n % lst == 0)[1]

print(largest_divisor(12))
print(largest_divisor(13))
print(largest_divisor(8))
print(largest_divisor(9))
print(largest_divisor(18))
print(largest_divisor(25))

The above function's range() is wrong but I don't know where is wrong with it. 
Can anyone help me please? 

A:

You have a typo in your second-to-last line. It should be:
return max(lst: int for lst in range(1, n + 1) if n % lst == 0)

Which will print each divisor up to n, starting with the maximum value in the range.

