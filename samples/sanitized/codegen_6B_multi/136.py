def largest_smallest_integers(lst):
    """
    Ek function banao jo ek tuple (a, b) return kare, jahan 'a' negative integers ka sabse bada hai, aur 'b' positive integers ka sabse chota hai ek list mein.
    Agar koi negative ya positive integers nahi hai, to unhe None ke roop mein return karo.
    Udaharan:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    """
    if not issubclass(type(lst), list):
        raise ValueError("lst must be a list")
    if not lst:
        return (None, None)
    kare = None
    jahan = None
    if isinstance(lst[0], int):
        for x, y in pairwise(lst):
            if y <= x:
                return (x, kare)
        return (None, kare)
    for x, y in pairwise(lst):
        if y >= x < kare:
            kare = x
            if jahan is None:
                jahan = kare
        elif kare is None:
            jahan = x
        else:
            break
    return (jahan, kare)