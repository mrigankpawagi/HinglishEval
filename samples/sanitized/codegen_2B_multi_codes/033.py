

def sort_third(l: list):
    """
    Yeh function ek list l leta hai aur ek list l' return karta hai aisa ki
    l' wahi hai jaisa l hai un indices par jo three se divisible nahi hote, jabki uske values un indices par jo three se divisible hote hain, wahi hoti hain
    jaisi corresponding indices ki values l ki hoti hain, lekin sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """   temp = []
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[i] % l[j] == 0 and l[i] < l[j]:
                l[i], l[j] = l[j], l[i]
                temp.append(l[i])
    return sort_third(temp)

