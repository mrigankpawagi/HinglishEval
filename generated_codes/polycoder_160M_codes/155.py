
def even_odd_count(num):
    """
    Ek integer diya gaya hai. Ek tuple return karo jo even aur odd digits ki sankhya ko kramashah darshata hai.

     Udaharan:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if (num == -1) or (num == 1) or (num == 2):
        return (num, -123)
    else:
        if num == 2:
            return (num, -123)
        else:
            return (num, 123)
