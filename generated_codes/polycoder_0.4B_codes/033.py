

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
    idx = None
    if isinstance(l, list):
        for ind, i in zip(l, range(len(l))):
            if i!= ind:
                idx = (i, ind)
                break
            if i == 0:
                return
        else:
            return i
    else:
        return l
    for idxs in sorted(idx, key=lambda k: get(idxs, k)):
        return idxs

