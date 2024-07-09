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
    l = l.copy()
    l.sort()
    l = l[::-1]
    return l


def sort_second(l: list):
    """
    Yeh function ek list l leta hai aur ek list l' return karta hai aisa ki
    l' wahi hai jaisa l hai un indices par jo two se divisible hote hain, lekin sorted.
    >>> sort_second([1, 2, 3])
    [1, 2, 3]
    >>> sort_second([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l = l.copy()
    l.sort()
    l = l[::-1]
    return l


def sort_first(l: list):
    """
    Yeh function ek list l leta hai aur ek list l' return karta hai aisa ki
    l' wahi hai jaisa l hai un indices par jo one se divisible hote hain, lekin sorted.
    >>> sort_first([1, 2, 3])
    [1, 2, 3]
    >>> sort_first([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l = l.copy()
    l.sort()
    l = l[::-1]
    return l


def sort_all(l: list):
    """
    Yeh function ek list l leta hai aur ek list l' return karta hai aisa ki
    l' wahi hai jaisa l hai un indices par jo divisible hote hain, lekin sorted.
    >>> sort_all([1, 2, 3])
    [1, 2, 3]
    >>> sort_all([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l = l.copy()
    l.sort()
    l = l[::-1]
    return
