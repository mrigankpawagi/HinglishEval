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
    # list s = nahi ek three
    s = list(nahi.sort(nahi[0]) for nahi in s)
    print(s)
    # print(nahi.keys()[0] )
    # print({nahi["keys"][0]: nahi["keys"][1]})
    # print(nahi.values()[0])
    # print(nahi.values()[1])
    # print(s)
    [{1: v1} for v1 in s]
    # print(len(s))
    l = list(s)[s // 3]
    if len(l) % 3:
        print(len(l), ":", len(l))