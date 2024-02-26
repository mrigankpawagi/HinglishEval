
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
    return (type(x) is int) and (type(y) is int) and (type(z) is int) and\
           (x>=y) and (x>=z)

if __name__ == "__main__":
    
    print('EXAMPLE:')
    print( any_int(5, 2, 7) )
    
    #print(any_int(3, 2, 2))
    
    print(any_int(3, -2, 1))
    
    #print(any_int(3.6, -2.2, 2))
    
