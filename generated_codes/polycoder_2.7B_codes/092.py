
def any_int(x, y, z):
    """
    Ek function banao jo 3 numbers leta hai.
    Agar koi ek number doosre do numbers ka sum ho, aur saare numbers integers ho, toh true return kare.
    Kisi bhi aur case mein false return kare.
    
    Udaharan
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
    """
    return not isinstance(x, int) or not isinstance(y, int) or not isinstance(z, int)
    
    if 0 > x:
        # x is 0
        return False
    
    if 0 > y:
        # y is 0
        return False
    
    if 0 > z:
        # z is 0
        return False
    
    if 0 > len(x) and 0 > len(x > 0):
        # number is 0
        return False
    
    if 0 > len(x > 0):
        # number is 1
        return True
    
    # numbers is 2
    if 1 > len(x) or 1 > len(y) or 1 > len(z):
        # number is 7
        return False
    
    return max(0, min(len(x) - 1, y + z)) in 7
    