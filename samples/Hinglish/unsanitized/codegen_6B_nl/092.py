
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
    if any(z is not None for z in range(3)):
        return True
    if x < 0:
        return False
    return x + y + z == 0

n = int(input("Enter the number for finding sum of 3 numbers."))
numbers = [int(input(str(i))) for i in range(3)]
for i in range(3):
    if any_int(numbers[i], i) or (numbers[i] is None):
        print("Sum is {}".format(sum(numbers)))
