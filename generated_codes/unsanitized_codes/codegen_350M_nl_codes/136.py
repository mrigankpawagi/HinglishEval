
def largest_smallest_integers(lst):
    """
    Ek function banao jo ek tuple (a, b) return kare, jahan 'a' negative integers ka sabse bada hai, aur 'b' positive integers ka sabse chota hai ek list mein.
    Agar koi negative ya positive integers nahi hai, to unhe None ke roop mein return karo.

    Udaharan:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    """
    smallest = None
    lst.append([])
    i = 0
    if lst.len() - i < 2:
        smallest = lst[-1]
    elif i < 1:
        smallest = min(lst, key = lambda i: i+1)
    elif i == lst.len() - i > 2:
        smallest = None
    else:
        smallest = lst[-i]

    return lambda x: largest_smallest_integers(x) + smaller


@functions
