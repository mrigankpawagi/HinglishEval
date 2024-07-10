
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
    a=[]
    for i in x,y,z:
        a.append(i)
        if y+z==x or x+z==y or x+y==z:
            return True
        elif y+z!=x and x+z!=y and x+y!=z:
            return False
        else:
            pass
def sum_of_list(lst1, lst2):
    """
    Ek list banao jo 2 lists ka sum ho.
    
    Udaharan
    sum_of_list([1, 2], [1.5, 4]) ➞ [2.5, 6]
    
    sum_of_list([15, 22, 32], [19, 12, 8]) ➞ [34, 34, 40]

    sum_of_list([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]) ➞ [2, 4, 6, 8, 10, 12]

    """
    for i,j in zip(lst1,lst2):
        summation=(i+j)
        l.append(round(summation,2))
        return l
def uniqueElement(array):
    """
    Ek function banao jo akele hi aaye wahi elements uthaaye jo ek array mein.
    
    Udaharan
    uniqueElement([1, 2, 3, 6, 5, 5, 4, 3, 4, 5, 5, 2, 1]) ➞ [6]
    
    uniqueElement([1, 2, 2, -3, 3, 3]) ➞ []

    uniqueElement(["a", "b", "b", "c"]) ➞ ["a", "c"]
    
    uniqueElement([[1], [2], [3], [1], [4], [3], [2]]) ➞ [[1], [3], [4]]
    """
    a=[x for x in array if array.count(x) == 1]
    if not a:
        