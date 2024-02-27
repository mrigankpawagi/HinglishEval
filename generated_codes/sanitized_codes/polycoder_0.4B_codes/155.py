
def even_odd_count(num):
    """
    Ek integer diya gaya hai. Ek tuple return karo jo even aur odd digits ki sankhya ko kramashah darshata hai.

     Udaharan:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    count = 0
    for i in xrange(num):
        count++ if i % 2 == 0 or i % 5 == 0:
            break
    return 1 + index_str(count)

