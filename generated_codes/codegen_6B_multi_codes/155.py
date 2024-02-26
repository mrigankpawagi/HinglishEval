
def even_odd_count(num):
    """
    Ek integer diya gaya hai. Ek tuple return karo jo even aur odd digits ki sankhya ko kramashah darshata hai.

     Udaharan:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    if num== 0:
        return 0
    elif num < 0:
        return (-1, even_odd_count(-num))
    else:
        odd, odd_digit = even_odd_count(num // 2)
        even, even_digit = even_odd_count(num - odd)
        return (odd, even)

print even_odd_count(123)
