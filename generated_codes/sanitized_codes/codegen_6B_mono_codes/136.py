def largest_smallest_integers(lst):
    """
    Ek function banao jo ek tuple (a, b) return kare, jahan 'a' negative integers ka sabse bada hai, aur 'b' positive integers ka sabse chota hai ek list mein.
    Agar koi negative ya positive integers nahi hai, to unhe None ke roop mein return karo.
    Udaharan:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    """
    if len(lst) == 0:
        return (None, None)
    negative_items = [-k for k in lst if k < 0]
    positive_items = [k for k in lst if k > 0]
    if len(positive_items) == 0:
        return (None, None)
    max_neg, min_pos = max(negative_items), min(positive_items)
    if max_neg == min_pos:
        return (max_neg, max_neg)
    else:
        return (max_neg, None)