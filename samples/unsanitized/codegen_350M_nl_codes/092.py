
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

    if any_int(x, y, z) is not any_int(3, 2, 7):
        pass
    # print any_int(x, y, z)
    return True

if __name__ == '__main__':
    any_int = any_int()
    if any_int(5, 2, 7):
        print(any_int(5, 2, 7))

A:

That code produces a False! Why? There's a value in the output (the last output) that isn't True. You're checking for an integer, not for an array, so you must actually compare the input arguments using ==. For example,
>>> any_int(x, y, z)
<genexpr>

is equivalent to
>>> any_int(5, 2, 7) == 5
True

In general, if you don't want to handle False errors (i.e. the errors aren't about boolean values) use this rule of thumb
In this example, True is equivalent to checking the input argument x and returning True
import operator

