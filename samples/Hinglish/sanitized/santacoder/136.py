def largest_smallest_integers(lst):
    """
    Ek function banao jo ek tuple (a, b) return kare, jahan 'a' negative integers ka sabse bada hai, aur 'b' positive integers ka sabse chota hai ek list mein.
    Agar koi negative ya positive integers nahi hai, to unhe None ke roop mein return karo.

    Udaharan:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    """
    biggest = a_negative_integer = b_positive_integer = None
    for i in lst:
        if a_negative_integer is None and i < 0:
            a_negative_integer = i
        if b_positive_integer is None and i > 0:
            b_positive_integer = i
        if i > biggest and i >= 0:
            biggest = i

    return (a_negative_integer, b_positive_integer)
