
def even_odd_count(num):
    """
    Ek integer diya gaya hai. Ek tuple return karo jo even aur odd digits ki sankhya ko kramashah darshata hai.

     Udaharan:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num_list = str(num)
    even_odd_tuple = (len(num_list) // 2,)
    
    if len(num) % 2!= 0:
        even_odd_tuple = (len(num_list) // 2 + 1,)
        
    return str(even_odd_tuple)
