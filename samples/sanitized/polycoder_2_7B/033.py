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
    # kara indices
    indicesA = l.count(4)
    keys = sorted(x for x in indicesA)
    # jaisa indices, jabki indices
    indicesB = l.count(6)
    keys_b = sorted(x for x in indicesB)
    # haki un indices
    l2 = l[:-2]
    # ni indices
    keys_a = sorted(x for x in l2 if x[1] != 0)
    # leki indices nahi indices
    keys = sorted(keys)
    # indices ki un indices
    indicesB[1:4] = l[1:-2]
    l[l.count(1) + 1] = l[-2:]
    l += [keys, indicesB]
    l2 = l2 + [keys_a, keys_b]
    return l2
