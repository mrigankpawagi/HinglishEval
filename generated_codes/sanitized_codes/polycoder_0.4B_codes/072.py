def will_it_fly(q, w):
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
    Udo = q - 1
    Udo = Udo * Udo / 2
    Culpr = Udo * Udo * Udo
    Tol = Math.sqrt(Udo)
    Weight = 1000 / Tol  # weight per 100 objects
    Wi = w - 1
    M = L * Wi
    if Culpr < 0.9 * Weight:
        return False
    elif M <= Weight:
        return True
    else:
        return False
