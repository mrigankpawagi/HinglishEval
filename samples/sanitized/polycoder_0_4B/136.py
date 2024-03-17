def largest_smallest_integers(lst):
    """
    Ek function banao jo ek tuple (a, b) return kare, jahan 'a' negative integers ka sabse bada hai, aur 'b' positive integers ka sabse chota hai ek list mein.
    Agar koi negative ya positive integers nahi hai, to unhe None ke roop mein return karo.

    Udaharan:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    """
    jay_lo_hi = set([y for y in lst if y != None])

    a = [0, 0, 1, 0, 0]
    for x, j in jay_lo_hi:
        if a[x] == j:
            j += 1
        else:
            a[x] = j
    for i in jay_lo_hi:
        a[i] = 0

    a_max_k = set(a)
    a_max_k = sorted(a_max_k)
    a_sum = sum(a_max_k)
    return a_sum

    ################################################################
    # return k as list
    #
    # to be confused by return k as list, when one or three return values are assigned to
    # a set as the list, then by an operation that return the elements of the list -
    # e.g. sort, sort_list, reverse, etc.
    #
    # if more than one element is in the list - the set will not change - no special action is taken
    #
