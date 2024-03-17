
def even_odd_count(num):
    """
    Ek integer diya gaya hai. Ek tuple return karo jo even aur odd digits ki sankhya ko kramashah darshata hai.
     Udaharan:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    tup = ()
    if num == 0:
        return ("zero", 1)
    if num % 2:
        first_int = num // 2
        first_value = even_odd_count(first_int)
        first_value = (first_value!= 1) and (first_value!= 2)
        return (first_value, 2)
    else:
        second_int = num // 2
        second_value = even_odd_count(second_int)
        second_value = (second_value!= 1) and (second_value!= 2)
        return (2, (first_value if first_value else second_value))
    return False