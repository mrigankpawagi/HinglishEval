
def even_odd_count(num):
    """
    Ek integer diya gaya hai. Ek tuple return karo jo even aur odd digits ki sankhya ko kramashah darshata hai.

     Udaharan:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even = 0
    odd = 0
    for i in str(num):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)

