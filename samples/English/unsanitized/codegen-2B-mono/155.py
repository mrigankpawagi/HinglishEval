
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even = 0
    odd = 0
    while num > 0:
        even = (even + num % 10) if num % 2 == 0 else odd
        odd = (odd + num % 10) if num % 2 == 1 else even
        num = num // 10
    return even, odd

# I found this code somewhere below my library. thanks!
