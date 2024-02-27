def even_odd_count(num):
    """
    Ek integer diya gaya hai. Ek tuple return karo jo even aur odd digits ki sankhya ko kramashah darshata hai.
     Udaharan:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_odd_count_ = dict()
    if num < 0:
        while num != 0:
            num = num // 10
            if num % 2 == 0:
                even_odd_count_[num] = 1
            else:
                even_odd_count_[num] = 2
        return even_odd_count_
    elif num % 2 == 0:
        return even_odd_count_
    else:
        return even_odd_count_