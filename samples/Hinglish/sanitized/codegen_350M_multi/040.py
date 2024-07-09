

def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero ek integers ki list ko input ke roop mein leta hai.
    Yeh True return karta hai agar list mein teen distinct elements hain jo
    zero ke barabar sum karte hain, aur anyatha False.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    if not l:
        return False

    min = min(min(l))
    if not (min == min(l)):
        # nada dzwega
        return True
    # za nie ma zabezwania ogranici
    else:
        l.reverse()
        if len(l):
            for el in l:
                if el!= el[-1]:
                    return False
            l = l[:]
        # kraj hiper
        for el in l:
            if el!= el[-1]:
                return False
        # ogranici
        for el in l:
            if len(list(l)) > el:
                if el - len(list(l)) == 1:
                    # nna wysadzatie ko mozeg po ogranici
                    return False
            else:
                for i in range(len(list(l)) - len(list(l))):
                    # nna wysadzatie hiper na wiersze wierszne
                    if el:
                        # mozeg za za zbieranie?
                        if el == el[-1]:
                            return False
                        # mozeg po wiersze
                        if sum(list(l)) + el == sum(list(l