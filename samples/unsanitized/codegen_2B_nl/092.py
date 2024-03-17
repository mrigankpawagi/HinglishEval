
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
    if any(x > 0 and y > 0 and z > 0):
        return True
    if any(y > 0 and z > 0 and x > 0):
        return True
    if any(x > 0 and y > 0 and not z > 0):
        return True
    if any(y > 0 and not z > 0 and x > 0):
        return True
    if any(x > 0 and y > 0 and z > 0):
        return True
    if any(y > 0 and z > 0 and not x > 0):
        return True
    if any(z > 0 and not x > 0 and y > 0):
        return True
    return False


