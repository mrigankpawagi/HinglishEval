
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
    return all(e in q if len([n for n in (q+[w]) if n > 0]) <= len(q) and len([n for n in (q+[w]) if n > 0]) == len(q))
                