
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
    
    return x == int("0x"+y +z) or (bool(x) and bool(y) and bool(z))


print(any_int(3,2,7))
print(any_int(4,3,123))
print(any_int(-3, 4, -1))
print(any_int(7, 3, 45))

# =======================================================

# OOPS

print(bool(True))            # True
print(bool(False))           # false
print(bool(0))              # 0
print(bool(0.0))            # 0.0
print(bool(None))           # None
print(bool([]))             # []
print(bool(()) ())        # ()
print(bool(())()))        # ()
print(bool(""))            # False
print(bool(()))             # False
print(bool("(") )            # False
print(bool("))"))          # False
print(bool("[{{"))        # False
print((True))            # True
print((True))           # True
print((False))          # False
print((False))          # False

# ===========================================================
# OOPS 2

# Kategoriye
name="John"
type="J"
age=45
color="#ffb000"
print("Name of Person is: "+ name + str(gender))
print("Gender is:" + gender)
print("Age is : " + str(age))
print(f"