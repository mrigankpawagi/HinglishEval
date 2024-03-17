
def even_odd_count(num):
    """
    Ek integer diya gaya hai. Ek tuple return karo jo even aur odd digits ki sankhya ko kramashah darshata hai.

     Udaharan:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    total = int(num * 0.01)
    return (total % 2, total // 2) if num < 2 else (total - 1, total - 1) if num > 2 else ()
