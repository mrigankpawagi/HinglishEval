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
    if x == y and x == z:
        return True
    else:
        return False


class User:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


u1 = User("Rahul", 34, 1, 1)
u2 = User("Amit", 23, 82, 24)
u3 = User("Meenitha", 20, 23, 1.5)
print(any_int(1, u1.age, u1.height))
