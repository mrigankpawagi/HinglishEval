
def even_odd_count(num):
    """
    Ek integer diya gaya hai. Ek tuple return karo jo even aur odd digits ki sankhya ko kramashah darshata hai.

     Udaharan:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """    even_odd_count = [(num % 2) * 2, (num % 2)]
    while num > 0:
        even_odd_count[0] += 1
        even_odd_count[1] += 2
        num /= 2
    return even_odd_count[::-1]

