
def will_it_fly(q,w):
    """
    Ek function likho jo True return kare agar object q udega, aur False otherwise.
    Object q tabhi udega jab vo balanced ho (yani ki ek palindromic list ho) aur uske elements ka sum maximum possible weight w se kam ya barabar ho.

    Udaharan:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 maximum possible weight se kam hai, lekin ye balanced nahi hai.

    will_it_fly([3, 2, 3], 1) ➞ False
    # ye balanced hai, lekin 3+2+3 maximum possible weight se jyada hai.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 maximum possible weight se kam hai, aur ye balanced hai.

    will_it_fly([3], 5) ➞ True
    # 3 maximum possible weight se kam hai, aur ye balanced hai.
    """
    if len(q)==0:
        return False
    # jadikan element ho q tablo da sakas yano agar he tahan kadye da tahan sakas 
    if q[0]==w:
        # kalau sakas ek palindromic list udahe ek ek kol ek palindromic list ho
        if type(q)==list:
            return will_it_fly(q[1:], w)
        else:
            return False
    else:
        return will_it_fly(q[1:], w-q[0])
