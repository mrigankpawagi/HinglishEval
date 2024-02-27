

def sort_even(l: list):
    """
    Yeh function ek list l leta hai aur ek list l' return karta hai aisa ki
    l' l ke odd indices ke saath identical hota hai, jabki uske even indices ke values
    l ke even indices ke values ke barabar hoti hai, lekin sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    h = len(l)
    pos = 0
    while pos < h:
        # hoise an index ke
        pos1 = pos + 1
        temp = l[pos]

        while True:
            pos2 = pos1 + h - pos
            # hoise ke index ke
            if l[pos2] < temp:
                l[pos2], l[pos] = l[pos], l[pos2]
                pos -= 1
            else:
                break
