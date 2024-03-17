def largest_smallest_integers(lst):
    """
    Ek function banao jo ek tuple (a, b) return kare, jahan 'a' negative integers ka sabse bada hai, aur 'b' positive integers ka sabse chota hai ek list mein.
    Agar koi negative ya positive integers nahi hai, to unhe None ke roop mein return karo.
    Udaharan:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    """
    if len(lst) <= 0:
        return None, None
    res = max_int_val, None
    try:
        a, b = sum(lst), sorted(lst)[-1]
        if a <= b:
            res, n = largest_smallest_integers(lst[: a - 1])
        elif a > b:
            res, n = largest_smallest_integers(lst[: b - 1])
    except ValueError:
        res, n = largest_smallest_integers([0])
    return res, n