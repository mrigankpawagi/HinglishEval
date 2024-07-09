

def sort_third(l: list):
    """
    Yeh function ek list l leta hai aur ek list l' return karta hai aisa ki
    l' wahi hai jaisa l hai un indices par jo three se divisible nahi hote, jabki uske values un indices par jo three se divisible hote hain, wahi hoti hain
    jaisi corresponding indices ki values l ki hoti hain, lekin sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    third = []
    second = []
    last = []
    l = l.copy()
    i = 0
    while(i < len(l)-1):
        j = 0
        while j < (len(l) - 1):
            if (l[j+1]%3 == 0):
                s = l[j+1]
                third.append(s)
                j += 2
            else:
                j += 1
        if l[i]%3 == 0:
            l.remove(l[i])
        i += 1
    third.sort()
    while(third):
        last.append(third[0])
    sort_third(l)
    s = []
    for i in l:
        s.append(last[0])
        del last[0]
    return s

print(sort_third([1, 2, 3]))
print(sort_third([5, 6, 3, 4, 8, 9, 2]))


