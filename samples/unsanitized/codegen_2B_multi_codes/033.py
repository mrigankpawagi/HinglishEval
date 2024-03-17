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
    temp = []
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[i] % l[j] == 0 and l[i] < l[j]:
                l[i], l[j] = l[j], l[i]
                temp.append(l[i])
    return sort_third(temp)


if __name__ == "__main__":
    l = [2, 5, 6, 3, 2, 1]
    print("{}".format([i[0] for i in sort_third(l)]))

    l = [
        3,
        1,
        4,
        2,
        9,
        8,
        1,
        5,
        7,
        7,
        6,
        8,
        8,
        9,
        1,
        4,
        7,
        8,
        3,
        5,
        7,
        8,
        2,
        12,
        5,
        2,
        13,
        1,
    ]
    print("{}".format([i[0] for i in sort_third(l)]))
